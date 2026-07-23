#!/usr/bin/env python3
"""Verify QA verdict discipline for changed review notes.

This checker does not judge pixels. It prevents a process failure: treating
`pass-with-caveats` or unresolved caveats as a promotion signal.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REVIEW_ROOTS = (
    ROOT / "assets",
    ROOT / "outputs",
    ROOT / "research" / "notes",
)

PROMOTION_TERMS = (
    "accepted",
    "candidate",
    "comparison-ready",
    "complete",
    "proceed-to-prompts",
    "publish-ready",
    "ready to use",
    "sent to video generation",
    "visual-draft",
    "visual-qa",
)
REVISION_TERMS = (
    "needs-revision",
    "reject",
    "reference-only",
    "revise",
    "repair",
    "rerun",
    "fix",
    "blocked",
)
STATUS_RE = re.compile(r"^\s*(?:[-*]\s*)?status\s*:\s*`?([^`\n]+?)`?\s*$", re.IGNORECASE | re.MULTILINE)


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def changed_files() -> list[Path]:
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    paths: list[Path] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        raw = line[3:].strip()
        if " -> " in raw:
            raw = raw.split(" -> ", 1)[1].strip()
        raw = raw.strip('"')
        path = ROOT / raw
        if path.exists() and path.is_file():
            paths.append(path)
    return paths


def all_review_files() -> list[Path]:
    files: list[Path] = []
    for root in REVIEW_ROOTS:
        if root.exists():
            files.extend(path for path in root.glob("**/*.md") if is_review_file(path))
    return files


def is_review_file(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    resolved = path.resolve()
    if not any(resolved.is_relative_to(root.resolve()) for root in REVIEW_ROOTS):
        return False
    name = path.name.lower()
    text_path = rel(path).lower()
    return any(
        token in name or token in text_path
        for token in (
            "qa",
            "review",
            "scene-adequacy",
            "verification",
            "publish-ready",
        )
    )


def selected_files(args: argparse.Namespace) -> list[Path]:
    if args.files:
        return [Path(raw).resolve() if Path(raw).is_absolute() else ROOT / raw for raw in args.files]
    if args.all:
        return all_review_files()
    return [path for path in changed_files() if is_review_file(path)]


def status_values(text: str) -> list[str]:
    return [match.group(1).strip().strip("`").lower() for match in STATUS_RE.finditer(text)]


def overall_status(text: str) -> str | None:
    statuses = status_values(text)
    return statuses[0] if statuses else None


def meaningful_caveat_lines(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        lower = line.lower()
        if "caveat" not in lower:
            continue
        if any(token in lower for token in ("none", "no caveat", "no unresolved caveat")):
            continue
        lines.append(line.strip())
    return lines


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()
    status = overall_status(text)
    failures: list[str] = []

    has_caveated_status = status is not None and (
        "pass-with-caveats" in status or "pass with caveats" in status
    )
    if has_caveated_status:
        failures.append("pass-with-caveats is not a pass; mark the artifact needs-revision/reject/reference-only or rerun QA after fixes.")
        if any(term in lower for term in PROMOTION_TERMS):
            failures.append("caveated QA text also contains promotion language.")
        if not any(term in lower for term in REVISION_TERMS):
            failures.append("caveated QA text must name a repair/revision next action.")

    clean_pass = status == "pass"
    caveat_lines = meaningful_caveat_lines(text)
    if clean_pass and caveat_lines:
        failures.append("clean pass contains unresolved caveat language; resolve caveats or change the status.")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify QA verdict discipline.")
    parser.add_argument("files", nargs="*", help="Specific review/QA files to check.")
    parser.add_argument("--changed", action="store_true", help="Check changed review/QA files.")
    parser.add_argument("--all", action="store_true", help="Check all review/QA markdown files.")
    args = parser.parse_args()

    files = [path for path in selected_files(args) if path.exists() and path.is_file()]
    failures: list[str] = []
    for path in files:
        for failure in check_file(path):
            failures.append(f"{rel(path)}: {failure}")

    if failures:
        print("Visual QA verdict discipline failed:")
        for failure in failures:
            print(f"- {failure}")
        print("\nFix the caveats and rerun QA, or mark the artifact needs-revision/reject/reference-only.")
        return 1

    print(f"Visual QA verdict discipline passed ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
