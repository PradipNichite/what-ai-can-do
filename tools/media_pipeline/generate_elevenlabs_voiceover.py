import argparse
import json
import os
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


def post_json(url, headers, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(url, data=body, headers=headers, method="POST")
    try:
        with urlopen(request, timeout=120) as response:
            return response.read()
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs request failed ({error.code}): {detail}") from error


def real_value(value):
    if not value:
        return None
    value = value.strip()
    if not value or value.startswith("your_"):
        return None
    return value


def pick_first_voice_id(api_key):
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

    parser = argparse.ArgumentParser(description="Generate Phase 1 Marathi voiceover with ElevenLabs.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Path to the video manifest JSON.")
    parser.add_argument("--voice-id", default=os.environ.get("ELEVENLABS_VOICE_ID"), help="ElevenLabs voice ID.")
    parser.add_argument("--model-id", default=os.environ.get("ELEVENLABS_MODEL_ID"), help="ElevenLabs model ID.")
    parser.add_argument("--out", help="Output MP3 path. Defaults to manifest.voiceover.local_output_path.")
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise SystemExit("Missing ELEVENLABS_API_KEY environment variable.")
    voice_id = real_value(args.voice_id) or pick_first_voice_id(api_key)

    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    model_id = args.model_id or manifest.get("voiceover", {}).get("model_id", "eleven_multilingual_v2")
    default_out = manifest.get("voiceover", {}).get("local_output_path")
    if not default_out:
        default_out = f"outputs/video-assets/{manifest['id']}.voiceover.mp3"
    out_path = Path(args.out or default_out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    text = manifest.get("voiceover", {}).get("text")
    if not text:
        text = "\n\n".join(scene["voiceover"] for scene in manifest["scenes"])
    audio = post_json(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        {
            "xi-api-key": api_key,
            "accept": "audio/mpeg",
            "content-type": "application/json",
        },
        {
            "text": text,
            "model_id": model_id,
            "voice_settings": {
                "stability": 0.48,
                "similarity_boost": 0.78,
                "style": 0.18,
                "use_speaker_boost": True,
            },
        },
    )

    out_path.write_bytes(audio)
    print(f"Created voiceover: {out_path.relative_to(ROOT)}")
    print(f"Bytes: {len(audio)}")


if __name__ == "__main__":
    main()
