import argparse
import json
import os
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "outputs" / "video-manifests" / "student-ai-study-runway-clips.json"
RUNWAY_API = "https://api.dev.runwayml.com/v1"
RUNWAY_VERSION = "2024-11-06"


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
    if not value or value.startswith("your_") or "example" in value:
        return None
    return value


def runway_request(method, path, api_key, payload=None):
    body = None
    headers = {
        "authorization": f"Bearer {api_key}",
        "content-type": "application/json",
        "x-runway-version": RUNWAY_VERSION,
        "user-agent": "WhatAICanDo-Runway-Python/0.1",
    }
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    request = Request(f"{RUNWAY_API}{path}", data=body, headers=headers, method=method)
    try:
        with urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Runway request failed ({error.code}): {detail}") from error


def create_task(api_key, clip, model, ratio, duration):
    payload = {
        "model": model,
        "promptImage": clip["image_url"],
        "promptText": clip["prompt"],
        "ratio": ratio,
        "duration": duration,
    }
    return runway_request("POST", "/image_to_video", api_key, payload)


def wait_for_task(api_key, task_id, timeout_seconds=900):
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        task = runway_request("GET", f"/tasks/{task_id}", api_key)
        status = task.get("status")
        print(f"{task_id}: {status}")
        if status in {"SUCCEEDED", "FAILED", "CANCELLED"}:
            return task
        time.sleep(10)
    raise TimeoutError(f"Timed out waiting for Runway task {task_id}")


def download(url, out_path):
    request = Request(url, headers={"user-agent": "WhatAICanDo-Runway-Python/0.1"})
    with urlopen(request, timeout=300) as response:
        out_path.write_bytes(response.read())


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Generate Runway image-to-video clips from a manifest.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Path to Runway clips manifest.")
    parser.add_argument("--clip", help="Clip id to render. Defaults to the first clip.")
    parser.add_argument("--all", action="store_true", help="Render all clips in the manifest.")
    parser.add_argument("--submit", action="store_true", help="Submit to Runway. Without this, only writes request JSON.")
    parser.add_argument("--wait", action="store_true", help="Poll until finished and download video.")
    args = parser.parse_args()

    api_key = real_value(os.environ.get("RUNWAYML_API_SECRET"))
    if args.submit and not api_key:
        raise SystemExit("Missing RUNWAYML_API_SECRET in .env or environment.")

    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    clips = manifest["clips"] if args.all else [manifest["clips"][0]]
    if args.clip:
        clips = [clip for clip in manifest["clips"] if clip["id"] == args.clip]
        if not clips:
            raise SystemExit(f"Clip id not found: {args.clip}")

    out_dir = ROOT / "outputs" / "runway-clips" / manifest["id"]
    out_dir.mkdir(parents=True, exist_ok=True)

    for clip in clips:
        request_payload = {
            "model": manifest.get("model", "gen4_turbo"),
            "promptImage": clip["image_url"],
            "promptText": clip["prompt"],
            "ratio": manifest.get("ratio", "720:1280"),
            "duration": manifest.get("duration", 5),
        }
        request_path = out_dir / f"{clip['id']}.request.json"
        request_path.write_text(json.dumps(request_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote request: {request_path.relative_to(ROOT)}")

        if not args.submit:
            continue

        task = create_task(
            api_key,
            clip,
            request_payload["model"],
            request_payload["ratio"],
            request_payload["duration"],
        )
        task_path = out_dir / f"{clip['id']}.task.json"
        task_path.write_text(json.dumps(task, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        task_id = task["id"]
        print(f"Started Runway task: {task_id}")

        if args.wait:
            final_task = wait_for_task(api_key, task_id)
            final_path = out_dir / f"{clip['id']}.final.json"
            final_path.write_text(json.dumps(final_task, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            if final_task.get("status") != "SUCCEEDED":
                print(json.dumps(final_task, ensure_ascii=False, indent=2))
                continue

            output = final_task.get("output") or []
            if not output:
                print(f"No output URL returned for {clip['id']}")
                continue

            video_path = out_dir / f"{clip['id']}.mp4"
            download(output[0], video_path)
            print(f"Downloaded: {video_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
