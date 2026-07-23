#!/usr/bin/env python3
"""Upload local media files to tmpfiles.org and print direct download URLs."""

from __future__ import annotations

import argparse
import json
import mimetypes
from pathlib import Path
from urllib.request import Request, urlopen


def upload_tmpfiles(path: Path) -> str:
    boundary = "----codex-boundary"
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = path.read_bytes()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")

    request = Request(
        "https://tmpfiles.org/api/v1/upload",
        data=body,
        headers={
            "content-type": f"multipart/form-data; boundary={boundary}",
            "user-agent": "WhatAICanDo-Media-Pipeline/0.1",
            "accept": "application/json",
        },
        method="POST",
    )
    with urlopen(request, timeout=180) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result["data"]["url"].replace("https://tmpfiles.org/", "https://tmpfiles.org/dl/")


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload files to tmpfiles.org.")
    parser.add_argument("paths", nargs="+", help="Files to upload.")
    parser.add_argument("--json-out", help="Optional output JSON mapping file names to URLs.")
    args = parser.parse_args()

    urls: dict[str, str] = {}
    for item in args.paths:
        path = Path(item).resolve()
        url = upload_tmpfiles(path)
        urls[path.name] = url
        print(f"{path.name}: {url}")

    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(urls, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
