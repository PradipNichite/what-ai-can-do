#!/usr/bin/env python3
"""Generate paired image-only and video-first frames in one OpenAI request."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from build_contact_sheet import build_contact_sheet, collect_images
from openai_image_story_generate import image_to_data_url, output_path_for_card, parse_prompt_pack, resolve_style_references, slugify
from openai_visual_qa import build_openai_client, load_dotenv, resolve_path
from pipeline_tracing import end_trace, flush_traces, trace_id, trace_run


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IMAGE_MODEL = "gpt-image-2"
DEFAULT_IMAGE_AGENT_MODEL = "gpt-5.5"


def rel_path(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def parse_video_prompt_pack(path: Path) -> list[dict[str, str | int]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    heading = r"^#{2,3}\s+Frame\s+\d+\s*[-:]"
    pattern = re.compile(
        r"^#{2,3}\s+Frame\s+(\d+)\s*[-:]\s*(.+?)\s*$"
        rf"(.*?)(?={heading}|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    frames: list[dict[str, str | int]] = []
    for match in pattern.finditer(text):
        number = int(match.group(1))
        title = match.group(2).strip()
        body = match.group(3)
        code_blocks = re.findall(r"```(?:text)?\s*(.*?)```", body, re.IGNORECASE | re.DOTALL)
        if not code_blocks:
            continue
        frames.append({"number": number, "title": title, "prompt": code_blocks[0].strip()})
    if not frames:
        raise ValueError(f"No video-first frame prompts found in {path}")
    return sorted(frames, key=lambda item: int(item["number"]))


def build_pair_prompt(image_card: dict[str, str | int], video_frame: dict[str, str | int]) -> str:
    number = int(image_card["number"])
    return (
        f"Create two separate 9:16 images for lesson frame {number:02d}.\n\n"
        "This is not a request for two variations of the same poster. It is a request for two "
        "different renderer deliverables that share the same lesson moment, character, and style.\n\n"
        "Output contract:\n"
        "- Return exactly two separate image outputs.\n"
        "- Output 1 is IMAGE_ONLY_STORY_CARD.\n"
        "- Output 2 is VIDEO_SOURCE_FRAME.\n"
        "- Do not make a collage, grid, comparison sheet, or two-panel image.\n"
        "- Keep the same learner character, outfit, desk, lighting, and visual style in both outputs.\n"
        "- No logos, no watermark, no extra unrelated text.\n\n"
        "Output 1 requirements, IMAGE_ONLY_STORY_CARD:\n"
        "- Must be self-contained when paused, like a native educational story card.\n"
        "- Must preserve the image-only prompt's explanatory structure, headline/callout intent, and exact requested text.\n"
        "- Must include enough integrated text for a viewer to understand the idea without voiceover.\n"
        "- Text should live inside the scene through tablet UI, notebook panels, sticky notes, arrows, labels, callouts, or mini-cards.\n"
        "- Do not simplify this output just because Output 2 is low-text.\n\n"
        "Output 2 requirements, VIDEO_SOURCE_FRAME:\n"
        "- Must be a clean image-to-video source frame, not a poster card.\n"
        "- Must use less embedded explanation than Output 1.\n"
        "- Must have one clear motion target from the video prompt.\n"
        "- Must preserve only the sparse technical text/numbers needed for animation.\n"
        "- Let voiceover carry explanations; do not copy Output 1's full headline/callout text.\n\n"
        "Shared technical requirement:\n"
        "- Preserve the technical numbers, labels, formulas, and named concepts requested in each prompt.\n\n"
        "IMAGE_ONLY_STORY_CARD prompt:\n"
        f"{image_card['prompt']}\n\n"
        "VIDEO_SOURCE_FRAME prompt:\n"
        f"{video_frame['prompt']}\n"
    )


def build_input(prompt: str, references: list[Path]) -> str | list[dict[str, object]]:
    if not references:
        return prompt
    content: list[dict[str, object]] = [
        {
            "type": "input_text",
            "text": (
                "Use the attached references for style, character continuity, warm study-desk "
                "composition, and native educational design. Do not copy their topic unless it "
                "matches the prompt.\n\n"
                + prompt
            ),
        }
    ]
    for path in references:
        content.append({"type": "input_image", "image_url": image_to_data_url(path)})
    return [{"role": "user", "content": content}]


def output_pair_paths(out_dir: Path, card: dict[str, str | int], output_format: str) -> tuple[Path, Path]:
    number = int(card["number"])
    title = slugify(str(card["title"]))
    return (
        out_dir / "image-only" / f"{number:02d}-{title}.{output_format}",
        out_dir / "video-first" / f"{number:02d}-{title}-video.{output_format}",
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run paired image-only/video-first generation experiments.")
    parser.add_argument("--image-prompt-pack", required=True)
    parser.add_argument("--video-prompt-pack", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--image-model", default=os.environ.get("OPENAI_IMAGE_MODEL") or DEFAULT_IMAGE_MODEL)
    parser.add_argument("--image-agent-model", default=os.environ.get("OPENAI_IMAGE_AGENT_MODEL") or DEFAULT_IMAGE_AGENT_MODEL)
    parser.add_argument("--size", default="1024x1536")
    parser.add_argument("--quality", default="medium")
    parser.add_argument("--output-format", default="png", choices=["png", "jpeg", "webp"])
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("OPENAI_REQUEST_TIMEOUT_SECONDS", 180)))
    parser.add_argument("--only-frame", type=int, action="append", help="Frame number to generate. Can be repeated.")
    parser.add_argument("--style-reference", action="append")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    load_dotenv()
    parser = build_arg_parser()
    args = parser.parse_args()
    try:
        image_pack = resolve_path(args.image_prompt_pack)
        video_pack = resolve_path(args.video_prompt_pack)
        out_dir = resolve_path(args.out_dir)
        if image_pack is None or video_pack is None or out_dir is None:
            raise ValueError("--image-prompt-pack, --video-prompt-pack, and --out-dir are required.")

        image_cards = {int(card["number"]): card for card in parse_prompt_pack(image_pack)}
        video_frames = {int(frame["number"]): frame for frame in parse_video_prompt_pack(video_pack)}
        selected = sorted(set(args.only_frame or image_cards.keys()) & set(video_frames.keys()))
        if not selected:
            raise ValueError("No matching frame numbers found between image and video prompt packs.")
        references = resolve_style_references(args.style_reference)
        summary = {
            "image_prompt_pack": rel_path(image_pack),
            "video_prompt_pack": rel_path(video_pack),
            "out_dir": rel_path(out_dir),
            "frames": selected,
            "image_model": args.image_model,
            "image_agent_model": args.image_agent_model,
            "quality": args.quality,
            "size": args.size,
            "style_references": [rel_path(path) for path in references],
        }
        if args.dry_run:
            print(json.dumps(summary, indent=2))
            return 0
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set.")

        client = build_openai_client(os.environ["OPENAI_API_KEY"], args.timeout)
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "metadata").mkdir(parents=True, exist_ok=True)
        results: list[dict[str, object]] = []
        with trace_run(
            "dual-format image/video experiment",
            run_type="chain",
            inputs=summary,
            metadata={
                "request_type": "dual_format_experiment",
                "image_prompt_pack": rel_path(image_pack),
                "video_prompt_pack": rel_path(video_pack),
                "out_dir": rel_path(out_dir),
            },
            tags=["media-pipeline", "openai", "dual-format-experiment"],
        ) as run:
            for number in selected:
                image_card = image_cards[number]
                video_frame = video_frames[number]
                prompt = build_pair_prompt(image_card, video_frame)
                metadata = {
                    "request_type": "openai_dual_format_image_generation",
                    "frame_number": number,
                    "image_title": image_card["title"],
                    "video_title": video_frame["title"],
                    "image_model": args.image_model,
                    "quality": args.quality,
                    "size": args.size,
                }
                response = client.responses.create(
                    model=args.image_agent_model,
                    input=build_input(prompt, references),
                    tools=[
                        {
                            "type": "image_generation",
                            "model": args.image_model,
                            "size": args.size,
                            "quality": args.quality,
                            "output_format": args.output_format,
                        }
                    ],
                    langsmith_extra={
                        "tags": ["media-pipeline", "openai", "dual-format-experiment", f"frame:{number:02d}"],
                        "metadata": metadata,
                    },
                )
                image_outputs = [
                    output.result
                    for output in response.output
                    if getattr(output, "type", None) == "image_generation_call"
                    and getattr(output, "result", None)
                ]
                image_path, video_path = output_pair_paths(out_dir, image_card, args.output_format)
                image_path.parent.mkdir(parents=True, exist_ok=True)
                video_path.parent.mkdir(parents=True, exist_ok=True)
                output_paths = [image_path, video_path]
                written_paths = []
                for index, image_base64 in enumerate(image_outputs[:2]):
                    output_paths[index].write_bytes(base64.b64decode(image_base64))
                    written_paths.append(output_paths[index])
                item = {
                    **metadata,
                    "api_response_id": getattr(response, "id", None),
                    "openai_request_id": getattr(response, "_request_id", None),
                    "outputs_requested": 2,
                    "outputs_received": len(image_outputs),
                    "written_paths": [rel_path(path) for path in written_paths],
                }
                (out_dir / "metadata" / f"{number:02d}.json").write_text(
                    json.dumps(item, indent=2) + "\n",
                    encoding="utf-8",
                )
                results.append(item)

            image_sheet = out_dir / "image-only-contact-sheet.jpg"
            video_sheet = out_dir / "video-first-contact-sheet.jpg"
            build_contact_sheet(collect_images(out_dir / "image-only"), image_sheet, 2, 360, 32)
            build_contact_sheet(collect_images(out_dir / "video-first"), video_sheet, 2, 360, 32)
            status = {
                **summary,
                "langsmith_trace_id": trace_id(run),
                "results": results,
                "image_contact_sheet": rel_path(image_sheet),
                "video_contact_sheet": rel_path(video_sheet),
            }
            (out_dir / "experiment-status.json").write_text(
                json.dumps(status, indent=2) + "\n",
                encoding="utf-8",
            )
            end_trace(run, status)

        flush_traces()
        print(json.dumps(status, indent=2))
        return 0
    except Exception as exc:
        print(f"openai_dual_format_experiment failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
