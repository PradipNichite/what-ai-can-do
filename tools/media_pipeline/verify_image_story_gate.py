#!/usr/bin/env python3
"""Verify image-only educational story gate language.

This checker is intentionally conservative. It cannot judge final artwork taste,
but it prevents the most common failure: treating the gate as buried guidance
instead of an explicit preflight/review requirement.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

PROMPT_REQUIRED = {
    "self-contained opener": ["self-contained", "opener"],
    "native generated composition": ["native", "generated", "composition"],
    "complete designed poster/card": ["complete designed", "poster"],
    "not pasted overlay": ["pasted", "overlay"],
    "integrated text plan": [
        "tablet",
        "notebook",
        "poster typography",
        "sticky",
        "callout",
    ],
}

REVIEW_REQUIRED = {
    "self-contained opener review": ["self-contained", "opener"],
    "native composition review": ["native", "composition"],
    "overlay failure check": ["overlay"],
    "mobile readability": ["readable"],
    "verdict": ["verdict"],
}


def run_git_changed() -> list[Path]:
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
        paths.append(ROOT / raw)
    return paths


def candidate_files(mode: str, explicit: list[str]) -> list[Path]:
    if explicit:
        return [Path(p).resolve() for p in explicit]
    if mode == "all":
        files = list((ROOT / "assets" / "image-prompts").glob("*image-story*.md"))
        files += list((ROOT / "assets" / "images").glob("*image-story*/*review-notes.md"))
        return files
    changed = run_git_changed()
    return [
        p
        for p in changed
        if p.suffix.lower() == ".md"
        and (
            ("assets" in p.parts and "image-prompts" in p.parts and "image-story" in p.name)
            or ("assets" in p.parts and "images" in p.parts and "review-notes" in p.name)
        )
    ]


def contains_all(text: str, terms: list[str]) -> bool:
    lower = text.lower()
    return all(term.lower() in lower for term in terms)


def check_file(path: Path) -> list[str]:
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    text = path.read_text(encoding="utf-8", errors="replace")
    lower_name = path.name.lower()
    failures: list[str] = []

    if "image-story" in lower_name and "review" not in lower_name:
        for label, terms in PROMPT_REQUIRED.items():
            if not contains_all(text, terms):
                failures.append(f"{rel}: missing prompt gate: {label} ({', '.join(terms)})")

    if "review-notes" in lower_name:
        for label, terms in REVIEW_REQUIRED.items():
            if not contains_all(text, terms):
                failures.append(f"{rel}: missing review gate: {label} ({', '.join(terms)})")
        verdict_text = text.lower()
        if "accepted" in verdict_text and "native" not in verdict_text:
            failures.append(f"{rel}: accepted verdict must explicitly mention native composition")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--changed", action="store_true", help="check changed image-story files")
    group.add_argument("--all", action="store_true", help="check all image-story prompt/review files")
    parser.add_argument("files", nargs="*", help="specific files to check")
    args = parser.parse_args()

    mode = "all" if args.all else "changed"
    files = candidate_files(mode, args.files)
    if not files:
        print("Image story gate: no changed image-story prompt/review files to check.")
        return 0

    failures: list[str] = []
    for path in files:
        if path.exists():
            failures.extend(check_file(path))

    if failures:
        print("Image story gate FAILED:")
        for failure in failures:
            print(f"- {failure}")
        print("\nRead IMAGE_STORY_GATE.md and fix the prompt pack/review before accepting visuals.")
        return 1

    print(f"Image story gate passed for {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
