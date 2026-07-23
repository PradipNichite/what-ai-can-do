#!/usr/bin/env python3
"""Classify lesson scenes into motion/rendering strategies.

The first version is deterministic and rule-based on purpose. It gives the
pipeline stable routing fields before we add an LLM reviewer or backend-specific
quality scoring.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]


PROGRAMMATIC_STRONG = {
    "axis",
    "bar",
    "curve",
    "derivative",
    "direction",
    "formula",
    "gradient",
    "graph",
    "learning rate",
    "matrix",
    "meter",
    "minimum",
    "numeric",
    "opposite",
    "overshoot",
    "point",
    "probability",
    "slope",
    "step",
    "threshold",
    "update",
    "vector",
    "weight",
}

PROGRAMMATIC_SUPPORT = {
    "compare",
    "computed",
    "decrease",
    "distance",
    "error",
    "improve",
    "improves",
    "lower",
    "loss",
    "measure",
    "number",
    "repeat",
    "reduce",
    "score",
    "scoring",
    "smaller",
    "value",
}

IMAGE_TO_VIDEO = {
    "camera",
    "character",
    "desk",
    "expression",
    "face",
    "hand",
    "human",
    "learner",
    "notebook",
    "phone",
    "reaction",
    "room",
    "student",
    "tablet",
    "teacher",
}

STILL = {
    "definition",
    "memory anchor",
    "recap",
    "summary",
}

IMAGE_FALLBACK = {
    "correct answer",
    "mistake",
    "prediction",
}


@dataclass
class SceneInput:
    id: str
    source_step: str
    scene_title: str
    learning_job: str
    core_visual_idea: str
    technical_truth: str
    source: dict[str, Any]


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "scene"


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def extract_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def extract_section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+\d+\.\s+{re.escape(heading)}\s*$"
        r"(?P<body>.*?)(?=^##\s+\d+\.|\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(markdown)
    return match.group("body") if match else ""


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_scene_flow(markdown: str) -> list[SceneInput]:
    section = extract_section(markdown, "Renderer-Agnostic Scene Flow")
    rows = [line for line in section.splitlines() if line.strip().startswith("|")]
    if len(rows) < 3:
        return []

    headers = [normalize(cell) for cell in split_table_row(rows[0])]
    scenes: list[SceneInput] = []
    for raw in rows[2:]:
        cells = split_table_row(raw)
        if len(cells) != len(headers):
            continue
        item = dict(zip(headers, cells))
        step = item.get("step", str(len(scenes) + 1))
        title = item.get("teaching job", f"Scene {step}")
        scenes.append(
            SceneInput(
                id=f"scene-{int(step):02d}" if step.isdigit() else slugify(title),
                source_step=step,
                scene_title=title,
                learning_job=title,
                core_visual_idea=item.get("core visual idea", ""),
                technical_truth=item.get("must be technically true", ""),
                source=item,
            )
        )
    return scenes


def parse_plan_json(plan: dict[str, Any]) -> list[SceneInput]:
    scenes: list[SceneInput] = []
    for index, scene in enumerate(plan.get("scenes", []), start=1):
        scene_id = str(scene.get("id") or f"scene-{index:02d}")
        title = str(scene.get("scene_title") or scene.get("title") or scene.get("beat") or scene_id)
        learning_job = str(scene.get("learning_job") or scene.get("voiceover_text") or title)
        visual = str(scene.get("core_visual_idea") or scene.get("visual_role") or scene.get("caption") or "")
        truth = str(scene.get("technical_truth") or scene.get("motion_role") or "")
        scenes.append(
            SceneInput(
                id=scene_id,
                source_step=str(scene.get("source_step") or index),
                scene_title=title,
                learning_job=learning_job,
                core_visual_idea=visual,
                technical_truth=truth,
                source=scene,
            )
        )
    return scenes


def count_signals(text: str, terms: set[str]) -> list[str]:
    return sorted(term for term in terms if term in text)


def verification_for(strategy: str) -> dict[str, Any]:
    common = {
        "requires_contact_sheet_review": True,
        "text_readability_required": True,
    }
    if strategy == "programmatic-technical-animation":
        return {
            **common,
            "commands": [
                "python tools/render_programmatic_animation.py --spec <scene-spec> --backend auto --out <clip.mp4>",
                "python tools/verify_video_motion.py <clip.mp4> --samples 12",
            ],
            "acceptance_checks": [
                "primary labels and captions are readable in sampled frames",
                "technical motion preserves exact graph, meter, arrow, or numeric relationships",
                "no blank frames or black borders",
            ],
        }
    if strategy == "hybrid-overlay":
        return {
            **common,
            "commands": [
                "python tools/verify_video_motion.py <assembled-or-generated-clip.mp4> --samples 12",
            ],
            "acceptance_checks": [
                "generated base motion does not warp the technical overlay",
                "overlay labels remain readable after assembly",
                "context and technical animation feel connected in one beat",
            ],
        }
    if strategy == "image-to-video":
        return {
            **common,
            "commands": [
                "python tools/verify_video_motion.py <generated-clip.mp4> --samples 12",
            ],
            "acceptance_checks": [
                "subject motion supports the teaching beat",
                "text-heavy areas do not morph or disappear",
                "identity and composition stay stable",
            ],
        }
    return {
        **common,
        "commands": [
            "python tools/verify_video_motion.py <assembled-clip.mp4> --samples 8",
        ],
        "acceptance_checks": [
            "subtle motion or reveal is enough for pacing",
            "readable text is prioritized over motion intensity",
            "no blank frames or black borders",
        ],
    }


def routing_fields(strategy: str) -> dict[str, Any]:
    if strategy == "programmatic-technical-animation":
        return {
            "preferred_backend": "pillow",
            "candidate_backends": ["pillow", "motion-canvas", "revideo", "remotion", "manim"],
            "fallback_strategy": "hybrid-overlay",
        }
    if strategy == "hybrid-overlay":
        return {
            "preferred_backend": "remotion-or-creatomate-assembly",
            "candidate_backends": ["pillow-overlay", "motion-canvas-overlay", "remotion", "creatomate"],
            "base_clip_candidates": ["runway", "veo", "luma", "fal"],
            "fallback_strategy": "programmatic-technical-animation",
        }
    if strategy == "image-to-video":
        return {
            "preferred_provider": "runway",
            "candidate_providers": ["runway", "veo", "luma", "fal"],
            "fallback_strategy": "still-animation",
        }
    return {
        "preferred_backend": "remotion-or-creatomate-assembly",
        "candidate_backends": ["remotion", "creatomate", "pillow"],
        "fallback_strategy": "static-card",
    }


def classify_scene(scene: SceneInput) -> dict[str, Any]:
    text = normalize(" ".join([scene.scene_title, scene.learning_job, scene.core_visual_idea, scene.technical_truth]))
    strong = count_signals(text, PROGRAMMATIC_STRONG)
    support = count_signals(text, PROGRAMMATIC_SUPPORT)
    image = count_signals(text, IMAGE_TO_VIDEO)
    still = count_signals(text, STILL)
    image_fallback = count_signals(text, IMAGE_FALLBACK)

    if strong:
        strategy = "programmatic-technical-animation"
        reason = "The beat depends on precise technical motion: " + ", ".join(strong[:4]) + "."
    elif support and image:
        strategy = "hybrid-overlay"
        reason = "The beat mixes generated context with technical evidence: " + ", ".join((support + image)[:4]) + "."
    elif support and len(support) >= 2:
        strategy = "hybrid-overlay"
        reason = "The beat needs a readable score/meter overlay, but not a full graph animation."
    elif image or image_fallback:
        strategy = "image-to-video"
        reason = "The beat is mainly contextual or cinematic rather than geometry-precise."
    elif still:
        strategy = "still-animation"
        reason = "The beat is mainly recap/summary text, so subtle reveal motion is enough."
    else:
        strategy = "still-animation"
        reason = "No strong technical or cinematic motion signal was found."

    return {
        "id": scene.id,
        "source_step": scene.source_step,
        "scene_title": scene.scene_title,
        "learning_job": scene.learning_job,
        "core_visual_idea": scene.core_visual_idea,
        "technical_truth": scene.technical_truth,
        "requires_animation": strategy != "still-animation",
        "renderer_strategy": strategy,
        **routing_fields(strategy),
        "reason": reason,
        "signals": {
            "programmatic_strong": strong,
            "programmatic_support": support,
            "image_to_video": image,
            "still_animation": still,
            "contextual_fallback": image_fallback,
        },
        "verification_required": verification_for(strategy),
    }


def build_report(result: dict[str, Any]) -> str:
    lines = [
        f"# {result['title']} Motion Strategy Classification",
        "",
        f"Source: `{result['source']}`",
        "",
        "## Summary",
        "",
    ]
    for strategy, count in sorted(result["summary"]["strategy_counts"].items()):
        lines.append(f"- `{strategy}`: {count}")
    lines.extend(
        [
            "",
            "## Scene Routing",
            "",
            "| Scene | Requires animation | Strategy | Preferred | Reason |",
            "|---|---:|---|---|---|",
        ]
    )
    for scene in result["scenes"]:
        preferred = scene.get("preferred_backend") or scene.get("preferred_provider") or ""
        lines.append(
            "| {title} | {requires} | `{strategy}` | `{preferred}` | {reason} |".format(
                title=scene["scene_title"],
                requires="yes" if scene["requires_animation"] else "no",
                strategy=scene["renderer_strategy"],
                preferred=preferred,
                reason=scene["reason"],
            )
        )
    lines.extend(
        [
            "",
            "## Pipeline Rule",
            "",
            "Run this classifier after scene flow or beat planning. Programmatic scenes should render and pass motion/contact-sheet checks before final assembly. Image-to-video scenes should use video-specific source frames with less embedded text, then pass the same sampled-frame verification.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify scenes into video motion/rendering strategies.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--source-module", help="Markdown source module with a Renderer-Agnostic Scene Flow table.")
    source.add_argument("--plan", help="JSON scene/beat plan.")
    parser.add_argument("--out", required=True, help="Output JSON strategy manifest.")
    parser.add_argument("--md-out", help="Optional human-readable Markdown report.")
    args = parser.parse_args()

    if args.source_module:
        input_path = Path(args.source_module)
        if not input_path.is_absolute():
            input_path = ROOT / input_path
        markdown = input_path.read_text(encoding="utf-8")
        title = extract_title(markdown, input_path.stem)
        scenes = parse_scene_flow(markdown)
    else:
        input_path = Path(args.plan)
        if not input_path.is_absolute():
            input_path = ROOT / input_path
        plan = json.loads(input_path.read_text(encoding="utf-8"))
        title = str(plan.get("title") or plan.get("id") or input_path.stem)
        scenes = parse_plan_json(plan)

    if not scenes:
        raise SystemExit("No scenes found. Expected a Renderer-Agnostic Scene Flow table or JSON scenes array.")

    classified = [classify_scene(scene) for scene in scenes]
    counts = Counter(scene["renderer_strategy"] for scene in classified)
    result = {
        "id": slugify(title) + "-motion-strategy-v1",
        "title": title,
        "source": rel(input_path),
        "classifier": {
            "name": "rule-based-motion-strategy-classifier",
            "version": "1",
            "strategy_options": [
                "programmatic-technical-animation",
                "hybrid-overlay",
                "image-to-video",
                "still-animation",
            ],
        },
        "summary": {
            "scene_count": len(classified),
            "strategy_counts": dict(sorted(counts.items())),
        },
        "scenes": classified,
    }

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.md_out:
        md_path = Path(args.md_out)
        if not md_path.is_absolute():
            md_path = ROOT / md_path
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(build_report(result), encoding="utf-8")

    print(rel(out_path))
    if args.md_out:
        print(rel(md_path))


if __name__ == "__main__":
    main()
