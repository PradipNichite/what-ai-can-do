#!/usr/bin/env python3
"""Review lesson scene adequacy before image generation."""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

from openai_visual_models import SceneAdequacyVerdict
from pipeline_tracing import end_trace, flush_traces, trace_id, trace_run


ROOT = Path(__file__).resolve().parents[2]
PIPELINE_DIR = Path(__file__).resolve().parent
PROMPT_PATH = PIPELINE_DIR / "prompts" / "openai_scene_adequacy.md"
DEFAULT_MODEL = "gpt-5.5"
DEFAULT_TIMEOUT_SECONDS = 180


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


def resolve_path(raw: str | None) -> Path | None:
    if not raw:
        return None
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def rel_path(path: Path | None) -> str:
    if path is None:
        return ""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def read_text(path: Path | None, limit: int | None = None) -> str:
    if path is None:
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    if limit is not None and len(text) > limit:
        return text[:limit] + "\n\n[TRUNCATED FOR API CONTEXT]\n"
    return text


def build_openai_client(api_key: str, timeout: int):
    client = OpenAI(api_key=api_key, timeout=timeout)
    try:
        from langsmith.wrappers import wrap_openai
    except ImportError:
        return client
    return wrap_openai(client)


def rubric_context() -> str:
    files = [
        ROOT / "HOW_AI_USES_MATH_SERIES_GUIDE.md",
        ROOT / "HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md",
        ROOT / "IMAGE_STORY_GATE.md",
    ]
    sections = []
    for path in files:
        if path.exists():
            sections.append(f"## {path.name}\n{read_text(path, limit=14000)}")
    return "\n\n".join(sections)


def build_context(args: argparse.Namespace) -> str:
    source_module = resolve_path(args.source_module)
    prompt_pack = resolve_path(args.prompt_pack)
    video_prompt_pack = resolve_path(args.video_prompt_pack)
    return textwrap.dedent(
        f"""
        {read_text(PROMPT_PATH)}

        Topic: {args.topic or ''}
        Renderer target: {args.renderer}

        Source module path: {rel_path(source_module)}
        Source module:
        {read_text(source_module, limit=26000)}

        Image prompt pack path: {rel_path(prompt_pack)}
        Image prompt pack:
        {read_text(prompt_pack, limit=22000)}

        Video prompt pack path: {rel_path(video_prompt_pack)}
        Video prompt pack:
        {read_text(video_prompt_pack, limit=18000)}

        Project rubrics:
        {rubric_context()}
        """
    ).strip()


def enforce_scene_status(verdict: dict[str, Any]) -> dict[str, Any]:
    blocking_gate = (
        verdict.get("mechanism_chain", {}).get("status") == "fail"
        or verdict.get("technical_completeness", {}).get("status") == "fail"
        or verdict.get("false_completion_risk", {}).get("status") == "high"
    )
    caveated = verdict.get("status") == "pass-with-caveats"
    if not blocking_gate and not caveated:
        return verdict

    verdict = dict(verdict)
    verdict["status"] = "needs-revision"
    if verdict.get("next_action") == "proceed-to-prompts":
        verdict["next_action"] = "revise-scene-flow"
    reasons = []
    if caveated:
        reasons.append("pass-with-caveats is a false pass and must be repaired")
    if blocking_gate:
        reasons.append(
            "failed mechanism/technical chain or high false-completion risk cannot proceed to image prompts"
        )
    verdict["verdict"] = (verdict.get("verdict", "") + " Scene adequacy override: " + "; ".join(reasons) + ".").strip()
    return verdict


