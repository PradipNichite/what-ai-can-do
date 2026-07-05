import argparse
import base64
import json
import mimetypes
import os
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "outputs" / "video-manifests" / "ai-customer-support-agent.mr.phase1.json"


def load_dotenv():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def clean_url_part(part):
    return str(part).strip("/")


def join_url(base, *parts):
    return "/".join([base.rstrip("/"), *[clean_url_part(part) for part in parts]])


def real_value(value):
    if not value:
        return None
    value = value.strip()
    if not value:
        return None
    placeholders = ("your_", "https://your-public-host.example", "example.com")
    if any(token in value for token in placeholders):
        return None
    return value


def data_uri(path):
    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def image_source(manifest, scene, asset_base_url):
    if real_value(scene.get("image_url")):
        return scene["image_url"]
    if asset_base_url:
        return join_url(asset_base_url, manifest["image_base_path"], scene["image"])
    return data_uri(ROOT / manifest["image_base_path"] / scene["image"])


def transition_for(index, duration=0.35):
    if index == 0:
        return None
    directions = ["180°", "0°", "90°", "270°"]
    return {
        "duration": duration,
        "easing": "cubic-in-out",
        "transition": True,
        "type": "slide",
        "fade": False,
        "direction": directions[(index - 1) % len(directions)],
    }


def motion_for(name, index, intensity=1):
    if intensity >= 2:
        start_end = [
            ("135%", "170%"),
            ("175%", "132%"),
            ("145%", "185%"),
        ][index % 3]
        return {
            "type": "scale",
            "time": 0,
            "duration": "100%",
            "easing": "linear",
            "scope": "element",
            "start_scale": start_end[0],
            "end_scale": start_end[1],
            "fade": False,
        }

    if name == "pan_left_with_zoom":
        return {
            "type": "scale",
            "time": 0,
            "duration": "100%",
            "easing": "linear",
            "scope": "element",
            "start_scale": "112%",
            "end_scale": "126%",
            "fade": False,
        }
    if name == "pan_right_with_zoom":
        return {
            "type": "scale",
            "time": 0,
            "duration": "100%",
            "easing": "linear",
            "scope": "element",
            "start_scale": "126%",
            "end_scale": "112%",
            "fade": False,
        }
    return {
        "type": "scale",
        "time": 0,
        "duration": "100%",
        "easing": "linear",
        "scope": "element",
        "start_scale": "118%",
        "end_scale": "108%" if index % 2 else "128%",
        "fade": False,
    }


def shot_layouts(index):
    layouts = [
        [
            {"x": "50%", "y": "50%", "width": "100%", "height": "100%"},
            {"x": "43%", "y": "43%", "width": "148%", "height": "148%"},
            {"x": "62%", "y": "58%", "width": "176%", "height": "176%"},
        ],
        [
            {"x": "50%", "y": "50%", "width": "100%", "height": "100%"},
            {"x": "35%", "y": "45%", "width": "165%", "height": "165%"},
            {"x": "67%", "y": "55%", "width": "185%", "height": "185%"},
        ],
        [
            {"x": "50%", "y": "50%", "width": "100%", "height": "100%"},
            {"x": "58%", "y": "42%", "width": "155%", "height": "155%"},
            {"x": "48%", "y": "66%", "width": "190%", "height": "190%"},
        ],
    ]
    return layouts[index % len(layouts)]


