#!/usr/bin/env python3
"""Run OpenAI vision QA on generated visual assets.

This tool intentionally makes the API call against actual image files. Prompt
text and local metadata can provide context, but they cannot produce the final
visual QA verdict for this project.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import textwrap
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

from openai_visual_models import VisualQAVerdict


ROOT = Path(__file__).resolve().parents[2]
PIPELINE_DIR = Path(__file__).resolve().parent
PROMPT_PATH = PIPELINE_DIR / "prompts" / "openai_visual_qa.md"
DEFAULT_MODEL = "gpt-5.5"
DEFAULT_TIMEOUT_SECONDS = 180
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def read_text(path: Path | None, limit: int | None = None) -> str:
    if path is None:
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    if limit is not None and len(text) > limit:
        return text[:limit] + "\n\n[TRUNCATED FOR API CONTEXT]\n"
    return text


def rel_path(path: Path | None) -> str:
    if path is None:
        return ""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def resolve_path(raw: str | None) -> Path | None:
    if not raw:
        return None
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def load_dotenv() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def collect_images(
    image_folder: Path | None,
    contact_sheet: Path | None,
    include_folder_images: bool,
) -> list[Path]:
    images: list[Path] = []
    if contact_sheet is not None:
        if not contact_sheet.exists():
            raise FileNotFoundError(f"Contact sheet not found: {contact_sheet}")
        images.append(contact_sheet)

    should_collect_folder = image_folder is not None and (
        include_folder_images or contact_sheet is None
    )
    if should_collect_folder:
        if not image_folder.exists():
            raise FileNotFoundError(f"Image folder not found: {image_folder}")
        folder_images = sorted(
            path
            for path in image_folder.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        )
        for path in folder_images:
            if contact_sheet is not None and path.resolve() == contact_sheet.resolve():
                continue
            images.append(path)

    if not images:
        raise ValueError("Provide --contact-sheet, --image-folder, or both with image files.")
    return images


def image_to_data_url(path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(path.name)
    if mime_type is None:
        mime_type = "image/png"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{data}"


def rubric_files_for_mode(mode: str) -> list[Path]:
    files = [ROOT / "VISUAL_QA_CHECKLIST.md"]
    if mode == "image-story":
        files.extend(
            [
                ROOT / "IMAGE_STORY_GATE.md",
                ROOT / "HOW_AI_USES_MATH_SERIES_GUIDE.md",
            ]
        )
    elif mode == "video-first":
        files.extend(
            [
                ROOT / "VIDEO_FIRST_VISUAL_GUIDE.md",
                ROOT / "HOW_AI_USES_MATH_SERIES_GUIDE.md",
            ]
        )
    elif mode == "skill-base":
        files.extend(
            [
                ROOT / "SKILL_BASE_EXAMPLE_VALIDATION.md",
                ROOT / "IMAGE_STORY_GATE.md",
                ROOT / "VIDEO_FIRST_VISUAL_GUIDE.md",
            ]
        )
    elif mode == "style-reference":
        files.extend([ROOT / "VIDEO_FIRST_VISUAL_GUIDE.md"])
    return files


def build_context(args: argparse.Namespace, images: list[Path]) -> str:
    prompt_pack = resolve_path(args.prompt_pack)
    source_module = resolve_path(args.source_module)
    rubric_sections = []
    for path in rubric_files_for_mode(args.mode):
        if path.exists():
            rubric_sections.append(f"## {path.name}\n{read_text(path, limit=12000)}")

    image_list = "\n".join(
        f"{index}. {rel_path(path)}" for index, path in enumerate(images, start=1)
    )
    return textwrap.dedent(
        f"""
        {read_text(PROMPT_PATH)}

        Mode: {args.mode}
        Intended use: {args.mode}
        Image files, in review order:
        {image_list}

        Prompt pack path: {rel_path(prompt_pack)}
        Prompt pack context:
        {read_text(prompt_pack, limit=18000)}

        Source module path: {rel_path(source_module)}
        Source module context:
        {read_text(source_module, limit=12000)}

        Rubrics:
        {"\n\n".join(rubric_sections)}
        """
    ).strip()


def build_content(args: argparse.Namespace, images: list[Path]) -> list[dict[str, str]]:
    content: list[dict[str, str]] = [
        {"type": "input_text", "text": build_context(args, images)}
    ]
    content.extend(
        {
            "type": "input_image",
            "image_url": image_to_data_url(path),
        }
        for path in images
    )
    return content


def build_openai_client(api_key: str, timeout: int):
    client = OpenAI(api_key=api_key, timeout=timeout)
    try:
        from langsmith.wrappers import wrap_openai
    except ImportError:
        return client
    return wrap_openai(client)


def run_visual_qa(
    args: argparse.Namespace,
    images: list[Path],
    api_key: str,
    parent_run: object | None = None,
    lesson_metadata: dict[str, object] | None = None,
):
    client = build_openai_client(api_key, args.timeout)
    content = build_content(args, images)
    request_metadata = {
        **(lesson_metadata or {}),
        "request_type": "openai_visual_qa",
        "model": args.model,
        "mode": args.mode,
        "image_count": len(images),
    }
    request_tags = [
        "media-pipeline",
        "openai",
        "visual-qa",
        args.mode,
    ]
    response = client.responses.parse(
        model=args.model,
        input=[{"role": "user", "content": content}],
        text_format=VisualQAVerdict,
        langsmith_extra={
            "tags": request_tags,
            "metadata": request_metadata,
        },
    )
    return response, getattr(response, "_request_id", None)


def markdown_from_verdict(
    verdict: dict[str, Any],
    args: argparse.Namespace,
    images: list[Path],
    response_id: str,
    openai_request_id: str | None = None,
) -> str:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        f"# OpenAI Visual QA - {args.mode}",
        "",
        f"Generated: {generated_at}",
        f"Model: `{args.model}`",
        f"Response ID: `{response_id}`",
        f"OpenAI request ID: `{openai_request_id or ''}`",
        "",
        "## Inputs",
        "",
        f"- Image folder: `{args.image_folder or ''}`",
        f"- Contact sheet: `{args.contact_sheet or ''}`",
        f"- Prompt pack: `{args.prompt_pack or ''}`",
        f"- Source module: `{args.source_module or ''}`",
        "",
        "Reviewed images:",
    ]
    lines.extend(f"- `{rel_path(path)}`" for path in images)
    lines.extend(
        [
            "",
            "## Verdict",
            "",
            f"- Status: `{verdict['status']}`",
            f"- Intended use: `{verdict['intended_use']}`",
            f"- Next action: `{verdict['next_action']}`",
            "",
            verdict["verdict"],
            "",
            "## Gate Evidence",
            "",
            f"- Opener: `{verdict['opener']['status']}` - {verdict['opener']['evidence']}",
            f"- Opener required fix: {verdict['opener']['required_fix']}",
            f"- Native composition: `{verdict['native_composition']['status']}` - {verdict['native_composition']['evidence']}",
            f"- Native composition required fix: {verdict['native_composition']['required_fix']}",
            f"- Overlay risk: `{verdict['overlay_risk']['status']}` - {verdict['overlay_risk']['evidence']}",
            f"- Mechanism visibility: `{verdict['mechanism_visibility']['status']}` - {verdict['mechanism_visibility']['evidence']}",
            f"- Mechanism required fix: {verdict['mechanism_visibility']['required_fix']}",
            f"- Technical understanding: `{verdict['technical_understanding']['status']}` - {verdict['technical_understanding']['evidence']}",
            f"- Technical understanding required fix: {verdict['technical_understanding']['required_fix']}",
            f"- False-completion risk: `{verdict['false_completion_risk']['status']}` - {verdict['false_completion_risk']['evidence']}",
            f"- False-completion required fix: {verdict['false_completion_risk']['required_fix']}",
            f"- Mobile readability: `{verdict['mobile_readability']['status']}` - {verdict['mobile_readability']['evidence']}",
            f"- Mobile readability required fix: {verdict['mobile_readability']['required_fix']}",
            "",
            "## Frame Notes",
            "",
        ]
    )
    for note in verdict.get("frame_notes", []):
        lines.extend(
            [
                f"### Frame {note['frame']}",
                "",
                f"- Status: `{note['status']}`",
                f"- Evidence: {note['evidence']}",
                f"- Fix: {note['fix']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def enforce_strict_status(verdict: dict[str, Any]) -> dict[str, Any]:
    """Prevent polished-but-shallow visuals from being accepted."""

    blocking_gate = (
        verdict.get("technical_understanding", {}).get("status") == "fail"
        or verdict.get("false_completion_risk", {}).get("status") == "high"
    )
    if not blocking_gate:
        return verdict

    verdict = dict(verdict)
    verdict["status"] = "needs-revision"
    verdict["next_action"] = "regenerate-frame"
    verdict["verdict"] = (
        verdict.get("verdict", "")
        + " Strict QA override: high false-completion risk or failed technical "
        "understanding cannot be accepted."
    ).strip()
    return verdict


def write_outputs(
    verdict: dict[str, Any],
    response_id: str,
    args: argparse.Namespace,
    images: list[Path],
    openai_request_id: str | None = None,
) -> None:
    json_out = resolve_path(args.json_out)
    md_out = resolve_path(args.out)
    if json_out is None:
        raise ValueError("--json-out is required")
    if md_out is None:
        raise ValueError("--out is required")

    json_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.parent.mkdir(parents=True, exist_ok=True)

    envelope = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "model": args.model,
        "mode": args.mode,
        "response_id": response_id,
        "openai_request_id": openai_request_id,
        "inputs": {
            "image_folder": args.image_folder,
            "contact_sheet": args.contact_sheet,
            "prompt_pack": args.prompt_pack,
            "source_module": args.source_module,
            "images": [rel_path(path) for path in images],
        },
        "verdict": verdict,
    }
    json_out.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    md_out.write_text(
        markdown_from_verdict(verdict, args, images, response_id, openai_request_id),
        encoding="utf-8",
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Use OpenAI vision to review generated visual assets."
    )
    parser.add_argument("--image-folder", help="Folder containing generated images.")
    parser.add_argument("--contact-sheet", help="Contact sheet image to review first.")
    parser.add_argument("--prompt-pack", help="Prompt pack Markdown for context.")
    parser.add_argument("--source-module", help="Source module Markdown for context.")
    parser.add_argument(
        "--mode",
        required=True,
        choices=["image-story", "video-first", "style-reference", "skill-base"],
    )
    parser.add_argument("--out", required=True, help="Markdown QA output path.")
    parser.add_argument("--json-out", required=True, help="JSON QA output path.")
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_VISION_QA_MODEL")
        or os.environ.get("OPENAI_MODEL")
        or DEFAULT_MODEL,
        help="OpenAI model for visual QA.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(
            os.environ.get("OPENAI_REQUEST_TIMEOUT_SECONDS", DEFAULT_TIMEOUT_SECONDS)
        ),
        help="Request timeout in seconds.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print payload summary without calling OpenAI.",
    )
    parser.add_argument(
        "--include-folder-images",
        action="store_true",
        help="Attach individual folder images in addition to the contact sheet.",
    )
    return parser


def main() -> int:
    load_dotenv()
    parser = build_arg_parser()
    args = parser.parse_args()

    try:
        image_folder = resolve_path(args.image_folder)
        contact_sheet = resolve_path(args.contact_sheet)
        images = collect_images(image_folder, contact_sheet, args.include_folder_images)
        content = build_content(args, images)

        if args.dry_run:
            summary = {
                "model": args.model,
                "mode": args.mode,
                "image_count": len(images),
                "images": [rel_path(path) for path in images],
                "structured_output": "Pydantic VisualQAVerdict via client.responses.parse",
                "schema_properties": list(
                    VisualQAVerdict.model_json_schema()["properties"].keys()
                ),
                "input_text_characters": len(content[0]["text"]),
                "json_out": args.json_out,
                "out": args.out,
            }
            print(json.dumps(summary, indent=2))
            return 0

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set.")

        start = time.time()
        response, openai_request_id = run_visual_qa(args, images, api_key)
        if response.output_parsed is None:
            raise RuntimeError("OpenAI response did not include parsed structured output.")
        verdict = enforce_strict_status(response.output_parsed.model_dump())
        response_id = str(getattr(response, "id", ""))
        write_outputs(verdict, response_id, args, images, openai_request_id)
        elapsed = time.time() - start
        print(
            f"OpenAI visual QA wrote {args.json_out} and {args.out} "
            f"in {elapsed:.1f}s."
        )
        if openai_request_id:
            print(f"OpenAI request ID: {openai_request_id}")
        print(f"Status: {verdict['status']} | Next action: {verdict['next_action']}")
        return 0
    except Exception as exc:
        print(f"openai_visual_qa failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