def run_scene_adequacy(args: argparse.Namespace, api_key: str):
    client = build_openai_client(api_key, args.timeout)
    request_metadata = {
        "request_type": "openai_scene_adequacy",
        "lesson_topic": args.topic or "",
        "renderer": args.renderer,
        "source_module": args.source_module,
        "prompt_pack": args.prompt_pack or "",
        "video_prompt_pack": args.video_prompt_pack or "",
        "model": args.model,
    }
    request_tags = [
        "media-pipeline",
        "openai",
        "scene-adequacy",
        args.renderer,
    ]
    response = client.responses.parse(
        model=args.model,
        input=[{"role": "user", "content": build_context(args)}],
        text_format=SceneAdequacyVerdict,
        langsmith_extra={
            "tags": request_tags,
            "metadata": request_metadata,
        },
    )
    return response, getattr(response, "_request_id", None)


def markdown_from_verdict(
    verdict: dict[str, Any],
    args: argparse.Namespace,
    response_id: str,
    openai_request_id: str | None,
    trace: str | None,
) -> str:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        f"# OpenAI Scene Adequacy - {args.renderer}",
        "",
        f"Generated: {generated_at}",
        f"Model: `{args.model}`",
        f"Response ID: `{response_id}`",
        f"OpenAI request ID: `{openai_request_id or ''}`",
        f"LangSmith trace ID: `{trace or ''}`",
        "",
        "## Inputs",
        "",
        f"- Topic: `{args.topic or ''}`",
        f"- Source module: `{args.source_module}`",
        f"- Image prompt pack: `{args.prompt_pack or ''}`",
        f"- Video prompt pack: `{args.video_prompt_pack or ''}`",
        "",
        "## Verdict",
        "",
        f"- Status: `{verdict['status']}`",
        f"- Next action: `{verdict['next_action']}`",
        "",
        verdict["verdict"],
        "",
        "## Gates",
        "",
    ]
    for key, label in [
        ("scene_count", "Scene count"),
        ("mechanism_chain", "Mechanism chain"),
        ("technical_completeness", "Technical completeness"),
        ("opener_readiness", "Opener readiness"),
        ("renderer_readiness", "Renderer readiness"),
    ]:
        gate = verdict[key]
        lines.extend(
            [
                f"- {label}: `{gate['status']}` - {gate['evidence']}",
                f"- {label} required fix: {gate['required_fix']}",
            ]
        )
    risk = verdict["false_completion_risk"]
    lines.extend(
        [
            f"- False-completion risk: `{risk['status']}` - {risk['evidence']}",
            f"- False-completion required fix: {risk['required_fix']}",
            "",
            "## Scene Notes",
            "",
        ]
    )
    for note in verdict.get("scene_notes", []):
        lines.extend(
            [
                f"### Scene {note['scene']}: {note['title']}",
                "",
                f"- Status: `{note['status']}`",
                f"- Learning job: {note['learning_job']}",
                f"- Visible evidence: {note['visible_evidence']}",
                f"- Transformation/comparison: {note['transformation_or_comparison']}",
                f"- Misconception risk: {note['misconception_risk']}",
                f"- Required fix: {note['required_fix']}",
                "",
            ]
        )
    lines.extend(["## Missing Scenes", ""])
    if verdict.get("missing_scenes"):
        for missing in verdict["missing_scenes"]:
            lines.extend(
                [
                    f"### Insert after scene {missing['insert_after_scene']}: {missing['title']}",
                    "",
                    f"- Learning job: {missing['learning_job']}",
                    f"- Why needed: {missing['why_needed']}",
                    f"- Must show: {missing['must_show']}",
                    "",
                ]
            )
    else:
        lines.append("None.")
        lines.append("")
    lines.extend(["## Recommended Scene Flow", ""])
    lines.extend(f"{index}. {scene}" for index, scene in enumerate(verdict["recommended_scene_flow"], start=1))
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(
    verdict: dict[str, Any],
    response_id: str,
    args: argparse.Namespace,
    openai_request_id: str | None,
    trace: str | None,
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
        "renderer": args.renderer,
        "response_id": response_id,
        "openai_request_id": openai_request_id,
        "langsmith_trace_id": trace,
        "inputs": {
            "topic": args.topic,
            "source_module": args.source_module,
            "prompt_pack": args.prompt_pack,
            "video_prompt_pack": args.video_prompt_pack,
        },
        "verdict": verdict,
    }
    json_out.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    md_out.write_text(
        markdown_from_verdict(verdict, args, response_id, openai_request_id, trace),
        encoding="utf-8",
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Use OpenAI structured output to review lesson scene adequacy before image generation."
    )
    parser.add_argument("--source-module", required=True, help="Lesson source module.")
    parser.add_argument("--prompt-pack", help="Image-story prompt pack.")
    parser.add_argument("--video-prompt-pack", help="Video-first prompt pack.")
    parser.add_argument("--topic", help="Human-readable lesson topic.")
    parser.add_argument(
        "--renderer",
        default="image-story",
        choices=["image-story", "video-first", "paired", "renderer-agnostic"],
    )
    parser.add_argument("--out", required=True, help="Markdown output path.")
    parser.add_argument("--json-out", required=True, help="JSON output path.")
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_SCENE_QA_MODEL")
        or os.environ.get("OPENAI_VISION_QA_MODEL")
        or os.environ.get("OPENAI_MODEL")
        or DEFAULT_MODEL,
        help="OpenAI model for scene adequacy review.",
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
    return parser


