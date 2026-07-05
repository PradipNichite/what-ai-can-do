import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description="Convert a smart scene plan into a Creatomate manifest.")
    parser.add_argument("plan", help="Planner JSON.")
    parser.add_argument("--out", help="Output Creatomate manifest path.")
    args = parser.parse_args()

    plan_path = Path(args.plan).resolve()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))

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
        "voiceover": {
            "provider": "elevenlabs",
            "model_id": "eleven_multilingual_v2"
        },
        "scenes": [],
    }

    visual_cursor = 0
    for scene in plan["scenes"]:
        manifest["scenes"].append({
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
        })
        visual_cursor += scene["duration"]

    out_path = Path(args.out or ROOT / "outputs/video-manifests/student-ai-study-runway-smart-edit.en.json")
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
