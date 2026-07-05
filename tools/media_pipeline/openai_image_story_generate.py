#!/usr/bin/env python3
"""Generate image-story cards with OpenAI image models in parallel."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from openai_visual_qa import build_openai_client, image_to_data_url, load_dotenv, resolve_path
from pipeline_tracing import end_trace, flush_traces, trace_id, trace_run


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IMAGE_MODEL = "gpt-image-2"
DEFAULT_IMAGE_AGENT_MODEL = "gpt-5.5"
DEFAULT_PARALLEL = 3


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:64] or "card"


def parse_prompt_pack(path: Path) -> list[dict[str, str | int]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    heading = r"^#{2,3}\s+(?:Card|Frame)\s+\d+\s*[-:]"
    pattern = re.compile(
        r"^#{2,3}\s+(?:Card|Frame)\s+(\d+)\s*[-:]\s*(.+?)\s*$"
        rf"(.*?)(?={heading}|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    cards: list[dict[str, str | int]] = []
    for match in pattern.finditer(text):
        number = int(match.group(1))
        title = match.group(2).strip()
        body = match.group(3)
        prompt_match = re.search(
            r"Prompt:\s*```(?:text)?\s*(.*?)```", body, re.IGNORECASE | re.DOTALL
        )
        if not prompt_match:
            continue
        cards.append(
            {
                "number": number,
                "title": title,
                "prompt": prompt_match.group(1).strip(),
            }
        )
    if not cards:
        raise ValueError(f"No card/frame prompts found in {path}")
    return sorted(cards, key=lambda item: int(item["number"]))


def output_path_for_card(out_dir: Path, card: dict[str, str | int], output_format: str) -> Path:
    number = int(card["number"])
    title = str(card["title"])
    return out_dir / f"{number:02d}-{slugify(title)}.{output_format}"


def resolve_style_references(raw_paths: list[str] | None) -> list[Path]:
    paths: list[Path] = []
    for raw_path in raw_paths or []:
        path = resolve_path(raw_path)
        if path is None:
            continue
        if not path.exists():
            raise FileNotFoundError(f"Style reference not found: {path}")
        paths.append(path)
    return paths


def build_image_generation_input(prompt: str, style_references: list[Path]) -> str | list[dict[str, object]]:
    if not style_references:
        return prompt

    content: list[dict[str, object]] = [
        {
            "type": "input_text",
            "text": (
                "Use the attached reference images only for visual style, composition grammar, "
                "character continuity, warm Indian study-desk atmosphere, native integrated "
                "text treatment, and mobile story-card polish. Do not copy their topic. "
                "Generate the new requested educational story card.\n\n"
                + prompt
            ),
        }
    ]
    for path in style_references:
        content.append({"type": "input_image", "image_url": image_to_data_url(path)})
    return [{"role": "user", "content": content}]


def generate_one(
    card: dict[str, str | int],
    args: argparse.Namespace,
    prompt_pack: Path,
    out_dir: Path,
    parent_run: object | None = None,
    lesson_metadata: dict[str, object] | None = None,
    style_references: list[Path] | None = None,
) -> dict[str, object]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set.")

    client = build_openai_client(api_key, args.timeout)
    output_path = output_path_for_card(out_dir, card, args.output_format)
    metadata_path = out_dir / "metadata" / f"{int(card['number']):02d}.json"
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    if style_references is None:
        style_references = resolve_style_references(getattr(args, "style_reference", None))

    last_error = None
    for attempt in range(1, args.retries + 2):
        started_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            image_tool: dict[str, object] = {
                "type": "image_generation",
                "model": args.model,
                "size": args.size,
                "quality": args.quality,
                "output_format": args.output_format,
            }
            output_compression = getattr(args, "output_compression", None)
            if output_compression is not None:
                image_tool["output_compression"] = output_compression

            request_metadata = {
                **(lesson_metadata or {}),
                "request_type": "openai_image_generation",
                "card_number": card["number"],
                "card_title": card["title"],
                "model": args.image_agent_model,
                "image_model": args.model,
                "size": args.size,
                "quality": args.quality,
                "output_format": args.output_format,
                "output_compression": output_compression,
                "attempt": attempt,
                "style_reference_count": len(style_references),
                "style_references": [str(path.relative_to(ROOT)) for path in style_references],
            }
            request_tags = [
                "media-pipeline",
                "openai",
                "image-generation",
                "image-story",
                f"card:{int(card['number']):02d}",
            ]
            try:
                import langsmith as ls

                trace_context = ls.tracing_context(
                    parent=parent_run,
                    metadata=request_metadata,
                    tags=request_tags,
                )
            except ImportError:
                from contextlib import nullcontext

                trace_context = nullcontext()

            with trace_context:
                response = client.responses.create(
                    model=args.image_agent_model,
                    input=build_image_generation_input(str(card["prompt"]), style_references),
                    tools=[image_tool],
                    langsmith_extra={
                        "tags": request_tags,
                        "metadata": request_metadata,
                    },
                )
            openai_request_id = getattr(response, "_request_id", None)
            image_outputs = [
                output.result
                for output in response.output
                if getattr(output, "type", None) == "image_generation_call"
            ]
            image_base64 = image_outputs[0] if image_outputs else None
            if not image_base64:
                raise RuntimeError("OpenAI response did not include image_generation_call result.")
            output_path.write_bytes(base64.b64decode(image_base64))
            metadata = {
                "source_prompt_pack": str(prompt_pack.relative_to(ROOT)),
                "card_number": card["number"],
                "card_title": card["title"],
                "prompt": card["prompt"],
                "model": args.image_agent_model,
                "image_model": args.model,
                "size": args.size,
                "quality": args.quality,
                "output_format": args.output_format,
                "output_compression": output_compression,
                "request_timestamp": started_at,
                "output_path": str(output_path.relative_to(ROOT)),
                "api_response_id": getattr(response, "id", None),
                "openai_request_id": openai_request_id,
                "langsmith_parent_trace_id": trace_id(parent_run),
                "style_references": [str(path.relative_to(ROOT)) for path in style_references],
                "retry_count": attempt - 1,
            }
            metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
            return metadata
        except Exception as exc:
            last_error = exc
            if attempt <= args.retries:
                time.sleep(min(2 * attempt, 10))
                continue
            raise RuntimeError(f"Card {card['number']} failed: {last_error}") from exc

    raise RuntimeError(f"Card {card['number']} failed: {last_error}")


def build_single_request_prompt(cards: list[dict[str, str | int]], prompt_pack: Path) -> str:
    card_blocks = []
    for card in cards:
        card_blocks.append(
            "\n".join(
                [
                    f"FRAME {int(card['number']):02d}: {card['title']}",
                    str(card["prompt"]),
                ]
            )
        )
    return (
        "Create a complete image-only educational story as separate 9:16 image files.\n"
        f"Prompt pack: {prompt_pack.name}\n\n"
        "Important output contract:\n"
        f"- Generate exactly {len(cards)} separate images, one image per frame.\n"
        "- Do not make a collage, grid, contact sheet, storyboard page, or multi-panel poster.\n"
        "- Each frame must be a standalone vertical mobile story card.\n"
        "- Keep one consistent learner character, outfit, lighting, desk, and illustration style across all frames.\n"
        "- Keep text native inside the generated card: tablet UI, notebook panels, sticky notes, labels, arrows, and callouts.\n"
        "- Render quoted text verbatim where each frame asks for exact text.\n"
        "- No extra text, no logos, no watermark.\n\n"
        "Frames to generate:\n\n"
        + "\n\n---\n\n".join(card_blocks)
    )


def generate_lesson_single_request(
    cards: list[dict[str, str | int]],
    args: argparse.Namespace,
    prompt_pack: Path,
    out_dir: Path,
    parent_run: object | None = None,
    lesson_metadata: dict[str, object] | None = None,
    style_references: list[Path] | None = None,
) -> list[dict[str, object]]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set.")
    if style_references is None:
        style_references = resolve_style_references(getattr(args, "style_reference", None))

    client = build_openai_client(api_key, args.timeout)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "metadata").mkdir(parents=True, exist_ok=True)

    image_tool: dict[str, object] = {
        "type": "image_generation",
        "model": args.model,
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
    }
    output_compression = getattr(args, "output_compression", None)
    if output_compression is not None:
        image_tool["output_compression"] = output_compression

    request_metadata = {
        **(lesson_metadata or {}),
        "request_type": "openai_image_generation_single_request_lesson",
        "card_count_requested": len(cards),
        "model": args.image_agent_model,
        "image_model": args.model,
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
        "output_compression": output_compression,
        "style_reference_count": len(style_references),
        "style_references": [str(path.relative_to(ROOT)) for path in style_references],
    }
    request_tags = [
        "media-pipeline",
        "openai",
        "image-generation",
        "image-story",
        "single-request-lesson",
    ]
    try:
        import langsmith as ls

        trace_context = ls.tracing_context(
            parent=parent_run,
            metadata=request_metadata,
            tags=request_tags,
        )
    except ImportError:
        from contextlib import nullcontext

        trace_context = nullcontext()

    lesson_prompt = build_single_request_prompt(cards, prompt_pack)
    with trace_context:
        response = client.responses.create(
            model=args.image_agent_model,
            input=build_image_generation_input(lesson_prompt, style_references),
            tools=[image_tool],
            langsmith_extra={
                "tags": request_tags,
                "metadata": request_metadata,
            },
        )

    image_outputs = [
        output.result
        for output in response.output
        if getattr(output, "type", None) == "image_generation_call"
        and getattr(output, "result", None)
    ]
    if not image_outputs:
        raise RuntimeError("OpenAI single-request response did not include image_generation_call results.")

    results: list[dict[str, object]] = []
    for index, image_base64 in enumerate(image_outputs):
        card = cards[index] if index < len(cards) else None
        if card is None:
            output_path = out_dir / f"{index + 1:02d}-extra-single-request-output.{args.output_format}"
            metadata_path = out_dir / "metadata" / f"{index + 1:02d}-extra.json"
            metadata = {
                "source_prompt_pack": str(prompt_pack.relative_to(ROOT)),
                "card_number": index + 1,
                "card_title": "Extra single-request output",
            }
        else:
            output_path = output_path_for_card(out_dir, card, args.output_format)
            metadata_path = out_dir / "metadata" / f"{int(card['number']):02d}.json"
            metadata = {
                "source_prompt_pack": str(prompt_pack.relative_to(ROOT)),
                "card_number": card["number"],
                "card_title": card["title"],
                "prompt": card["prompt"],
            }
        output_path.write_bytes(base64.b64decode(image_base64))
        metadata.update(
            {
                "generation_mode": "single-request-lesson",
                "card_count_requested": len(cards),
                "image_outputs_received": len(image_outputs),
                "model": args.image_agent_model,
                "image_model": args.model,
                "size": args.size,
                "quality": args.quality,
                "output_format": args.output_format,
                "output_compression": output_compression,
                "api_response_id": getattr(response, "id", None),
                "openai_request_id": getattr(response, "_request_id", None),
                "langsmith_parent_trace_id": trace_id(parent_run),
                "style_references": [str(path.relative_to(ROOT)) for path in style_references],
                "output_path": str(output_path.relative_to(ROOT)),
            }
        )
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        results.append(metadata)

    return results


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate image-story cards with OpenAI.")
    parser.add_argument("--prompt-pack", required=True, help="Image-story prompt pack.")
    parser.add_argument("--out-dir", required=True, help="Output folder for generated cards.")
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_IMAGE_MODEL") or DEFAULT_IMAGE_MODEL,
        help="OpenAI image model.",
    )
    parser.add_argument(
        "--image-agent-model",
        default=os.environ.get("OPENAI_IMAGE_AGENT_MODEL") or DEFAULT_IMAGE_AGENT_MODEL,
        help="Responses model that invokes the image_generation tool.",
    )
    parser.add_argument("--size", default="1024x1536", help="Image size.")
    parser.add_argument("--quality", default="medium", help="Image quality.")
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
        default=int(os.environ.get("OPENAI_MAX_PARALLEL_IMAGES", DEFAULT_PARALLEL)),
        help="Concurrent image requests.",
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
        "--only-card",
        type=int,
        action="append",
        help="Generate only the specified card number. Can be repeated.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    load_dotenv()
    parser = build_arg_parser()
    args = parser.parse_args()
    try:
        prompt_pack = resolve_path(args.prompt_pack)
        out_dir = resolve_path(args.out_dir)
        if prompt_pack is None or out_dir is None:
            raise ValueError("--prompt-pack and --out-dir are required.")
        if args.output_compression is not None and args.output_format not in {"jpeg", "webp"}:
            raise ValueError("--output-compression is only valid with --output-format jpeg or webp.")
        cards = parse_prompt_pack(prompt_pack)
        if args.only_card:
            selected = set(args.only_card)
            cards = [card for card in cards if int(card["number"]) in selected]
            if not cards:
                raise ValueError(f"No matching cards found for --only-card {sorted(selected)}")
        lesson_slug = prompt_pack.stem.replace("-image-story", "")
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        lesson_metadata: dict[str, object] = {
            "lesson_slug": lesson_slug,
            "pipeline_run_id": run_id,
            "pipeline_stage": "image_story_generation",
            "request_group": "image_story_lesson",
            "prompt_pack": str(prompt_pack.relative_to(ROOT)),
            "out_dir": str(out_dir.relative_to(ROOT)),
            "model": args.model,
            "parallel": args.parallel,
        }
        lesson_tags = [
            "media-pipeline",
            "image-story",
            "openai",
            f"lesson:{lesson_slug}",
            "stage:image-generation",
        ]
        summary = {
            "prompt_pack": str(prompt_pack.relative_to(ROOT)),
            "out_dir": str(out_dir.relative_to(ROOT)),
            "lesson_slug": lesson_slug,
            "pipeline_run_id": run_id,
            "model": args.model,
            "image_agent_model": args.image_agent_model,
            "size": args.size,
            "quality": args.quality,
            "parallel": args.parallel,
            "cards": [
                {
                    "number": card["number"],
                    "title": card["title"],
                    "output_path": str(output_path_for_card(out_dir, card, args.output_format).relative_to(ROOT)),
                }
                for card in cards
            ],
        }
        if args.dry_run:
            print(json.dumps(summary, indent=2))
            return 0

        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set.")

        out_dir.mkdir(parents=True, exist_ok=True)
        results: list[dict[str, object]] = []
        with trace_run(
            "image-story lesson generation",
            run_type="chain",
            inputs=summary,
            metadata=lesson_metadata,
            tags=lesson_tags,
        ) as lesson_run:
            with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as executor:
                futures = [
                    executor.submit(
                        generate_one,
                        card,
                        args,
                        prompt_pack,
                        out_dir,
                        lesson_run,
                        lesson_metadata,
                        None,
                    )
                    for card in cards
                ]
                for future in as_completed(futures):
                    results.append(future.result())

            end_trace(
                lesson_run,
                {
                    "generated_count": len(results),
                    "out_dir": str(out_dir.relative_to(ROOT)),
                    "langsmith_trace_id": trace_id(lesson_run),
                },
            )

        run = {
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            **summary,
            "langsmith_trace_id": trace_id(lesson_run),
            "results": sorted(results, key=lambda item: int(item["card_number"])),
        }
        (out_dir / "generation-run.json").write_text(
            json.dumps(run, indent=2) + "\n",
            encoding="utf-8",
        )
        flush_traces()
        print(f"Generated {len(results)} image(s) in {out_dir}")
        return 0
    except Exception as exc:
        print(f"openai_image_story_generate failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
