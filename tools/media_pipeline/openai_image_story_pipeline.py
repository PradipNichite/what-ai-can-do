#!/usr/bin/env python3
"""Run image-story generation, contact sheet creation, and QA under one trace."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from build_contact_sheet import build_contact_sheet, collect_images
from openai_image_story_generate import (
    generate_lesson_single_request,
    generate_one,
    output_path_for_card,
    parse_prompt_pack,
    resolve_style_references,
)
from openai_visual_qa import load_dotenv, resolve_path, run_visual_qa, write_outputs
from pipeline_tracing import end_trace, flush_traces, trace_id, trace_run


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IMAGE_MODEL = "gpt-image-2"
DEFAULT_IMAGE_AGENT_MODEL = "gpt-5.5"
DEFAULT_QA_MODEL = "gpt-5.5"


def rel_path(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def run_gate(prompt_pack: Path) -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_image_story_gate.py", rel_path(prompt_pack)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stdout)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate and QA an OpenAI image-story lesson under one trace."
    )
    parser.add_argument("--prompt-pack", required=True)
    parser.add_argument("--source-module", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--mode", default="image-story", choices=["image-story"])
    parser.add_argument("--image-model", default=os.environ.get("OPENAI_IMAGE_MODEL") or DEFAULT_IMAGE_MODEL)
    parser.add_argument("--image-agent-model", default=os.environ.get("OPENAI_IMAGE_AGENT_MODEL") or DEFAULT_IMAGE_AGENT_MODEL)
    parser.add_argument("--qa-model", default=os.environ.get("OPENAI_VISION_QA_MODEL") or DEFAULT_QA_MODEL)
    parser.add_argument("--size", default="1024x1536")
    parser.add_argument("--quality", default="medium")
    parser.add_argument("--output-format", default="png", choices=["png", "jpeg", "webp"])
    parser.add_argument(
        "--output-compression",
        type=int,
        default=(
            int(os.environ["OPENAI_IMAGE_OUTPUT_COMPRESSION"])
            if os.environ.get("OPENAI_IMAGE_OUTPUT_COMPRESSION")
            else None
        ),
        help="Compression level for jpeg/webp outputs when supported.",
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=int(os.environ.get("OPENAI_MAX_PARALLEL_IMAGES", 3)),
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("OPENAI_REQUEST_TIMEOUT_SECONDS", 180)),
    )
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument(
        "--style-reference",
        action="append",
        help="Reference image for style/character/composition. Can be repeated.",
    )
    parser.add_argument(
        "--reference-strategy",
        choices=["all-cards", "anchor-after-first", "single-request-lesson", "none"],
        default=os.environ.get("OPENAI_IMAGE_REFERENCE_STRATEGY", "anchor-after-first"),
        help=(
            "How to pass style references. anchor-after-first generates the anchor card "
            "with external refs, then uses that generated card for the rest. "
            "single-request-lesson asks one OpenAI request to return all lesson frames."
        ),
    )
    parser.add_argument(
        "--character-anchor-card",
        type=int,
        default=int(os.environ.get("OPENAI_IMAGE_CHARACTER_ANCHOR_CARD", 1)),
        help="Card number to generate first and reuse as the lesson character anchor.",
    )
    parser.add_argument(
        "--only-card",
        type=int,
        action="append",
        help="Generate only the specified card number. Can be repeated.",
    )
    parser.add_argument("--skip-qa", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    load_dotenv()
    parser = build_arg_parser()
    args = parser.parse_args()
    try:
        if not os.environ.get("OPENAI_API_KEY") and not args.dry_run:
            raise RuntimeError("OPENAI_API_KEY is not set.")

        prompt_pack = resolve_path(args.prompt_pack)
        source_module = resolve_path(args.source_module)
        out_dir = resolve_path(args.out_dir)
        if prompt_pack is None or source_module is None or out_dir is None:
            raise ValueError("--prompt-pack, --source-module, and --out-dir are required.")
        if args.output_compression is not None and args.output_format not in {"jpeg", "webp"}:
            raise ValueError("--output-compression is only valid with --output-format jpeg or webp.")

        all_cards = parse_prompt_pack(prompt_pack)
        cards = all_cards
        if args.only_card:
            selected = set(args.only_card)
            cards = [card for card in cards if int(card["number"]) in selected]
            if not cards:
                raise ValueError(f"No matching cards found for --only-card {sorted(selected)}")
        anchor_card = next(
            (card for card in all_cards if int(card["number"]) == args.character_anchor_card),
            None,
        )
        lesson_slug = prompt_pack.stem.replace("-image-story", "")
        pipeline_run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        contact_sheet = out_dir / f"{out_dir.name}-contact-sheet.jpg"
        qa_md = out_dir / f"{out_dir.name}-qa.md"
        qa_json = out_dir / f"{out_dir.name}-qa.json"

        lesson_metadata: dict[str, object] = {
            "lesson_slug": lesson_slug,
            "pipeline_run_id": pipeline_run_id,
            "pipeline_stage": "image_story_pipeline",
            "request_group": "image_story_lesson",
            "prompt_pack": rel_path(prompt_pack),
            "source_module": rel_path(source_module),
            "out_dir": rel_path(out_dir),
            "image_model": args.image_model,
            "image_agent_model": args.image_agent_model,
            "qa_model": args.qa_model,
            "parallel": args.parallel,
            "style_references": args.style_reference or [],
            "reference_strategy": args.reference_strategy,
            "character_anchor_card": args.character_anchor_card,
        }
        lesson_tags = [
            "media-pipeline",
            "image-story",
            "openai",
            f"lesson:{lesson_slug}",
            "stage:pipeline",
        ]
        summary = {
            **lesson_metadata,
            "cards": [
                {
                    "number": card["number"],
                    "title": card["title"],
                    "output_path": rel_path(output_path_for_card(out_dir, card, args.output_format)),
                }
                for card in cards
            ],
            "contact_sheet": rel_path(contact_sheet),
            "qa_md": rel_path(qa_md),
            "qa_json": rel_path(qa_json),
        }
        if args.dry_run:
            print(json.dumps(summary, indent=2))
            return 0

        out_dir.mkdir(parents=True, exist_ok=True)
        with trace_run(
            "image-story lesson pipeline",
            run_type="chain",
            inputs=summary,
            metadata=lesson_metadata,
            tags=lesson_tags,
        ) as lesson_run:
            with trace_run(
                "verify image-story gate",
                run_type="tool",
                parent=lesson_run,
                inputs={"prompt_pack": rel_path(prompt_pack)},
                metadata={**lesson_metadata, "request_type": "local_gate_check"},
                tags=["media-pipeline", "gate-check", f"lesson:{lesson_slug}"],
            ) as gate_run:
                run_gate(prompt_pack)
                end_trace(gate_run, {"status": "pass"})

            image_args = SimpleNamespace(
                model=args.image_model,
                image_agent_model=args.image_agent_model,
                size=args.size,
                quality=args.quality,
                output_format=args.output_format,
                output_compression=args.output_compression,
                timeout=args.timeout,
                retries=args.retries,
                style_reference=args.style_reference,
            )
            results: list[dict[str, object]] = []
            base_style_references = (
                [] if args.reference_strategy == "none" else resolve_style_references(args.style_reference)
            )
            if args.reference_strategy == "single-request-lesson":
                results.extend(
                    generate_lesson_single_request(
                        cards,
                        image_args,
                        prompt_pack,
                        out_dir,
                        lesson_run,
                        lesson_metadata,
                        base_style_references,
                    )
                )
            else:
                remaining_cards = list(cards)
                card_style_references = base_style_references

                if args.reference_strategy == "anchor-after-first" and anchor_card is not None:
                    anchor_path = output_path_for_card(out_dir, anchor_card, args.output_format)
                    selected_anchor = next(
                        (card for card in remaining_cards if int(card["number"]) == args.character_anchor_card),
                        None,
                    )
                    if selected_anchor is not None:
                        results.append(
                            generate_one(
                                selected_anchor,
                                image_args,
                                prompt_pack,
                                out_dir,
                                lesson_run,
                                lesson_metadata,
                                base_style_references,
                            )
                        )
                        remaining_cards = [
                            card
                            for card in remaining_cards
                            if int(card["number"]) != args.character_anchor_card
                        ]
                        card_style_references = [anchor_path]
                    elif anchor_path.exists():
                        card_style_references = [anchor_path]

                with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as executor:
                    futures = [
                        executor.submit(
                            generate_one,
                            card,
                            image_args,
                            prompt_pack,
                            out_dir,
                            lesson_run,
                            lesson_metadata,
                            card_style_references,
                        )
                        for card in remaining_cards
                    ]
                    for future in as_completed(futures):
                        results.append(future.result())

            generation_run = {
                "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                **summary,
                "langsmith_trace_id": trace_id(lesson_run),
                "results": sorted(results, key=lambda item: int(item["card_number"])),
            }
            (out_dir / "generation-run.json").write_text(
                json.dumps(generation_run, indent=2) + "\n",
                encoding="utf-8",
            )

            with trace_run(
                "build contact sheet",
                run_type="tool",
                parent=lesson_run,
                inputs={"image_folder": rel_path(out_dir), "out": rel_path(contact_sheet)},
                metadata={**lesson_metadata, "request_type": "local_contact_sheet"},
                tags=["media-pipeline", "contact-sheet", f"lesson:{lesson_slug}"],
            ) as sheet_run:
                build_contact_sheet(collect_images(out_dir), contact_sheet, 4, 320, 32)
                end_trace(sheet_run, {"contact_sheet": rel_path(contact_sheet)})

            qa_status = None
            qa_next_action = None
            qa_openai_request_id = None
            if not args.skip_qa:
                qa_args = SimpleNamespace(
                    image_folder=rel_path(out_dir),
                    contact_sheet=rel_path(contact_sheet),
                    prompt_pack=rel_path(prompt_pack),
                    source_module=rel_path(source_module),
                    mode=args.mode,
                    out=rel_path(qa_md),
                    json_out=rel_path(qa_json),
                    model=args.qa_model,
                    timeout=args.timeout,
                    include_folder_images=False,
                )
                response, qa_openai_request_id = run_visual_qa(
                    qa_args,
                    [contact_sheet],
                    os.environ["OPENAI_API_KEY"],
                    lesson_run,
                    lesson_metadata,
                )
                if response.output_parsed is None:
                    raise RuntimeError("OpenAI QA response did not include parsed output.")
                verdict = response.output_parsed.model_dump()
                qa_status = verdict["status"]
                qa_next_action = verdict["next_action"]
                write_outputs(
                    verdict,
                    str(getattr(response, "id", "")),
                    qa_args,
                    [contact_sheet],
                    qa_openai_request_id,
                )

            status = {
                "status": qa_status or "generated",
                "next_action": qa_next_action,
                "lesson_slug": lesson_slug,
                "pipeline_run_id": pipeline_run_id,
                "langsmith_trace_id": trace_id(lesson_run),
                "out_dir": rel_path(out_dir),
                "contact_sheet": rel_path(contact_sheet),
                "qa_md": rel_path(qa_md) if qa_status else None,
                "qa_json": rel_path(qa_json) if qa_status else None,
                "qa_openai_request_id": qa_openai_request_id,
            }
            (out_dir / "pipeline-status.json").write_text(
                json.dumps(status, indent=2) + "\n",
                encoding="utf-8",
            )
            end_trace(lesson_run, status)

        flush_traces()
        print(json.dumps(status, indent=2))
        return 0
    except Exception as exc:
        print(f"openai_image_story_pipeline failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
