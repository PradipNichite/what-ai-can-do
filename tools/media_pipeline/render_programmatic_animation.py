#!/usr/bin/env python3
"""Render deterministic educational animations from a small JSON spec.

This is intentionally lightweight: it gives the project a programmatic motion
lane before committing to a larger Remotion/Motion Canvas/Revideo backend.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Canvas:
    width: int
    height: int
    margin: int
    graph_left: int
    graph_top: int
    graph_right: int
    graph_bottom: int


def ease_in_out(t: float) -> float:
    t = clamp(t)
    return t * t * (3 - 2 * t)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def lerp(start: float, end: float, t: float) -> float:
    return start + (end - start) * clamp(t)


def phase_progress(time_s: float, start: float, end: float) -> float:
    if end <= start:
        return 1.0
    return clamp((time_s - start) / (end - start))


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    font_dir = Path("C:/Windows/Fonts")
    candidates = [
        font_dir / ("arialbd.ttf" if bold else "arial.ttf"),
        font_dir / ("segoeuib.ttf" if bold else "segoeui.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


FONTS = {
    "mega": load_font(74, bold=True),
    "hero": load_font(60, bold=True),
    "title": load_font(42, bold=True),
    "caption": load_font(38, bold=True),
    "body": load_font(32),
    "body_bold": load_font(32, bold=True),
    "small": load_font(25),
    "tiny": load_font(21),
}


def rounded_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_center(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, font: ImageFont.ImageFont, fill: str) -> None:
    box = draw.textbbox((0, 0), text, font=font)
    x = xy[0] - (box[2] - box[0]) / 2
    y = xy[1] - (box[3] - box[1]) / 2
    draw.text((x, y), text, font=font, fill=fill)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = " ".join([*current, word])
        box = draw.textbbox((0, 0), candidate, font=font)
        if current and box[2] - box[0] > max_width:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def draw_wrapped_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: str,
    max_width: int,
    line_gap: int = 8,
) -> None:
    y = xy[1]
    for line in wrap_text(draw, text, font, max_width):
        draw.text((xy[0], y), line, font=font, fill=fill)
        box = draw.textbbox((0, 0), line, font=font)
        y += box[3] - box[1] + line_gap


def draw_arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    fill: str,
    width: int = 10,
    head: int = 28,
) -> None:
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    left = (end[0] - head * math.cos(angle - math.pi / 6), end[1] - head * math.sin(angle - math.pi / 6))
    right = (end[0] - head * math.cos(angle + math.pi / 6), end[1] - head * math.sin(angle + math.pi / 6))
    draw.polygon([end, left, right], fill=fill)


def loss_value(x: float, minimum: float, base_loss: float) -> float:
    return base_loss + (x - minimum) ** 2


def graph_point(canvas: Canvas, x: float, y: float, x_min: float, x_max: float, y_min: float, y_max: float) -> tuple[float, float]:
    gx = canvas.graph_left + (x - x_min) / (x_max - x_min) * (canvas.graph_right - canvas.graph_left)
    gy = canvas.graph_bottom - (y - y_min) / (y_max - y_min) * (canvas.graph_bottom - canvas.graph_top)
    return gx, gy


def draw_background(draw: ImageDraw.ImageDraw, canvas: Canvas) -> None:
    draw.rectangle((0, 0, canvas.width, canvas.height), fill="#f7efe4")
    draw.ellipse((-260, -180, 360, 420), fill="#f0c87d")
    draw.ellipse((760, 1460, 1280, 2030), fill="#8bc2b2")
    rounded_rect(draw, (58, 128, canvas.width - 58, canvas.height - 92), 42, "#fffaf2", "#dec9aa", 3)


def draw_header(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    title = spec["title"]
    subtitle = spec.get("subtitle", "")
    draw.text((96, 182), title, font=FONTS["hero"], fill="#22252a")
    draw.text((100, 260), subtitle, font=FONTS["body"], fill="#5d6570")
    rounded_rect(draw, (96, 330, canvas.width - 96, 402), 26, "#e7f3ef", None)
    label = "Programmatic animation: the dot, arrows, and loss score are code-controlled"
    draw.text((128, 350), label, font=FONTS["small"], fill="#276257")
    if time_s < 1.0:
        alpha_bar = int(270 * ease_in_out(time_s))
        draw.line((100, 424, 100 + alpha_bar, 424), fill="#f28c38", width=8)


def draw_micro_header(draw: ImageDraw.ImageDraw, title: str, subtitle: str, canvas: Canvas) -> None:
    draw.text((92, 168), title, font=FONTS["hero"], fill="#22252a")
    draw_wrapped_text(draw, (96, 248), subtitle, FONTS["body"], "#5d6570", canvas.width - 192, 8)


def draw_caption_panel(draw: ImageDraw.ImageDraw, canvas: Canvas, text: str, y: int = 1540) -> None:
    box = (90, y, canvas.width - 90, y + 170)
    rounded_rect(draw, box, 30, "#26313a", None)
    draw_wrapped_text(draw, (128, y + 36), text, FONTS["caption"], "#ffffff", canvas.width - 256, 10)


def draw_value_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    value: str,
    accent: str,
) -> None:
    rounded_rect(draw, box, 28, "#ffffff", "#ddc39d", 3)
    draw.text((box[0] + 30, box[1] + 28), title, font=FONTS["body_bold"], fill="#2a3038")
    draw.text((box[0] + 30, box[1] + 86), value, font=FONTS["hero"], fill=accent)


def draw_complete_opener_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    draw_micro_header(draw, "Gradient Descent In AI", "How slope helps a model reduce error", canvas)
    rounded_rect(draw, (104, 430, canvas.width - 104, 690), 36, "#ffffff", "#ddc39d", 3)
    draw.text((144, 474), "School math clue", font=FONTS["body_bold"], fill="#2a3038")
    draw.text((144, 536), "slope on a graph", font=FONTS["hero"], fill="#2f6f93")
    rounded_rect(draw, (104, 760, canvas.width - 104, 1060), 36, "#26313a", None)
    draw.text((144, 808), "AI training job", font=FONTS["body_bold"], fill="#ffffff")
    draw_wrapped_text(draw, (144, 872), "Use that slope clue to make wrong predictions less wrong.", FONTS["caption"], "#ffffff", canvas.width - 288, 12)
    draw_caption_panel(draw, canvas, "In this short, one cat/dog mistake becomes a lower loss.", 1430)


def draw_intro_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    draw_micro_header(draw, "Gradient Descent", "How AI learns from a mistake", canvas)
    draw_value_card(draw, (100, 470, 480, 690), "model says", "dog", "#ce4b3d")
    draw_value_card(draw, (600, 470, 980, 690), "correct answer", "cat", "#2b7d5a")
    gap_t = ease_in_out(phase_progress(time_s, 0.65, 1.4))
    draw_arrow(draw, (490, 580), (lerp(500, 590, gap_t), 580), "#f28c38", width=9, head=26)
    text_center(draw, (540, 520), "mistake", FONTS["body_bold"], "#8a5a1e")
    loss_y = int(lerp(1120, 830, ease_in_out(phase_progress(time_s, 1.1, 2.1))))
    rounded_rect(draw, (170, loss_y, 910, loss_y + 190), 34, "#26313a", None)
    draw.text((220, loss_y + 36), "loss score", font=FONTS["body_bold"], fill="#ffffff")
    rounded_rect(draw, (220, loss_y + 112, 720, loss_y + 148), 18, "#59626b", None)
    rounded_rect(draw, (220, loss_y + 112, 660, loss_y + 148), 18, "#f06b55", None)
    draw.text((750, loss_y + 82), "8/10", font=FONTS["hero"], fill="#ffffff")
    draw_caption_panel(draw, canvas, "The loss score tells AI how wrong it was.", 1430)


def draw_setting_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    draw_micro_header(draw, "What can the model change?", "Not the answer directly: it changes a setting.", canvas)
    rounded_rect(draw, (110, 500, canvas.width - 110, 850), 36, "#ffffff", "#ddc39d", 3)
    draw.text((154, 558), "current weight", font=FONTS["body_bold"], fill="#2a3038")
    bar = (154, 690, canvas.width - 154, 738)
    rounded_rect(draw, bar, 24, "#dde3e4", None)
    fill_right = int(lerp(bar[0], bar[2] - 200, ease_in_out(phase_progress(time_s, 0.4, 1.6))))
    rounded_rect(draw, (bar[0], bar[1], fill_right, bar[3]), 24, "#f0a04b", None)
    draw.ellipse((fill_right - 34, bar[1] - 24, fill_right + 34, bar[3] + 24), fill="#f05f45", outline="#ffffff", width=5)
    draw.text((154, 778), "too low -> high loss", font=FONTS["caption"], fill="#ce4b3d")
    rounded_rect(draw, (160, 990, 920, 1250), 36, "#e7f3ef", None)
    draw_wrapped_text(draw, (210, 1044), "Training asks: which small change makes loss lower?", FONTS["caption"], "#24594f", 640, 12)
    draw_caption_panel(draw, canvas, "Gradient descent is the rule for choosing that small change.", 1450)


def draw_bridge_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    draw_micro_header(draw, "Now AI needs a better setting", "Think of every setting as a point on a loss curve.", canvas)
    curve = spec["curve"]
    x_min, x_max = curve["x_range"]
    y_min, y_max = curve["y_range"]
    minimum = curve["minimum"]
    base_loss = curve["base_loss"]
    bridge_canvas = Canvas(canvas.width, canvas.height, canvas.margin, 150, 520, canvas.width - 150, 1280)
    rounded_rect(draw, (110, 450, canvas.width - 110, 1360), 38, "#fdf8ef", "#dac29a", 3)
    draw.line((bridge_canvas.graph_left, bridge_canvas.graph_bottom, bridge_canvas.graph_right, bridge_canvas.graph_bottom), fill="#9b8565", width=6)
    draw.line((bridge_canvas.graph_left, bridge_canvas.graph_bottom, bridge_canvas.graph_left, bridge_canvas.graph_top), fill="#9b8565", width=6)
    curve_points = []
    for idx in range(160):
        x = x_min + (x_max - x_min) * idx / 159
        y = loss_value(x, minimum, base_loss)
        curve_points.append(graph_point(bridge_canvas, x, y, x_min, x_max, y_min, y_max))
    draw.line(curve_points, fill="#2f6f93", width=12, joint="curve")
    start = graph_point(bridge_canvas, -1.85, loss_value(-1.85, minimum, base_loss), x_min, x_max, y_min, y_max)
    target = graph_point(bridge_canvas, minimum, base_loss, x_min, x_max, y_min, y_max)
    draw.ellipse((start[0] - 26, start[1] - 26, start[0] + 26, start[1] + 26), fill="#f05f45", outline="#ffffff", width=5)
    draw.ellipse((target[0] - 22, target[1] - 22, target[0] + 22, target[1] + 22), fill="#45ad7d", outline="#ffffff", width=5)
    text_center(draw, (start[0] + 80, start[1] - 42), "high loss", FONTS["body_bold"], "#ce4b3d")
    text_center(draw, (target[0], target[1] + 70), "low loss", FONTS["body_bold"], "#276257")
    draw_caption_panel(draw, canvas, "Learning means moving toward lower loss.", 1460)


def draw_repeat_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    draw_micro_header(draw, "Training repeats the loop", "One update helps. Many updates train the model.", canvas)
    cards = [
        ("start", "loss 8/10", "#f06b55"),
        ("after steps", "loss 5/10", "#f0a04b"),
        ("later", "loss 3/10", "#45ad7d"),
    ]
    y = 500
    reveal = ease_in_out(phase_progress(time_s, 0.2, 2.2))
    count = max(1, min(3, int(math.ceil(reveal * 3))))
    for idx, (label, value, color) in enumerate(cards[:count]):
        rounded_rect(draw, (120, y, canvas.width - 120, y + 190), 34, "#ffffff", "#ddc39d", 3)
        draw.text((160, y + 36), label, font=FONTS["body_bold"], fill="#5d6570")
        draw.text((160, y + 92), value, font=FONTS["hero"], fill=color)
        if idx < count - 1:
            draw_arrow(draw, (canvas.width - 250, y + 96), (canvas.width - 160, y + 96), "#2f6f93", width=8, head=22)
        y += 250
    rounded_rect(draw, (120, 1310, canvas.width - 120, 1510), 34, "#26313a", None)
    draw_wrapped_text(draw, (164, 1360), "Same rule, repeated on many training examples.", FONTS["caption"], "#ffffff", canvas.width - 328, 10)
    draw_caption_panel(draw, canvas, "Lower training loss means the model fits these examples better.", 1625)


def draw_recap_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas) -> None:
    draw_micro_header(draw, "What gradient descent does", "A tiny rule turns mistakes into improvement.", canvas)
    items = [
        ("1", "Measure the loss"),
        ("2", "Find the uphill direction"),
        ("3", "Take a small step the other way"),
    ]
    y = 560
    for number, text in items:
        rounded_rect(draw, (112, y, canvas.width - 112, y + 190), 34, "#ffffff", "#ddc39d", 3)
        draw.ellipse((154, y + 44, 254, y + 144), fill="#2f6f93")
        text_center(draw, (204, y + 94), number, FONTS["title"], "#ffffff")
        draw.text((292, y + 62), text, font=FONTS["caption"], fill="#2a3038")
        y += 240
    draw_caption_panel(draw, canvas, "Same idea, repeated many times: lower error.", 1490)


def draw_complete_takeaway_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas) -> None:
    draw_micro_header(draw, "Remember", "Gradient descent is not a magic jump.", canvas)
    rounded_rect(draw, (108, 500, canvas.width - 108, 840), 40, "#ffffff", "#ddc39d", 3)
    draw_wrapped_text(draw, (152, 560), "It measures error, reads the local slope, then takes a small downhill step.", FONTS["caption"], "#2a3038", canvas.width - 304, 12)
    rounded_rect(draw, (108, 940, canvas.width - 108, 1240), 40, "#e7f3ef", None)
    draw.text((152, 1000), "Memory anchor", font=FONTS["body_bold"], fill="#276257")
    draw_wrapped_text(draw, (152, 1064), "AI learns by taking repeated small steps on an error curve.", FONTS["caption"], "#24594f", canvas.width - 304, 12)
    draw_caption_panel(draw, canvas, "If the next loss is lower, the update helped.", 1465)


def draw_scene_chip(draw: ImageDraw.ImageDraw, canvas: Canvas, label: str) -> None:
    box = (canvas.width - 260, 164, canvas.width - 96, 224)
    rounded_rect(draw, box, 22, "#e7f3ef", None)
    text_center(draw, ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), label, FONTS["small"], "#276257")


def draw_comparison_scene_caption(draw: ImageDraw.ImageDraw, canvas: Canvas, text: str) -> None:
    draw_caption_panel(draw, canvas, text, 1738)


def draw_loss_meter(draw: ImageDraw.ImageDraw, canvas: Canvas, current_loss: float, initial_loss: float) -> None:
    box = (100, 1450, canvas.width - 100, 1614)
    rounded_rect(draw, box, 30, "#26313a", None)
    draw.text((136, 1482), "loss score", font=FONTS["body_bold"], fill="#ffffff")
    meter = (136, 1548, canvas.width - 230, 1584)
    rounded_rect(draw, meter, 18, "#59626b", None)
    fill_ratio = clamp((current_loss - 0.18) / max(initial_loss - 0.18, 0.01))
    fill_right = int(lerp(meter[0], meter[2], fill_ratio))
    color = "#f06b55" if fill_ratio > 0.55 else "#45ad7d"
    rounded_rect(draw, (meter[0], meter[1], fill_right, meter[3]), 18, color, None)
    draw.text((canvas.width - 196, 1530), f"{current_loss:.2f}", font=FONTS["title"], fill="#ffffff")


def draw_equation_chip(draw: ImageDraw.ImageDraw, canvas: Canvas, weight: float, step_index: int) -> None:
    chip = (100, 1644, canvas.width - 100, 1734)
    rounded_rect(draw, chip, 28, "#ffffff", "#ddc39d", 3)
    draw.text((132, 1672), f"step {step_index}: weight = {weight:+.2f}", font=FONTS["body_bold"], fill="#2a3038")
    draw.text((604, 1676), "update moves opposite", font=FONTS["small"], fill="#6c5b3d")


def draw_curve_scene(draw: ImageDraw.ImageDraw, spec: dict[str, Any], canvas: Canvas, time_s: float) -> None:
    curve = spec["curve"]
    x_min, x_max = curve["x_range"]
    y_min, y_max = curve["y_range"]
    minimum = curve["minimum"]
    base_loss = curve["base_loss"]
    points = [float(x) for x in spec["steps"]]
    start_x = points[0]
    reveal_curve = ease_in_out(phase_progress(time_s, 1.05, 2.15))
    step_t = ease_in_out(phase_progress(time_s, 2.15, 6.45))
    exact = step_t * (len(points) - 1)
    left_i = min(int(math.floor(exact)), len(points) - 2)
    local_t = exact - left_i
    current_x = lerp(points[left_i], points[left_i + 1], ease_in_out(local_t))
    current_y = loss_value(current_x, minimum, base_loss)
    current_loss = current_y
    initial_loss = loss_value(start_x, minimum, base_loss)

    graph_box = (canvas.graph_left, canvas.graph_top, canvas.graph_right, canvas.graph_bottom)
    rounded_rect(draw, (graph_box[0] - 32, graph_box[1] - 44, graph_box[2] + 32, graph_box[3] + 44), 34, "#fdf8ef", "#dac29a", 3)
    draw.line((canvas.graph_left, canvas.graph_bottom, canvas.graph_right, canvas.graph_bottom), fill="#9b8565", width=5)
    draw.line((canvas.graph_left, canvas.graph_bottom, canvas.graph_left, canvas.graph_top), fill="#9b8565", width=5)
    draw.text((canvas.graph_left + 8, canvas.graph_top - 36), "loss", font=FONTS["small"], fill="#5b4c37")
    draw.text((canvas.graph_right - 132, canvas.graph_bottom + 16), "weight", font=FONTS["small"], fill="#5b4c37")

    samples = 180
    visible_samples = max(2, int(samples * reveal_curve))
    curve_points: list[tuple[float, float]] = []
    for idx in range(visible_samples):
        x = x_min + (x_max - x_min) * idx / (samples - 1)
        y = loss_value(x, minimum, base_loss)
        curve_points.append(graph_point(canvas, x, y, x_min, x_max, y_min, y_max))
    if len(curve_points) > 1:
        draw.line(curve_points, fill="#2f6f93", width=10, joint="curve")

    min_point = graph_point(canvas, minimum, base_loss, x_min, x_max, y_min, y_max)
    draw.ellipse((min_point[0] - 12, min_point[1] - 12, min_point[0] + 12, min_point[1] + 12), fill="#45ad7d")
    text_center(draw, (min_point[0], min_point[1] + 48), "lowest loss", FONTS["tiny"], "#276257")

    trail_count = min(left_i + 1, len(points))
    for idx in range(trail_count):
        px = points[idx]
        py = loss_value(px, minimum, base_loss)
        gx, gy = graph_point(canvas, px, py, x_min, x_max, y_min, y_max)
        draw.ellipse((gx - 10, gy - 10, gx + 10, gy + 10), fill="#f28c38")
        if idx > 0:
            prev_x = points[idx - 1]
            prev_y = loss_value(prev_x, minimum, base_loss)
            prev = graph_point(canvas, prev_x, prev_y, x_min, x_max, y_min, y_max)
            draw.line((prev[0], prev[1], gx, gy), fill="#f0a04b", width=5)

    current = graph_point(canvas, current_x, current_y, x_min, x_max, y_min, y_max)
    pulse = 1 + 0.12 * math.sin(time_s * 2 * math.pi * 2)
    radius = 24 * pulse
    draw.ellipse((current[0] - radius, current[1] - radius, current[0] + radius, current[1] + radius), fill="#f05f45", outline="#ffffff", width=5)

    slope = 2 * (current_x - minimum)
    if reveal_curve > 0.35:
        tangent_dx = 0.28
        tangent_start = graph_point(canvas, current_x - tangent_dx, current_y - slope * tangent_dx, x_min, x_max, y_min, y_max)
        tangent_end = graph_point(canvas, current_x + tangent_dx, current_y + slope * tangent_dx, x_min, x_max, y_min, y_max)
        tangent_start = (
            clamp(tangent_start[0], canvas.graph_left, canvas.graph_right),
            clamp(tangent_start[1], canvas.graph_top, canvas.graph_bottom),
        )
        tangent_end = (
            clamp(tangent_end[0], canvas.graph_left, canvas.graph_right),
            clamp(tangent_end[1], canvas.graph_top, canvas.graph_bottom),
        )
        draw.line((tangent_start[0], tangent_start[1], tangent_end[0], tangent_end[1]), fill="#ce4b3d", width=7)
        draw.text((canvas.graph_left + 34, canvas.graph_top + 28), "gradient points uphill", font=FONTS["body_bold"], fill="#ce4b3d")

    next_index = min(left_i + 1, len(points) - 1)
    next_x = points[next_index]
    next_y = loss_value(next_x, minimum, base_loss)
    next_point = graph_point(canvas, next_x, next_y, x_min, x_max, y_min, y_max)
    arrow_reveal = ease_in_out(phase_progress(time_s, 2.6, 3.25))
    arrow_end = (lerp(current[0], next_point[0], arrow_reveal), lerp(current[1], next_point[1], arrow_reveal))
    if reveal_curve > 0.45:
        draw_arrow(draw, current, arrow_end, "#45ad7d", width=9, head=24)
        draw.text((canvas.graph_right - 360, canvas.graph_top + 82), "move opposite", font=FONTS["body_bold"], fill="#2b7d5a")

    if time_s >= 6.05:
        warning_t = ease_in_out(phase_progress(time_s, 6.05, 7.25))
        overshoot_start = graph_point(canvas, -0.18, loss_value(-0.18, minimum, base_loss), x_min, x_max, y_min, y_max)
        overshoot_end = graph_point(canvas, 1.15, loss_value(1.15, minimum, base_loss), x_min, x_max, y_min, y_max)
        warning_end = (lerp(overshoot_start[0], overshoot_end[0], warning_t), lerp(overshoot_start[1], overshoot_end[1], warning_t))
        draw_arrow(draw, overshoot_start, warning_end, "#b55fbd", width=7, head=22)
        rounded_rect(draw, (canvas.graph_left + 220, canvas.graph_bottom - 108, canvas.graph_right - 40, canvas.graph_bottom - 38), 22, "#f4e7f6", None)
        draw.text((canvas.graph_left + 250, canvas.graph_bottom - 92), "too big a step can overshoot", font=FONTS["small"], fill="#7b3f83")

    draw_loss_meter(draw, canvas, current_loss, initial_loss)
    draw_equation_chip(draw, canvas, current_x, left_i + 1)


def render_gradient_descent_frame(spec: dict[str, Any], frame: int) -> Image.Image:
    width = int(spec["canvas"]["width"])
    height = int(spec["canvas"]["height"])
    fps = int(spec["fps"])
    time_s = frame / fps
    canvas = Canvas(
        width=width,
        height=height,
        margin=80,
        graph_left=142,
        graph_top=520,
        graph_right=width - 142,
        graph_bottom=1360,
    )
    image = Image.new("RGB", (width, height), "#f7efe4")
    draw = ImageDraw.Draw(image)
    draw_background(draw, canvas)
    draw_header(draw, spec, canvas, time_s)
    draw_curve_scene(draw, spec, canvas, time_s)
    footer = spec.get("footer", "A small coded step can make the model less wrong.")
    draw_wrapped_text(draw, (100, height - 156), footer, FONTS["body"], "#4c5960", width - 200)
    return image


def render_gradient_descent_micro_lesson_frame(spec: dict[str, Any], frame: int) -> Image.Image:
    width = int(spec["canvas"]["width"])
    height = int(spec["canvas"]["height"])
    fps = int(spec["fps"])
    time_s = frame / fps
    canvas = Canvas(
        width=width,
        height=height,
        margin=80,
        graph_left=142,
        graph_top=500,
        graph_right=width - 142,
        graph_bottom=1328,
    )
    image = Image.new("RGB", (width, height), "#f7efe4")
    draw = ImageDraw.Draw(image)
    draw_background(draw, canvas)

    if time_s < 3.4:
        draw_intro_scene(draw, spec, canvas, time_s)
    elif time_s < 6.0:
        draw_bridge_scene(draw, spec, canvas, time_s - 3.4)
    elif time_s < 15.2:
        draw_micro_header(draw, "Follow one update", "The dot steps down the curve as loss decreases.", canvas)
        draw_curve_scene(draw, spec, canvas, time_s - 6.0)
    elif time_s < 17.4:
        draw_micro_header(draw, "Step size matters", "A step that is too large can jump past the low point.", canvas)
        draw_curve_scene(draw, spec, canvas, 7.25)
    else:
        draw_recap_scene(draw, spec, canvas)
    return image


def scene_at_time(spec: dict[str, Any], time_s: float) -> dict[str, Any]:
    scenes = spec.get("scene_timing", [])
    for scene in scenes:
        if float(scene["start"]) <= time_s < float(scene["end"]):
            return scene
    if scenes:
        return scenes[-1]
    return {"id": "recap", "start": 0, "end": spec["duration_seconds"], "title": "Recap", "subtitle": "", "caption": ""}


def render_gradient_descent_classifier_short_frame(spec: dict[str, Any], frame: int) -> Image.Image:
    width = int(spec["canvas"]["width"])
    height = int(spec["canvas"]["height"])
    fps = int(spec["fps"])
    time_s = frame / fps
    canvas = Canvas(
        width=width,
        height=height,
        margin=80,
        graph_left=142,
        graph_top=500,
        graph_right=width - 142,
        graph_bottom=1328,
    )
    image = Image.new("RGB", (width, height), "#f7efe4")
    draw = ImageDraw.Draw(image)
    draw_background(draw, canvas)

    scene = scene_at_time(spec, time_s)
    scene_id = scene["id"]
    local_t = time_s - float(scene["start"])
    title = scene.get("title", "Gradient Descent")
    subtitle = scene.get("subtitle", "")
    caption = scene.get("caption", "")
    chip = scene.get("chip", "")

    if scene_id == "wrong_prediction":
        draw_intro_scene(draw, spec, canvas, local_t)
        if caption:
            draw_caption_panel(draw, canvas, caption, 1430)
    elif scene_id == "measure_loss":
        draw_intro_scene(draw, spec, canvas, 2.7)
        if caption:
            draw_caption_panel(draw, canvas, caption, 1430)
    elif scene_id == "loss_curve":
        draw_bridge_scene(draw, spec, canvas, local_t + 0.4)
        if caption:
            draw_caption_panel(draw, canvas, caption, 1460)
    elif scene_id == "gradient_direction":
        draw_micro_header(draw, title, subtitle, canvas)
        draw_curve_scene(draw, spec, canvas, 2.75)
        if caption:
            draw_comparison_scene_caption(draw, canvas, caption)
    elif scene_id == "small_update":
        draw_micro_header(draw, title, subtitle, canvas)
        draw_curve_scene(draw, spec, canvas, 3.0 + local_t)
        if caption:
            draw_comparison_scene_caption(draw, canvas, caption)
    elif scene_id == "lower_loss":
        draw_micro_header(draw, title, subtitle, canvas)
        draw_curve_scene(draw, spec, canvas, 5.1)
        if caption:
            draw_comparison_scene_caption(draw, canvas, caption)
    elif scene_id == "repeat":
        draw_micro_header(draw, title, subtitle, canvas)
        draw_curve_scene(draw, spec, canvas, 4.2 + local_t * 0.9)
        if caption:
            draw_comparison_scene_caption(draw, canvas, caption)
    elif scene_id == "quick_check":
        draw_micro_header(draw, title, subtitle, canvas)
        draw_curve_scene(draw, spec, canvas, 7.25)
        if caption:
            draw_comparison_scene_caption(draw, canvas, caption)
    else:
        draw_recap_scene(draw, spec, canvas)

    if chip:
        draw_scene_chip(draw, canvas, chip)
    return image


def render_gradient_descent_complete_short_frame(spec: dict[str, Any], frame: int) -> Image.Image:
    width = int(spec["canvas"]["width"])
    height = int(spec["canvas"]["height"])
    fps = int(spec["fps"])
    time_s = frame / fps
    canvas = Canvas(
        width=width,
        height=height,
        margin=80,
        graph_left=142,
        graph_top=500,
        graph_right=width - 142,
        graph_bottom=1328,
    )
    image = Image.new("RGB", (width, height), "#f7efe4")
    draw = ImageDraw.Draw(image)
    draw_background(draw, canvas)

    scene = scene_at_time(spec, time_s)
    scene_id = scene["id"]
    local_t = time_s - float(scene["start"])
    if scene_id == "opener":
        draw_complete_opener_scene(draw, spec, canvas, local_t)
    elif scene_id == "mistake":
        draw_intro_scene(draw, spec, canvas, min(local_t, 2.8))
    elif scene_id == "setting":
        draw_setting_scene(draw, spec, canvas, local_t)
    elif scene_id == "mechanism":
        draw_micro_header(draw, "The setting moves downhill", "The dot moves opposite the uphill gradient.", canvas)
        draw_curve_scene(draw, spec, canvas, 1.8 + local_t * 0.72)
        draw_caption_panel(draw, canvas, "This is the mechanism: slope direction controls the update.", 1738)
    elif scene_id == "repeat":
        draw_repeat_scene(draw, spec, canvas, local_t)
    elif scene_id == "step_size":
        draw_micro_header(draw, "Why not one huge jump?", "A too-large step can cross the low-loss region.", canvas)
        draw_curve_scene(draw, spec, canvas, 7.25)
        draw_caption_panel(draw, canvas, "Step size matters because overshooting can raise loss again.", 1738)
    else:
        draw_complete_takeaway_scene(draw, spec, canvas)
    return image


def resolve_backend(spec: dict[str, Any], cli_backend: str) -> str:
    if cli_backend != "auto":
        return cli_backend
    return str(spec.get("animation_backend", "pillow"))


def render(
    spec: dict[str, Any],
    out_path: Path,
    poster_path: Path | None,
    report_path: Path | None,
    backend: str,
) -> None:
    if backend != "pillow":
        raise ValueError(
            f"Unsupported animation backend '{backend}'. "
            "This prototype currently implements 'pillow'; keep the backend field so "
            "future Motion Canvas, Revideo, Remotion, or Manim renderers can share the same spec contract."
        )

    fps = int(spec["fps"])
    duration = float(spec["duration_seconds"])
    total_frames = int(round(duration * fps))
    renderer = spec["renderer"]
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with imageio.get_writer(str(out_path), fps=fps, codec="libx264", quality=8, macro_block_size=8) as writer:
        for frame in range(total_frames):
            if renderer == "gradient_descent_curve":
                image = render_gradient_descent_frame(spec, frame)
            elif renderer == "gradient_descent_micro_lesson":
                image = render_gradient_descent_micro_lesson_frame(spec, frame)
            elif renderer == "gradient_descent_classifier_short":
                image = render_gradient_descent_classifier_short_frame(spec, frame)
            elif renderer == "gradient_descent_complete_short":
                image = render_gradient_descent_complete_short_frame(spec, frame)
            else:
                raise ValueError(f"Unsupported renderer: {renderer}")
            if frame == 0 and poster_path is not None:
                poster_path.parent.mkdir(parents=True, exist_ok=True)
                image.save(poster_path)
            writer.append_data(np.asarray(image))

    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report = {
            "spec": spec.get("id"),
            "renderer": renderer,
            "animation_backend": backend,
            "video": str(out_path),
            "poster": str(poster_path) if poster_path else None,
            "fps": fps,
            "duration_seconds": duration,
            "frames": total_frames,
            "resolution": [int(spec["canvas"]["width"]), int(spec["canvas"]["height"])],
        }
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a programmatic educational animation.")
    parser.add_argument("--spec", required=True, help="Path to animation JSON spec.")
    parser.add_argument("--out", required=True, help="Output MP4 path.")
    parser.add_argument("--poster", help="Optional poster PNG path.")
    parser.add_argument("--report", help="Optional render report JSON path.")
    parser.add_argument(
        "--backend",
        default="auto",
        choices=["auto", "pillow"],
        help="Animation backend. Use 'auto' to read animation_backend from the spec.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = ROOT / spec_path
    with spec_path.open("r", encoding="utf-8") as handle:
        spec = json.load(handle)

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    poster_path = Path(args.poster) if args.poster else None
    if poster_path is not None and not poster_path.is_absolute():
        poster_path = ROOT / poster_path
    report_path = Path(args.report) if args.report else None
    if report_path is not None and not report_path.is_absolute():
        report_path = ROOT / report_path

    backend = resolve_backend(spec, args.backend)
    render(spec, out_path, poster_path, report_path, backend)


if __name__ == "__main__":
    main()
