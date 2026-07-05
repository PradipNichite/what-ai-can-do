import argparse
import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]


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


def real_value(value):
    if not value:
        return None
    value = value.strip()
    if not value or value.startswith("your_"):
        return None
    return value


def generate_sfx(api_key, text, duration):
    payload = {
        "text": text,
        "duration_seconds": duration,
        "prompt_influence": 0.45,
        "model_id": "eleven_text_to_sound_v2",
    }
    request = Request(
        "https://api.elevenlabs.io/v1/sound-generation",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "accept": "audio/mpeg",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=180) as response:
            return response.read()
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs SFX request failed ({error.code}): {detail}") from error


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Generate ElevenLabs SFX MP3 files.")
    parser.add_argument("manifest", help="JSON object with an sfx list.")
    args = parser.parse_args()

    api_key = real_value(os.environ.get("ELEVENLABS_API_KEY"))
    if not api_key:
        raise SystemExit("Missing ELEVENLABS_API_KEY.")

    path = Path(args.manifest).resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data["sfx"]

    out_dir = ROOT / "outputs" / "video-assets" / "sfx" / path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    for item in items:
        out_path = out_dir / f"{item['id']}.mp3"
        audio = generate_sfx(api_key, item["prompt"], item.get("duration", 0.8))
        out_path.write_bytes(audio)
        print(f"{item['id']}: {out_path.relative_to(ROOT)} ({len(audio)} bytes)")


if __name__ == "__main__":
    main()
