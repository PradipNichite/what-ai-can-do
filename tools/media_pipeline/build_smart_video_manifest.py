import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description="Convert a smart scene plan into a Creatomate manifest.")
    parser.add_argument("plan", help="Planner JSON.")
    parser.add_argument("--motion-strategy", help="Optional scene motion strategy classifier JSON.")
    parser.add_argument("--out", help="Output Creatomate manifest path.")
    args = parser.parse_args()

    plan_path = Path(args.plan).resolve()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    motion_strategy_path = Path(args.motion_strategy).resolve() if args.motion_strategy else None
    motion_strategy = json.loads(motion_strategy_path.read_text(encoding="utf-8")) if motion_strategy_path else None

    motion_by_id = {}
    if motion_strategy:
        for item in motion_strategy.get("scenes", []):
            keys = {item.get("id"), item.get("source_step")}
            if item.get("source_step") and str(item["source_step"]).isdigit():
                keys.add(f"scene-{int(item['source_step']):02d}")
            keys.add(str(item.get("scene_title", "")).strip().lower())
            for key in keys:
                if key:
                    motion_by_id[str(key)] = item

    total_duration = round(max(
        scene["voiceover_start"] + scene.get("audio_duration", scene["duration"])
        for scene in plan["scenes"]
    ), 2)
    visual_duration = round(sum(scene["duration"] for scene in plan["scenes"]), 2)
    total_duration = max(total_duration, visual_duration)

    manifest_id = plan["id"].replace("-plan", "-edit-en")

    manifest = {
        "id": manifest_id,
        "title": "How Students Can Use AI To Study Better - Smart Planned Edit",
        "language": "en-IN",
        "format": "vertical-video",
        "width": 720,
        "height": 1280,
        "fps": 30,
        "output_format": "mp4",
        "target_duration_seconds": total_duration,
        "source_plan": str(plan_path.relative_to(ROOT)),
        **({"motion_strategy_source": str(motion_strategy_path.relative_to(ROOT))} if motion_strategy_path else {}),
        "voiceover": {
            "provider": "elevenlabs",
            "model_id": "eleven_multilingual_v2"
        },
        "scenes": [],
    }

    visual_cursor = 0
    for scene in plan["scenes"]:
        scene_motion = (
            motion_by_id.get(str(scene.get("id", "")))
            or motion_by_id.get(str(scene.get("source_step", "")))
            or motion_by_id.get(str(scene.get("title", "")).strip().lower())
        )
        scene_payload = {
            "id": scene["id"],
            "duration": scene["duration"],
            "video_time": round(visual_cursor, 2),
            "video_url": scene["video_url"],
            "voiceover_text": scene["voiceover_text"],
            "voiceover_start": scene["voiceover_start"],
            "audio_duration": scene.get("audio_duration", scene["duration"]),
            **({"caption": scene["caption"]} if scene.get("caption") else {}),
            **({"caption_start": scene["caption_start"]} if scene.get("caption_start") is not None else {}),
            **({"caption_duration": scene["caption_duration"]} if scene.get("caption_duration") is not None else {}),
            **({"sfx": scene["sfx"]} if scene.get("sfx") else {}),
        }
        if scene_motion:
            scene_payload["motion_strategy"] = {
                "requires_animation": scene_motion["requires_animation"],
                "renderer_strategy": scene_motion["renderer_strategy"],
                "preferred_backend": scene_motion.get("preferred_backend"),
                "preferred_provider": scene_motion.get("preferred_provider"),
                "fallback_strategy": scene_motion.get("fallback_strategy"),
                "reason": scene_motion.get("reason"),
            }
        for key in ("renderer_strategy", "animation_backend", "clip_provider", "assembly_provider"):
            if scene.get(key) is not None:
                scene_payload[key] = scene[key]
        manifest["scenes"].append(scene_payload)
        visual_cursor += scene["duration"]

    out_path = Path(args.out or ROOT / "outputs/video-manifests/student-ai-study-runway-smart-edit.en.json")
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
