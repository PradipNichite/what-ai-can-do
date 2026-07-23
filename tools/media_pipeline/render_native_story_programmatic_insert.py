#!/usr/bin/env python3
"""Render a style-preserving programmatic insert over a native story frame."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[2]


def resolve(path: str) -> Path:
    item = Path(path)
    if not item.is_absolute():
        item = ROOT / item
    return item


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def ease_in_out(t: float) -> float:
    t = clamp(t)
    return t * t * (3 - 2 * t)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * clamp(t)


def arrow_head(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], fill: tuple[int, int, int, int]) -> None:
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 28
    left = (end[0] - size * math.cos(angle - math.pi / 6), end[1] - size * math.sin(angle - math.pi / 6))
    right = (end[0] - size * math.cos(angle + math.pi / 6), end[1] - size * math.sin(angle + math.pi / 6))
    draw.polygon([end, left, right], fill=fill)


def draw_glow_line(
    overlay: Image.Image,
    start: tuple[float, float],
    end: tuple[float, float],
    color: tuple[int, int, int, int],
    width: int,
) -> None:
    glow = Image.new("RGBA", overlay.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.line([start, end], fill=(color[0], color[1], color[2], 80), width=width + 18)
    glow = glow.filter(ImageFilter.GaussianBlur(10))
    overlay.alpha_composite(glow)
    draw = ImageDraw.Draw(overlay)
    draw.line([start, end], fill=color, width=width)
    arrow_head(draw, start, end, color)


def draw_glow_dot(
    overlay: Image.Image,
    center: tuple[float, float],
    radius: float,
    color: tuple[int, int, int, int],
) -> None:
    glow = Image.new("RGBA", overlay.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse(
        (center[0] - radius * 2.4, center[1] - radius * 2.4, center[0] + radius * 2.4, center[1] + radius * 2.4),
        fill=(color[0], color[1], color[2], 70),
    )
    glow = glow.filter(ImageFilter.GaussianBlur(12))
    overlay.alpha_composite(glow)
    draw = ImageDraw.Draw(overlay)
    draw.ellipse(
        (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius),
        fill=color,
        outline=(255, 255, 255, 245),
        width=5,
    )


def render_frame(base: Image.Image, frame_index: int, fps: int, duration: float, spec: dict) -> Image.Image:
    t = frame_index / max(1, int(round(fps * duration)) - 1)
    image = base.copy().convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))

    old = tuple(spec["old_point"])
    new = tuple(spec["new_point"])
    control = tuple(spec.get("control_point", [(old[0] + new[0]) / 2, min(old[1], new[1]) - 70]))

    # Three readable phases: identify old point, draw exact small step, settle on new point.
    identify = ease_in_out(min(t / 0.22, 1))
    move_t = ease_in_out((t - 0.24) / 0.48)
    settle = ease_in_out((t - 0.72) / 0.18)

    pulse = 1.0 + 0.14 * math.sin(t * math.tau * 4)
    if identify > 0:
        draw_glow_dot(overlay, old, 25 * pulse * identify, (245, 116, 35, 245))

    if move_t > 0:
        # Quadratic Bezier keeps the code-controlled step visually near the generated arrow.
        p0 = old
        p1 = control
        p2 = new
        points: list[tuple[float, float]] = []
        samples = max(2, int(36 * move_t))
        for i in range(samples):
            u = i / max(1, samples - 1)
            x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u**2 * p2[0]
            y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u**2 * p2[1]
            points.append((x, y))
        draw = ImageDraw.Draw(overlay)
        for a, b in zip(points, points[1:]):
            draw.line([a, b], fill=(35, 178, 105, 235), width=9)
        if len(points) > 1:
            arrow_head(draw, points[-2], points[-1], (35, 178, 105, 235))
        current = points[-1]
        draw_glow_dot(overlay, current, 23 * pulse, (35, 178, 105, 245))

    if settle > 0.2:
        draw_glow_dot(overlay, new, 25 * pulse, (35, 178, 105, 245))

    if t > 0.62:
        # Subtle exactness cue: this is the code-controlled part, not generated text.
        draw = ImageDraw.Draw(overlay)
        box = spec.get("loss_badge_box", [592, 1048, 786, 1110])
        alpha = int(170 * settle)
        draw.rounded_rectangle(tuple(box), radius=18, fill=(22, 75, 54, alpha), outline=(255, 255, 255, int(170 * settle)), width=3)
        if settle > 0.6:
            try:
                font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
            except Exception:
                from PIL import ImageFont as _ImageFont

                font = _ImageFont.load_default()
            draw.text((box[0] + 18, box[1] + 14), "loss lower", fill=(255, 255, 255, 235), font=font)

    image.alpha_composite(overlay)
    return image.convert("RGB")


def render(spec: dict, out_path: Path) -> None:
    base = Image.open(resolve(spec["source_frame"])).convert("RGB")
    target_size = spec.get("output_size")
    if target_size:
        target_w, target_h = int(target_size[0]), int(target_size[1])
        src_w, src_h = base.size
        scale = max(target_w / src_w, target_h / src_h)
        resized = base.resize((int(round(src_w * scale)), int(round(src_h * scale))), Image.Resampling.LANCZOS)
        offset_x = max(0, (resized.width - target_w) / 2)
        offset_y = max(0, (resized.height - target_h) / 2)
        base = resized.crop((int(round(offset_x)), int(round(offset_y)), int(round(offset_x + target_w)), int(round(offset_y + target_h))))

        def map_point(point: list[float]) -> list[float]:
            return [point[0] * scale - offset_x, point[1] * scale - offset_y]

        spec = dict(spec)
        spec["old_point"] = map_point(spec["old_point"])
        spec["new_point"] = map_point(spec["new_point"])
        if spec.get("control_point"):
            spec["control_point"] = map_point(spec["control_point"])
        if spec.get("loss_badge_box"):
            box = spec["loss_badge_box"]
            spec["loss_badge_box"] = [
                box[0] * scale - offset_x,
                box[1] * scale - offset_y,
                box[2] * scale - offset_x,
                box[3] * scale - offset_y,
            ]
    fps = int(spec.get("fps", 30))
    duration = float(spec.get("duration", 5))
    total_frames = int(round(fps * duration))
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with imageio.get_writer(str(out_path), fps=fps, codec="libx264", quality=8, macro_block_size=8) as writer:
        for frame_index in range(total_frames):
            frame = render_frame(base, frame_index, fps, duration, spec)
            writer.append_data(np.asarray(frame))


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a native-story programmatic insert.")
    parser.add_argument("--spec", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    spec_path = resolve(args.spec)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    render(spec, resolve(args.out))
    print(Path(args.out))


if __name__ == "__main__":
    from PIL import ImageFont

    main()