def main() -> int:
    load_dotenv()
    parser = build_arg_parser()
    args = parser.parse_args()

    try:
        source_module = resolve_path(args.source_module)
        if source_module is None or not source_module.exists():
            raise FileNotFoundError(f"Source module not found: {args.source_module}")
        for raw in [args.prompt_pack, args.video_prompt_pack]:
            path = resolve_path(raw)
            if raw and (path is None or not path.exists()):
                raise FileNotFoundError(f"Context file not found: {raw}")

        context = build_context(args)
        if args.dry_run:
            summary = {
                "model": args.model,
                "renderer": args.renderer,
                "structured_output": "Pydantic SceneAdequacyVerdict via client.responses.parse",
                "schema_properties": list(
                    SceneAdequacyVerdict.model_json_schema()["properties"].keys()
                ),
                "input_text_characters": len(context),
                "json_out": args.json_out,
                "out": args.out,
            }
            print(json.dumps(summary, indent=2))
            return 0

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set.")

        metadata = {
            "request_type": "scene_adequacy_pipeline",
            "lesson_topic": args.topic or "",
            "renderer": args.renderer,
            "source_module": args.source_module,
        }
        start = time.time()
        with trace_run(
            "lesson scene adequacy",
            inputs={
                "source_module": args.source_module,
                "prompt_pack": args.prompt_pack,
                "video_prompt_pack": args.video_prompt_pack,
            },
            metadata=metadata,
            tags=["media-pipeline", "scene-adequacy", args.renderer],
        ) as run:
            response, openai_request_id = run_scene_adequacy(args, api_key)
            if response.output_parsed is None:
                raise RuntimeError("OpenAI response did not include parsed structured output.")
            verdict = enforce_scene_status(response.output_parsed.model_dump())
            response_id = str(getattr(response, "id", ""))
            write_outputs(verdict, response_id, args, openai_request_id, trace_id(run))
            end_trace(
                run,
                {
                    "status": verdict["status"],
                    "next_action": verdict["next_action"],
                    "out": args.out,
                    "json_out": args.json_out,
                    "openai_request_id": openai_request_id,
                },
            )
        flush_traces()

        elapsed = time.time() - start
        print(
            f"OpenAI scene adequacy wrote {args.json_out} and {args.out} "
            f"in {elapsed:.1f}s."
        )
        if openai_request_id:
            print(f"OpenAI request ID: {openai_request_id}")
        print(f"Status: {verdict['status']} | Next action: {verdict['next_action']}")
        return 0
    except Exception as exc:
        print(f"openai_scene_adequacy failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
