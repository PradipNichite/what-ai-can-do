#!/usr/bin/env python3
"""Static guardrail for How AI Uses Math video style and QA claims."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]

STYLE_TERMS = (
    "style_reference_contact_sheet",
    "style reference contact sheet",
    "style/reference contact sheet",
    "accepted source-frame qa",
    "accepted style reference",
    "native story gold candidate",
    "native-story gold candidate",
    "native educational story",
    "gold candidate",
)
PROGRAMMATIC_TERMS = (
    "programmatic",
    "animation_backend",
    "motion-canvas",
    "revideo",
    "remotion",
    "manim",
    "pillow",
)
REJECT_TERMS = ("status: reject", "status: rejected", "failure calibration", "rejected")
PASS_STATUSES = ("status: pass",)
CAVEAT_STATUSES = ("status: pass-with-caveats",)
LESSON_GATE_TERMS = (
    "minimum lesson gate",
    "school concept",
    "ai use",
    "concrete example",
    "mechanism chain",
    "memory anchor",
    "quick check",
)
VIDEO_PATH_PARTS = (
    "outputs/video-manifests/",
    "outputs/video-scripts/",
    "outputs/video-renders/verification/",
)


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def lower_text(path: Path) -> str:
    return read_text(path).lower()


def changed_files() -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    if result.stdout.strip():
        return [ROOT / line.strip() for line in result.stdout.splitlines() if line.strip()]

    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    paths: list[Path] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        raw = line[3:]
        if " -> " in raw:
            raw = raw.split(" -> ", 1)[1]
        path = ROOT / raw
        if path.exists() and path.is_file():
            paths.append(path)
    return paths


def candidate_files(paths: list[Path]) -> list[Path]:
    selected: list[Path] = []
    for path in paths:
        name = rel(path)
        if any(
            token in path.name
            for token in (
                "uploaded-url",
                "uploaded-urls",
                "uploaded-source-urls",
                "uploaded-clip-urls",
                "fresh-video-urls",
            )
        ):
            continue
        if any(part in name for part in VIDEO_PATH_PARTS) and path.suffix.lower() in {".md", ".json"}:
            selected.append(path)
    return selected


def paired_visual_qa(path: Path) -> Path | None:
    stem = path.stem
    if stem.endswith(".en") or stem.endswith(".mr"):
        stem = Path(stem).stem
    candidates = [
        ROOT / "outputs" / "video-renders" / "verification" / f"{stem}.visual-qa.md",
        ROOT / "outputs" / "video-renders" / "verification" / f"{stem.replace('.en', '').replace('.mr', '')}.visual-qa.md",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def json_value(path: Path) -> dict[str, Any] | None:
    if path.suffix.lower() != ".json":
        return None
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError:
        return None


def is_programmatic_candidate(path: Path, text: str, data: dict[str, Any] | None) -> bool:
    if any(term in text for term in PROGRAMMATIC_TERMS):
        return True
    if data:
        values = json.dumps(data, ensure_ascii=False).lower()
        return any(term in values for term in PROGRAMMATIC_TERMS)
    return False


def is_rejected(text: str) -> bool:
    return any(term in text for term in REJECT_TERMS)


def is_source_draft(text: str) -> bool:
    return any(
        term in text
        for term in (
            "status: `source-draft`",
            "status: source-draft",
            "not a rendered candidate yet",
            "lesson-design blueprint",
        )
    )


def has_style_reference(text: str) -> bool:
    return any(term in text for term in STYLE_TERMS)


def has_style_preserving_animation_role(text: str) -> bool:
    return any(
        term in text
        for term in (
            "animation_policy",
            "style-preserving",
            "style preserving",
            "small technical enhancement",
            "small technical insert",
            "subtle motion",
            "image-to-video",
            "runway",
            "creatomate",
        )
    )


def status_line(text: str) -> str | None:
    for line in text.splitlines():
        if line.strip().lower().startswith("status:"):
            return line.strip().lower()
    return None


def check_visual_qa(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    status = status_line(text)
    if any(text.startswith(prefix) for prefix in CAVEAT_STATUSES) or (status in CAVEAT_STATUSES):
        errors.append("pass-with-caveats is blocking; revise the artifact or mark it needs-revision/reject/reference-only.")
    if status and "fail" in text and "status: reject" not in text and "status: needs-revision" not in text:
        errors.append("QA text contains a failing style/composition review but status is not reject or needs-revision.")
    if any(text.startswith(prefix) for prefix in PASS_STATUSES) or (status in PASS_STATUSES):
        required = [
            ("Files/images opened with ChatGPT vision", "must state actual visual files opened with ChatGPT vision"),
            ("Contact sheet inspected: yes", "must state contact sheet was visually inspected"),
        ]
        original = read_text(path)
        for needle, message in required:
            if needle.lower() not in original.lower():
                errors.append(message)
        if "programmatic" in text:
            if not has_style_reference(text):
                errors.append("programmatic pass requires the accepted lesson style reference.")
            if "motion verification is not visual qa" not in text and "motion verifier" not in text:
                errors.append("programmatic pass must distinguish motion verification from visual QA.")
        if "gradient-descent" in rel(path).lower() or "how ai uses math" in text:
            if "style reference" not in text and "accepted source-frame qa" not in text:
                errors.append("How AI Uses Math video QA pass requires an explicit accepted style/reference comparison.")
            if "style/reference contact sheet inspected: yes" not in text:
                errors.append("How AI Uses Math video QA pass must state the accepted style/reference contact sheet was inspected.")
            if not has_style_reference(text):
                errors.append("How AI Uses Math video QA pass must preserve the accepted lesson style reference.")
            missing_terms = [term for term in LESSON_GATE_TERMS if term not in text]
            if missing_terms:
                errors.append(
                    "How AI Uses Math video QA pass must document the minimum lesson gate "
                    f"(missing: {', '.join(missing_terms)})."
                )
    return errors


def check_candidate(path: Path) -> list[str]:
    text = lower_text(path)
    data = json_value(path)
    errors: list[str] = []

    if path.name.endswith(".visual-qa.md"):
        errors.extend(check_visual_qa(path, text))
        return errors

    if not is_programmatic_candidate(path, text, data):
        return errors

    qa = paired_visual_qa(path)
    qa_text = lower_text(qa) if qa else ""
    if qa_text and is_rejected(qa_text):
        return errors

    if is_rejected(text):
        return errors

    combined = text + "\n" + qa_text
    if not has_style_reference(combined):
        errors.append("programmatic video candidate lacks an accepted lesson style reference.")
    if not has_style_preserving_animation_role(combined):
        errors.append("programmatic video candidate must state animation is a style-preserving enhancement, not the full visual style.")
    if qa is None and not is_source_draft(text):
        errors.append("programmatic video candidate has no paired visual QA note under outputs/video-renders/verification/.")
    elif qa is not None and "contact sheet inspected: yes" not in qa_text:
        errors.append(f"paired visual QA does not state contact sheet inspection: {rel(qa)}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify video style and QA guardrails.")
    parser.add_argument("paths", nargs="*", help="Specific files to check.")
    parser.add_argument("--changed", action="store_true", help="Check changed git files.")
    parser.add_argument("--all", action="store_true", help="Check all video manifest/script/QA files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.changed:
        paths = changed_files()
    elif args.all:
        paths = [path for part in VIDEO_PATH_PARTS for path in (ROOT / part).glob("**/*") if path.is_file()]
    else:
        paths = [Path(p) if Path(p).is_absolute() else ROOT / p for p in args.paths]

    files = candidate_files(paths)
    failures: list[str] = []
    for path in files:
        errors = check_candidate(path)
        for error in errors:
            failures.append(f"{rel(path)}: {error}")

    if failures:
        print("Video style gate failed:")
        for failure in failures:
            print(f"- {failure}")
        print("\nRun visual QA against actual contact sheets and preserve the accepted lesson style reference.")
        return 1

    print(f"Video style gate passed ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
