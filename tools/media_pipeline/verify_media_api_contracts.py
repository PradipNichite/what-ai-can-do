#!/usr/bin/env python3
"""Verify local media API contract memory matches the repo wrappers."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains(path: Path, needles: list[str], failures: list[str]) -> None:
    text = read(path)
    for needle in needles:
        if needle not in text:
            failures.append(f"{path.relative_to(ROOT)} is missing expected API contract text: {needle}")


def main() -> int:
    failures: list[str] = []

    required_files = [
        ".agents/skills/media-api-contracts/SKILL.md",
        ".agents/skills/media-api-contracts/references/runway.md",
        ".agents/skills/media-api-contracts/references/creatomate.md",
        ".agents/skills/media-api-contracts/references/elevenlabs.md",
        ".agents/skills/media-api-contracts/references/tmpfiles.md",
        ".agents/skills/media-api-contracts/references/openai-media.md",
    ]
    for item in required_files:
        if not (ROOT / item).exists():
            failures.append(f"Missing media API contract file: {item}")

    contains(
        ROOT / ".env.example",
        ["OPENAI_API_KEY=", "RUNWAYML_API_SECRET=", "CREATOMATE_API_KEY=", "ELEVENLABS_API_KEY="],
        failures,
    )
    contains(
        ROOT / "tools" / "media_pipeline" / "generate_runway_clips.py",
        [
            "RUNWAYML_API_SECRET",
            "https://api.dev.runwayml.com/v1",
            "2024-11-06",
            "/image_to_video",
            "promptImage",
            "promptText",
            "x-runway-version",
        ],
        failures,
    )
    contains(
        ROOT / "tools" / "media_pipeline" / "render_creatomate_phase1.py",
        [
            "CREATOMATE_API_KEY",
            "https://api.creatomate.com/v1/renders",
            'json.dumps({"source": source}',
            '"authorization": f"Bearer {api_key}"',
        ],
        failures,
    )
    contains(
        ROOT / "tools" / "media_pipeline" / "generate_scene_voiceovers.py",
        [
            "ELEVENLABS_API_KEY",
            "ELEVENLABS_VOICE_ID",
            "eleven_multilingual_v2",
            "https://api.elevenlabs.io/v1/text-to-speech/",
            "xi-api-key",
            "voiceover_url",
        ],
        failures,
    )
    contains(
        ROOT / "tools" / "media_pipeline" / "upload_tmpfiles.py",
        [
            "https://tmpfiles.org/api/v1/upload",
            'name="file"',
            'replace("https://tmpfiles.org/", "https://tmpfiles.org/dl/")',
        ],
        failures,
    )
    contains(
        ROOT / "tools" / "media_pipeline" / "README.md",
        [
            "RUNWAYML_API_SECRET",
            "CREATOMATE_API_KEY",
            "ELEVENLABS_API_KEY",
            "source frames -> image-to-video clips -> ElevenLabs voice -> Creatomate assembly",
        ],
        failures,
    )
    contains(
        ROOT / "AGENT_SYSTEM_OVERVIEW.md",
        [
            ".agents/skills/media-api-contracts/SKILL.md",
            "tools/verify_media_api_contracts.py",
        ],
        failures,
    )

    if failures:
        print("Media API contract verification FAILED:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Media API contract verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
