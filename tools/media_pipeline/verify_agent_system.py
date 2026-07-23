#!/usr/bin/env python3
"""Verify the repo agent overview matches installed local skills and hooks."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def local_skill_paths() -> list[str]:
    skills_dir = ROOT / ".agents" / "skills"
    if not skills_dir.exists():
        return []
    return sorted(
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in skills_dir.glob("*/SKILL.md")
    )


def hook_commands() -> list[str]:
    hooks_path = ROOT / ".codex" / "hooks.json"
    if not hooks_path.exists():
        return []
    data = json.loads(read(hooks_path))
    commands: list[str] = []
    for event in data.get("hooks", {}).values():
        for group in event:
            for hook in group.get("hooks", []):
                for key in ("command", "commandWindows"):
                    value = hook.get(key)
                    if isinstance(value, str):
                        commands.append(value.replace("\\", "/"))
    return commands


def main() -> int:
    failures: list[str] = []

    overview_path = ROOT / "AGENT_SYSTEM_OVERVIEW.md"
    overview = read(overview_path) if overview_path.exists() else ""

    for skill_path in local_skill_paths():
        if skill_path not in overview:
            failures.append(f"AGENT_SYSTEM_OVERVIEW.md does not mention local skill: {skill_path}")

    expected_stop_commands = (
        "tools/verify_agent_system.py",
        "tools/verify_image_story_gate.py",
        "tools/verify_media_api_contracts.py",
        "tools/verify_video_style_gate.py",
        "tools/verify_visual_qa_verdicts.py",
    )
    commands = hook_commands()
    for expected in expected_stop_commands:
        if not any(expected in command for command in commands):
            failures.append(f".codex/hooks.json does not run: {expected}")

    pre_commit_path = ROOT / ".githooks" / "pre-commit"
    pre_commit = read(pre_commit_path) if pre_commit_path.exists() else ""
    for expected in expected_stop_commands:
        if expected not in pre_commit:
            failures.append(f".githooks/pre-commit does not run: {expected}")

    agents = read(ROOT / "AGENTS.md") if (ROOT / "AGENTS.md").exists() else ""
    for section in (
        "Documentation Hygiene",
        "Image-Only Educational Stories",
        "Media API Contracts",
        "Video Style Gate",
    ):
        if section not in agents:
            failures.append(f"AGENTS.md is missing mandatory section: {section}")

    if "pass-with-caveats" not in agents or "not a pass" not in agents:
        failures.append("AGENTS.md must state that pass-with-caveats is not a pass.")

    if failures:
        print("Agent system verification FAILED:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Agent system verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