def add_dynamic_scene(elements, manifest, scene, index, cursor, image_url):
    parts = [0.34, 0.33, 0.33]
    shot_durations = [round(scene["duration"] * part, 2) for part in parts]
    shot_durations[-1] = round(scene["duration"] - sum(shot_durations[:-1]), 2)
    layouts = shot_layouts(index)

    scene_labels = [
        scene["caption_title"],
        scene["caption_body"],
        ["AI = coach", "Ask better", "Practice wins", "Check it"][index % 4],
    ]

    shot_time = cursor
    for shot_index, shot_duration in enumerate(shot_durations):
        animations = [motion_for(scene.get("motion"), index + shot_index, intensity=2)]
        transition = transition_for(index * 3 + shot_index, duration=0.22 if shot_index else 0.45)
        if transition:
            animations.insert(0, transition)

        elements.append(
            {
                "type": "image",
                "track": 1,
                "time": shot_time,
                "duration": shot_duration,
                "source": image_url,
                "x": layouts[shot_index]["x"],
                "y": layouts[shot_index]["y"],
                "width": layouts[shot_index]["width"],
                "height": layouts[shot_index]["height"],
                "fit": "cover",
                "clip": True,
                "animations": [
                    *animations,
                    *(
                        [
                            {
                                "type": "shake",
                                "time": "start",
                                "duration": 0.22,
                            }
                        ]
                        if shot_index == 1
                        else []
                    ),
                ],
            }
        )

        if shot_index == 1:
            elements.append(
                {
                    "type": "shape",
                    "track": 2,
                    "time": shot_time,
                    "duration": 0.18,
                    "x": "50%",
                    "y": "50%",
                    "width": "100%",
                    "height": "100%",
                    "path": "M 0 0 L 100 0 L 100 100 L 0 100 L 0 0 Z",
                    "fill_color": "rgba(255, 204, 77, 0.34)",
                    "animations": [
                        {"type": "fade", "duration": 0.08, "time": "start"},
                        {"type": "fade", "duration": 0.1, "time": "end", "reversed": True},
                    ],
                }
            )

        elements.append(
            {
                "type": "text",
                "track": 3,
                "time": shot_time + 0.1,
                "duration": max(shot_duration - 0.22, 0.8),
                "text": scene_labels[shot_index],
                "x": "50%",
                "y": "84%" if shot_index != 0 else "16%",
                "width": "92%",
                "height": "13%",
                "x_alignment": "50%",
                "y_alignment": "50%",
                "fill_color": "#ffffff" if shot_index != 2 else "#07111f",
                "font_family": "Arial",
                "font_weight": 900,
                "font_size": "64px" if shot_index != 1 else "48px",
                "background_color": "rgba(8, 18, 31, 0.86)" if shot_index != 2 else "rgba(255, 204, 77, 0.95)",
                "border_radius": "14px",
                "padding": "20px 30px",
                "animations": [
                    {
                        "type": "slide",
                        "duration": 0.2,
                        "time": "start",
                        "easing": "cubic-out",
                        "direction": "90°" if shot_index != 0 else "270°",
                        "fade": True,
                    },
                    {
                        "type": "scale",
                        "duration": 0.25,
                        "time": "start",
                        "easing": "back-out",
                        "start_scale": "78%",
                        "end_scale": "100%",
                    },
                    {"type": "fade", "duration": 0.12, "time": "end", "reversed": True},
                ],
            }
        )

        shot_time += shot_duration

    elements.append(
        {
            "type": "text",
            "track": 4,
            "time": cursor + 0.05,
            "duration": 1.15,
            "text": f"{index + 1}",
            "x": "12%",
            "y": "12%",
            "width": "13%",
            "height": "8%",
            "x_alignment": "50%",
            "y_alignment": "50%",
            "fill_color": "#ffffff",
            "font_family": "Arial",
            "font_weight": 900,
            "font_size": "72px",
            "background_color": "rgba(232, 75, 59, 0.96)",
            "border_radius": "999px",
            "animations": [
                {"type": "scale", "duration": 0.28, "time": "start", "easing": "elastic-out", "start_scale": "25%", "end_scale": "100%"},
                {"type": "fade", "duration": 0.12, "time": "end", "reversed": True},
            ],
        }
    )


def add_clean_scene(elements, scene, index, image_url):
    animations = []
    transition = transition_for(index, duration=0.5)
    if transition:
        animations.append(transition)

    elements.append(
        {
            "type": "image",
            "track": 1,
            "source": image_url,
            "duration": scene["duration"],
            "x": "50%",
            "y": "50%",
            "width": "100%",
            "height": "100%",
            "fit": "contain",
            "clip": False,
            "animations": animations,
        }
    )


def add_clean_video_scene(elements, scene, cursor, crossfade=0):
    animations = []
    if crossfade and cursor > 0:
        animations.append({"type": "fade", "duration": crossfade, "time": "start"})

    elements.append(
        {
            "type": "video",
            "track": 1,
            "time": scene.get("video_time", cursor),
            "source": scene["video_url"],
            "duration": scene["duration"],
            "x": "50%",
            "y": "50%",
            "width": "100%",
            "height": "100%",
            "fit": "contain",
            "clip": False,
            "animations": animations,
        }
    )


