import argparse
import json
from pathlib import Path

import imageio.v3 as iio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def sample_frames(video_path, samples):
    meta = iio.immeta(video_path)
    duration = float(meta.get("duration", 0) or 0)
    fps = float(meta.get("fps", 30) or 30)
    if duration <= 0:
        duration = samples

    frames = []
    for index in range(samples):
        frame_index = max(0, int(duration * fps * (index + 0.5) / samples))
        frame = iio.imread(video_path, index=frame_index, plugin="FFMPEG")
        frames.append(Image.fromarray(frame).convert("RGB"))
    return frames, duration


def frame_diff_score(frames):
    scores = []
    previous = None
    for frame in frames:
        small = frame.resize((180, 320)).convert("L")
        arr = np.asarray(small, dtype=np.float32)
        if previous is not None:
            scores.append(float(np.mean(np.abs(arr - previous))))
        previous = arr
    return scores


def black_border_ratio(frame):
    arr = np.asarray(frame.convert("RGB"))
    mask = np.all(arr < 18, axis=2)
    return float(mask.mean())


def make_contact_sheet(frames, scores, out_path):
    thumb_w, thumb_h = 216, 384
    label_h = 34
    sheet = Image.new("RGB", (thumb_w * len(frames), thumb_h + label_h), "white")
    draw = ImageDraw.Draw(sheet)

    for index, frame in enumerate(frames):
        thumb = frame.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = index * thumb_w
        sheet.paste(thumb, (x, 0))
        label = f"{index + 1}"
        if index > 0:
            label += f" diff {scores[index - 1]:.1f}"
        draw.text((x + 8, thumb_h + 8), label, fill=(0, 0, 0))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path)


def main():
    parser = argparse.ArgumentParser(description="Create a contact sheet and motion score for an MP4.")
    parser.add_argument("video", help="Path to MP4.")
    parser.add_argument("--samples", type=int, default=8)
    args = parser.parse_args()

    video_path = Path(args.video).resolve()
    frames, duration = sample_frames(video_path, args.samples)
    scores = frame_diff_score(frames)
    borders = [black_border_ratio(frame) for frame in frames]

    out_dir = video_path.parent / "verification"
    sheet_path = out_dir / f"{video_path.stem}.contact-sheet.jpg"
    report_path = out_dir / f"{video_path.stem}.motion-report.json"
    make_contact_sheet(frames, scores, sheet_path)

    report = {
        "video": str(video_path),
        "duration_seconds": duration,
        "samples": args.samples,
        "mean_frame_diff": float(np.mean(scores)) if scores else 0,
        "max_frame_diff": float(np.max(scores)) if scores else 0,
        "black_border_ratio_mean": float(np.mean(borders)),
        "black_border_ratio_max": float(np.max(borders)),
        "contact_sheet": str(sheet_path),
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
