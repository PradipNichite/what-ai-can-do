#!/usr/bin/env python3
"""Build a contact sheet from an image folder."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
FRAME_IMAGE_RE = re.compile(r"^\d{2}-.+")


def resolve_path(raw: str) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def collect_images(image_folder: Path) -> list[Path]:
    images = sorted(
        path
        for path in image_folder.iterdir()
        if path.is_file()
        and path.suffix.lower() in IMAGE_EXTENSIONS
        and FRAME_IMAGE_RE.match(path.stem)
    )
    if not images:
        raise ValueError(f"No images found in {image_folder}")
    return images


def fit_image(image: Image.Image, width: int, height: int) -> Image.Image:
    image = image.convert("RGB")
    image.thumbnail((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), "white")
    x = (width - image.width) // 2
    y = (height - image.height) // 2
    canvas.paste(image, (x, y))
    return canvas


def build_contact_sheet(
    image_paths: list[Path],
    out_path: Path,
    columns: int,
    thumb_width: int,
    label_height: int,
) -> None:
    first = Image.open(image_paths[0])
    aspect = first.height / first.width
    thumb_height = int(thumb_width * aspect)
    rows = (len(image_paths) + columns - 1) // columns
    sheet = Image.new(
        "RGB",
        (columns * thumb_width, rows * (thumb_height + label_height)),
        "white",
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for index, path in enumerate(image_paths):
        row = index // columns
        col = index % columns
        x = col * thumb_width
        y = row * (thumb_height + label_height)
        with Image.open(path) as image:
            sheet.paste(fit_image(image, thumb_width, thumb_height), (x, y))
        label = f"{index + 1:02d} {path.stem}"
        draw.rectangle((x, y + thumb_height, x + thumb_width, y + thumb_height + label_height), fill="white")
        draw.text((x + 8, y + thumb_height + 8), label[:42], fill=(0, 0, 0), font=font)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a contact sheet for generated images.")
    parser.add_argument("--image-folder", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--thumb-width", type=int, default=320)
    args = parser.parse_args()

    image_folder = resolve_path(args.image_folder)
    out_path = resolve_path(args.out)
    build_contact_sheet(
        collect_images(image_folder),
        out_path,
        max(1, args.columns),
        args.thumb_width,
        32,
    )
    print(f"Wrote contact sheet: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