def build_source(manifest, asset_base_url=None, voiceover_url=None, music_url=None, voice_id=None, style="clean"):
    elements = []
    cursor = 0

    for index, scene in enumerate(manifest["scenes"]):
        if scene.get("video_url"):
            crossfade = 0.28 if style == "paced" else 0
            add_clean_video_scene(elements, scene, cursor, crossfade=crossfade)
            cursor += scene["duration"]
            continue

        image_url = image_source(manifest, scene, asset_base_url)
        if style == "dynamic":
            add_dynamic_scene(elements, manifest, scene, index, cursor, image_url)
            cursor += scene["duration"]
            continue
        if style == "clean":
            add_clean_scene(elements, scene, index, image_url)
            cursor += scene["duration"]
            continue

        image_animations = [motion_for(scene.get("motion"), index)]
        transition = transition_for(index)
        if transition:
            image_animations.insert(0, transition)

        elements.append(
            {
                "type": "image",
                "track": 1,
                "source": image_url,
                "duration": scene["duration"],
                "x": "50%",
                "y": "50%",
                "width": "100%",
                "height": "100%",
                "fit": "cover",
                "clip": True,
                "animations": image_animations,
            }
        )

        if scene.get("caption_title") or scene.get("caption_body"):
            elements.append(
                {
                    "type": "text",
                    "track": 2,
                    "time": cursor + 0.35,
                    "duration": max(scene["duration"] - 0.65, 1),
                    "text": scene["caption_title"],
                    "x": "50%",
                    "y": "10%",
                    "width": "86%",
                    "height": "8%",
                    "x_alignment": "50%",
                    "y_alignment": "50%",
                    "fill_color": "#ffffff",
                    "font_family": "Arial",
                    "font_weight": 800,
                    "font_size": "58px",
                    "background_color": "rgba(8, 18, 31, 0.78)",
                    "border_radius": "18px",
                    "padding": "18px 28px",
                    "animations": [
                        {
                            "type": "slide",
                            "duration": 0.35,
                            "time": "start",
                            "easing": "cubic-out",
                            "direction": "270°",
                            "fade": True,
                        },
                        {"type": "fade", "duration": 0.2, "time": "end", "reversed": True},
                    ],
                }
            )
            elements.append(
                {
                    "type": "text",
                    "track": 3,
                    "time": cursor + 0.72,
                    "duration": max(scene["duration"] - 1.05, 1),
                    "text": scene["caption_body"],
                    "x": "50%",
                    "y": "90%",
                    "width": "84%",
                    "height": "9%",
                    "x_alignment": "50%",
                    "y_alignment": "50%",
                    "fill_color": "#07111f",
                    "font_family": "Arial",
                    "font_weight": 700,
                    "font_size": "42px",
                    "background_color": "rgba(255, 204, 77, 0.92)",
                    "border_radius": "18px",
                    "padding": "18px 28px",
                    "animations": [
                        {
                            "type": "slide",
                            "duration": 0.35,
                            "time": "start",
                            "easing": "cubic-out",
                            "direction": "90°",
                            "fade": True,
                        },
                        {"type": "fade", "duration": 0.2, "time": "end", "reversed": True},
                    ],
                }
            )
            elements.append(
                {
                    "type": "text",
                    "track": 4,
                    "time": cursor + 0.15,
                    "duration": min(scene["duration"], 1.4),
                    "text": f"{index + 1}",
                    "x": "12%",
                    "y": "19%",
                    "width": "10%",
                    "height": "7%",
                    "x_alignment": "50%",
                    "y_alignment": "50%",
                    "fill_color": "#ffffff",
                    "font_family": "Arial",
                    "font_weight": 900,
                    "font_size": "64px",
                    "background_color": "rgba(232, 75, 59, 0.9)",
                    "border_radius": "999px",
                    "animations": [
                        {"type": "scale", "duration": 0.35, "time": "start", "easing": "elastic-out", "start_scale": "45%", "end_scale": "100%"},
                        {"type": "fade", "duration": 0.2, "time": "end", "reversed": True},
                    ],
                }
            )

        cursor += scene["duration"]

    for scene in manifest["scenes"]:
        caption = scene.get("caption")
        if caption:
            caption_time = scene.get("caption_start", scene.get("voiceover_start", scene.get("video_time", 0)))
            caption_duration = scene.get("caption_duration", min(scene.get("duration", 3), 2.4))
            elements.append(
                {
                    "type": "text",
                    "track": 5,
                    "time": caption_time,
                    "duration": caption_duration,
                    "text": caption,
                    "x": "50%",
                    "y": "84%",
                    "width": "88%",
                    "height": "11%",
                    "x_alignment": "50%",
                    "y_alignment": "50%",
                    "fill_color": "#ffffff",
                    "font_family": "Arial",
                    "font_weight": 900,
                    "font_size": "56px",
                    "background_color": "rgba(5, 12, 24, 0.78)",
                    "border_radius": "18px",
                    "padding": "18px 28px",
                    "animations": [
                        {
                            "type": "scale",
                            "duration": 0.18,
                            "time": "start",
                            "easing": "back-out",
                            "start_scale": "82%",
                            "end_scale": "100%",
                        },
                        {"type": "fade", "duration": 0.12, "time": "end", "reversed": True},
                    ],
                }
            )

    for scene in manifest["scenes"]:
        for sfx_index, sfx in enumerate(scene.get("sfx", []), start=1):
            if not sfx.get("url"):
                continue
            elements.append(
                {
                    "name": f"SFX-{scene['id']}-{sfx_index}",
                    "type": "audio",
                    "track": 20 + sfx_index,
                    "source": sfx["url"],
                    "time": sfx.get("time", scene.get("video_time", 0)),
                    "duration": sfx.get("duration", 1),
                    "volume": sfx.get("volume", "45%"),
                }
            )

    voiceover = manifest.get("voiceover", {})
    scene_voiceovers = [scene for scene in manifest["scenes"] if scene.get("voiceover_url")]
    if scene_voiceovers:
        cursor = 0
        for index, scene in enumerate(manifest["scenes"]):
            if scene.get("voiceover_url"):
                elements.append(
                    {
                        "name": f"Voiceover-{index + 1}",
                        "type": "audio",
                        "track": 10,
                        "source": scene["voiceover_url"],
                        "time": scene.get("voiceover_start", cursor),
                        "duration": scene.get("audio_duration", scene["duration"]),
                    }
                )
            cursor += scene["duration"]
    elif voiceover_url:
        elements.append(
            {
                "name": "Voiceover-1",
                "type": "audio",
                "track": 10,
                "source": voiceover_url,
                "time": 0,
                "duration": manifest["target_duration_seconds"],
            }
        )
    elif voiceover.get("provider") == "creatomate-elevenlabs":
        effective_voice_id = real_value(voice_id) or real_value(voiceover.get("voice_id")) or real_value(os.environ.get("ELEVENLABS_VOICE_ID"))
        if not effective_voice_id:
            effective_voice_id = pick_first_elevenlabs_voice_id()
        model_id = voiceover.get("model_id", os.environ.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2"))
        stability = voiceover.get("stability", 0.72)
        elements.append(
            {
                "name": "Voiceover-1",
                "type": "audio",
                "track": 10,
                "source": voiceover["text"],
                "provider": f"elevenlabs model_id={model_id} voice_id={effective_voice_id} stability={stability}",
                "time": 0,
                "duration": manifest["target_duration_seconds"],
            }
        )
    else:
        raise SystemExit("Missing voiceover. Provide VOICEOVER_URL or use manifest voiceover.provider=creatomate-elevenlabs.")

    if music_url:
        elements.append(
            {
                "type": "audio",
                "track": 11,
                "source": music_url,
                "time": 0,
                "duration": manifest["target_duration_seconds"],
                "volume": manifest.get("music", {}).get("volume", "12%"),
            }
        )

    return {
        "output_format": manifest["output_format"],
        "width": manifest["width"],
        "height": manifest["height"],
        "frame_rate": manifest["fps"],
        "duration": manifest["target_duration_seconds"],
        "elements": elements,
    }


def start_render(api_key, source):
    body = json.dumps({"source": source}, ensure_ascii=False).encode("utf-8")
    request = Request(
        "https://api.creatomate.com/v1/renders",
        data=body,
        headers={
            "authorization": f"Bearer {api_key}",
            "content-type": "application/json",
            "user-agent": "Creatomate-Phase1-Python/0.1",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Creatomate request failed ({error.code}): {detail}") from error


def fetch_render(api_key, render_id):
    request = Request(
        f"https://api.creatomate.com/v1/renders/{render_id}",
        headers={
            "authorization": f"Bearer {api_key}",
            "user-agent": "Creatomate-Phase1-Python/0.1",
        },
        method="GET",
    )
    try:
        with urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Creatomate status request failed ({error.code}): {detail}") from error


def pick_first_elevenlabs_voice_id():
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise SystemExit("Missing ELEVENLABS_VOICE_ID and ELEVENLABS_API_KEY; cannot choose a default voice.")
    request = Request(
        "https://api.elevenlabs.io/v1/voices",
        headers={"xi-api-key": api_key},
        method="GET",
    )
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs voices request failed ({error.code}): {detail}") from error

    voices = data.get("voices", [])
    if not voices:
        raise SystemExit("ElevenLabs account returned no voices.")
    voice = voices[0]
    print(f"Using ElevenLabs voice from account: {voice.get('name', 'Unnamed')} ({voice['voice_id']})")
    return voice["voice_id"]


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Build or submit a Creatomate Phase 1 render.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Path to the video manifest JSON.")
    parser.add_argument("--asset-base-url", default=os.environ.get("VIDEO_ASSET_BASE_URL"), help="Public base URL for repo assets.")
    parser.add_argument("--voiceover-url", default=os.environ.get("VOICEOVER_URL"), help="Public URL for the ElevenLabs MP3.")
    parser.add_argument("--voice-id", default=os.environ.get("ELEVENLABS_VOICE_ID"), help="ElevenLabs voice ID for Creatomate TTS.")
    parser.add_argument("--music-url", default=os.environ.get("MUSIC_URL"), help="Optional public music URL.")
    parser.add_argument("--style", choices=["clean", "paced", "dynamic", "captioned"], default="clean", help="Render style. clean preserves cards without overlays.")
    parser.add_argument("--submit", action="store_true", help="Submit the render to Creatomate.")
    parser.add_argument("--wait", action="store_true", help="Poll Creatomate until the render finishes.")
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    asset_base_url = real_value(args.asset_base_url)
    voiceover_url = real_value(args.voiceover_url) or real_value(manifest.get("voiceover", {}).get("public_url"))
    voice_id = real_value(args.voice_id)
    music_url = real_value(args.music_url) or real_value(manifest.get("music", {}).get("public_url"))

    if not asset_base_url:
        print("No VIDEO_ASSET_BASE_URL set; embedding local PNGs as data URLs.")

    source = build_source(manifest, asset_base_url, voiceover_url, music_url, voice_id, args.style)
    out_dir = ROOT / "outputs" / "video-renders"
    out_dir.mkdir(parents=True, exist_ok=True)
    source_path = out_dir / f"{manifest['id']}.creatomate-source.json"
    source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote Creatomate source JSON: {source_path.relative_to(ROOT)}")

    if not args.submit:
        print("Dry run only. Add --submit to start a Creatomate render.")
        return

    api_key = os.environ.get("CREATOMATE_API_KEY")
    if not api_key:
        raise SystemExit("Missing CREATOMATE_API_KEY environment variable.")

    renders = start_render(api_key, source)
    response_path = out_dir / f"{manifest['id']}.creatomate-render-response.json"
    response_path.write_text(json.dumps(renders, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Started {len(renders)} Creatomate render(s).")
    for render in renders:
        print(f"{render.get('id')}: {render.get('status')}")
        if render.get("url"):
            print(render["url"])
    print(f"Saved render response: {response_path.relative_to(ROOT)}")

    if args.wait:
        final = []
        unfinished = {render["id"] for render in renders}
        deadline = time.time() + 900
        while unfinished and time.time() < deadline:
            time.sleep(5)
            for render_id in list(unfinished):
                render = fetch_render(api_key, render_id)
                status = render.get("status")
                print(f"{render_id}: {status}")
                if status not in {"planned", "waiting", "transcribing", "rendering"}:
                    unfinished.remove(render_id)
                    final.append(render)
                    if render.get("url"):
                        print(render["url"])
                    if render.get("error_message"):
                        print(render["error_message"])
        final_path = out_dir / f"{manifest['id']}.creatomate-render-final.json"
        final_path.write_text(json.dumps(final, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Saved final render status: {final_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
