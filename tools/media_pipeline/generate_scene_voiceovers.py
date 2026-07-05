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


def elevenlabs_request(api_key, voice_id, model_id, text):
    request = Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=json.dumps(
            {
                "text": text,
                "model_id": model_id,
                "voice_settings": {
                    "stability": 0.54,
                    "similarity_boost": 0.78,
                    "style": 0.1,
                    "use_speaker_boost": True,
                },
            },
            ensure_ascii=False,
        ).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "accept": "audio/mpeg",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=120) as response:
            return response.read()
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs request failed ({error.code}): {detail}") from error


def pick_first_voice_id(api_key):
    request = Request(
        "https://api.elevenlabs.io/v1/voices",
        headers={"xi-api-key": api_key},
        method="GET",
    )
    with urlopen(request, timeout=60) as response:
        voices = json.loads(response.read().decode("utf-8")).get("voices", [])
    if not voices:
        raise SystemExit("ElevenLabs account returned no voices.")
    voice = voices[0]
    print(f"Using ElevenLabs voice from account: {voice.get('name', 'Unnamed')} ({voice['voice_id']})")
    return voice["voice_id"]


def upload_tmpfiles(path):
    # Keep upload implementation in PowerShell/curl out of this script? No: use urllib multipart here.
    boundary = "----codex-boundary"
    data = path.read_bytes()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
        "Content-Type: audio/mpeg\r\n\r\n"
    ).encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")

    request = Request(
        "https://tmpfiles.org/api/v1/upload",
        data=body,
        headers={"content-type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    with urlopen(request, timeout=180) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result["data"]["url"].replace("https://tmpfiles.org/", "https://tmpfiles.org/dl/")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Generate one ElevenLabs MP3 per manifest scene.")
    parser.add_argument("manifest", help="Manifest with scenes[].voiceover_text.")
    parser.add_argument("--voice-id", help="Override ElevenLabs voice ID.")
    parser.add_argument("--no-upload", action="store_true", help="Only create local MP3 files.")
    parser.add_argument("--write-manifest", action="store_true", help="Patch scenes[].voiceover_url into the manifest.")
    args = parser.parse_args()

    api_key = real_value(os.environ.get("ELEVENLABS_API_KEY"))
    if not api_key:
        raise SystemExit("Missing ELEVENLABS_API_KEY.")

    voice_id = real_value(args.voice_id) or real_value(os.environ.get("ELEVENLABS_VOICE_ID")) or pick_first_voice_id(api_key)
    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    model_id = manifest.get("voiceover", {}).get("model_id", os.environ.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2"))

    out_dir = ROOT / "outputs" / "video-assets" / manifest["id"]
    out_dir.mkdir(parents=True, exist_ok=True)

    for index, scene in enumerate(manifest["scenes"], start=1):
        text = scene.get("voiceover_text")
        if not text:
            continue
        out_path = out_dir / f"{index:02d}-{scene['id']}.mp3"
        audio = elevenlabs_request(api_key, voice_id, model_id, text)
        out_path.write_bytes(audio)
        url = None if args.no_upload else upload_tmpfiles(out_path)
        if url:
            scene["voiceover_url"] = url
        print(f"{scene['id']}: {out_path.relative_to(ROOT)}")
        if url:
            print(url)

    if args.write_manifest:
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Updated manifest: {manifest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
