#!/usr/bin/env python3
"""Render a local vertical video edit from approved image frames and clips."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import imageio.v2 as imageio
import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]


def resolve(path: str) -> Path:
    item = Path(path)
    if not item.is_absolute():
        item = ROOT / item
    return item


def cover_image(image: Image.Image, size: tuple[int, int], scale: float = 1.0) -> Image.Image:
    target_w, target_h = size
    src_w, src_h = image.size
    factor = max(target_w / src_w, target_h / src_h) * scale
    new_size = (int(round(src_w * factor)), int(round(src_h * factor)))
    resized = image.resize(new_size, Image.Resampling.LANCZOS)
    left = max(0, (resized.width - target_w) // 2)
    top = max(0, (resized.height - target_h) // 2)
    return resized.crop((left, top, left + target_w, top + target_h)).convert("RGB")


def image_scene_frames(scene: dict[str, Any], fps: int, size: tuple[int, int]) -> list[np.ndarray]:
    image = Image.open(resolve(scene["path"])).convert("RGB")
    duration = float(scene["duration"])
    frame_count = int(round(duration * fps))
    zoom = float(scene.get("zoom", 0.025))
    frames = []
    for index in range(frame_count):
        t = index / max(1, frame_count - 1)
        scale = 1.0 + zoom * t
        frames.append(np.asarray(cover_image(image, size, scale)))
    return frames


def clip_scene_frames(scene: dict[str, Any], fps: int, size: tuple[int, int]) -> list[np.ndarray]:
    clip_path = resolve(scene["path"])
    reader = imageio.get_reader(str(clip_path))
    meta = reader.get_meta_data()
    clip_fps = float(meta.get("fps", fps) or fps)
    duration = float(scene.get("duration", meta.get("duration", 0) or 0))
    frame_count = int(round(duration * fps))
    frames: list[np.ndarray] = []
    try:
        for index in range(frame_count):
            source_index = int(round(index * clip_fps / fps))
            try:
                frame = reader.get_data(source_index)
            except IndexError:
                break
            image = Image.fromarray(frame).convert("RGB")
            frames.append(np.asarray(cover_image(image, size, 1.0)))
    finally:
        reader.close()

    if not frames:
        raise ValueError(f"No frames read from {clip_path}")
    while len(frames) < frame_count:
        frames.append(frames[-1])
    return frames[:frame_count]


def render(manifest: dict[str, Any], out_path: Path) -> None:
    fps = int(manifest.get("fps", 24))
    width = int(manifest.get("width", 720))
    height = int(manifest.get("height", 1280))
    size = (width, height)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with imageio.get_writer(str(out_path), fps=fps, codec="libx264", quality=8, macro_block_size=8) as writer:
        for scene in manifest["scenes"]:
            kind = scene.get("type", "image")
            frames = clip_scene_frames(scene, fps, size) if kind == "clip" else image_scene_frames(scene, fps, size)
            for frame in frames:
                writer.append_data(frame)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a local vertical edit from approved frames and clips.")
    parser.add_argument("--manifest", required=True, help="Path to edit manifest JSON.")
    parser.add_argument("--out", required=True, help="Output MP4 path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_path = resolve(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    out_path = resolve(args.out)
    render(manifest, out_path)
    print(out_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
