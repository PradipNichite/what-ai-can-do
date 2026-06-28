from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "assets" / "images" / "customer-support-mobile-story"
OUT_DIR = ROOT / "assets" / "images" / "customer-support-mobile-story-mr"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_BOLD = r"C:\Windows\Fonts\NirmalaB.ttf"
FONT_REGULAR = r"C:\Windows\Fonts\Nirmala.ttf"

CARDS = [
    (
        "01-late-order.png",
        "माझी ऑर्डर अजून आली नाही",
        "कस्टमरला फक्त एकच गोष्ट जाणून घ्यायची आहे: “माझं पार्सल कुठे आहे?”",
    ),
    (
        "02-human-checks-system.png",
        "सपोर्ट एजंट सिस्टम चेक करतो",
        "तो ऑर्डर आयडी किंवा मोबाइल नंबर घेऊन सिस्टममध्ये ऑर्डर शोधतो.",
    ),
    (
        "03-ai-without-access.png",
        "एआयकडे माहितीच नसेल तर?",
        "तो फक्त साधं उत्तर देऊ शकतो. खरं डिलिव्हरी स्टेटस सांगू शकत नाही.",
    ),
    (
        "04-ai-gets-tools.png",
        "एआयला योग्य सिस्टम जोडली",
        "ऑर्डर सिस्टम, डेटाबेस आणि कुरियर स्टेटस जोडले की एआय प्रत्यक्ष ऑर्डर चेक करू शकतो.",
    ),
    (
        "05-specific-update.png",
        "आता उत्तर नेमकं मिळतं",
        "पार्सल सध्या कुठे आहे, डिलिव्हरी कधी होऊ शकते, हे एआय स्पष्ट सांगू शकतो.",
    ),
    (
        "06-human-handover.png",
        "केस अवघड असेल तर माणूस हवा",
        "रिफंड, डॅमेज्ड आयटम किंवा रागावलेला कस्टमर असेल, तर माणसाचा सपोर्ट गरजेचा आहे.",
    ),
    (
        "07-ai-tools-human-summary.png",
        "बेस्ट सेटअप",
        "साधं काम एआय करतो. अवघड केस माणसाकडे जातात.",
    ),
]


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def text_height(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]


def fit_font(draw, text, font_path, max_width, start_size, min_size):
    size = start_size
    while size >= min_size:
        font = ImageFont.truetype(font_path, size)
        if text_width(draw, text, font) <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(font_path, min_size)


def wrap_text(draw, text, font, max_width):
    words = text.split(" ")
    lines = []
    line = ""
    for word in words:
        candidate = word if not line else f"{line} {word}"
        if text_width(draw, candidate, font) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def render_card(index, filename, title, body):
    img = Image.open(SRC_DIR / filename).convert("RGB")
    width, height = img.size
    canvas = img.copy().convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    margin = int(width * 0.055)
    panel_width = width - 2 * margin
    panel_height = int(height * 0.21)
    panel_x = margin
    panel_y = height - panel_height - int(height * 0.035)
    radius = 36

    shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        (
            panel_x + 8,
            panel_y + 10,
            panel_x + panel_width + 8,
            panel_y + panel_height + 10,
        ),
        radius=radius,
        fill=(0, 0, 0, 90),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    canvas.alpha_composite(shadow)

    draw.rounded_rectangle(
        (panel_x, panel_y, panel_x + panel_width, panel_y + panel_height),
        radius=radius,
        fill=(255, 250, 240, 238),
        outline=(255, 196, 77, 255),
        width=4,
    )

    tag = f"{index}/7"
    tag_font = ImageFont.truetype(FONT_BOLD, 34)
    tag_w = text_width(draw, tag, tag_font)
    tag_h = text_height(draw, tag, tag_font)
    tag_pad_x, tag_pad_y = 18, 8
    tag_x = panel_x + panel_width - tag_w - 2 * tag_pad_x - 22
    tag_y = panel_y + 22
    draw.rounded_rectangle(
        (
            tag_x,
            tag_y,
            tag_x + tag_w + 2 * tag_pad_x,
            tag_y + tag_h + 2 * tag_pad_y,
        ),
        radius=18,
        fill=(12, 45, 95, 255),
    )
    draw.text(
        (tag_x + tag_pad_x, tag_y + tag_pad_y - 2),
        tag,
        font=tag_font,
        fill=(255, 255, 255, 255),
    )

    max_text_width = panel_width - 60
    title_font = fit_font(draw, title, FONT_BOLD, max_text_width - 110, 48, 34)
    body_font = ImageFont.truetype(FONT_REGULAR, 34)
    body_lines = wrap_text(draw, body, body_font, max_text_width)

    while len(body_lines) > 3 and body_font.size > 26:
        body_font = ImageFont.truetype(FONT_REGULAR, body_font.size - 2)
        body_lines = wrap_text(draw, body, body_font, max_text_width)

    text_x = panel_x + 34
    text_y = panel_y + 24
    draw.text((text_x, text_y), title, font=title_font, fill=(12, 45, 95, 255))
    text_y += text_height(draw, title, title_font) + 22

    for line in body_lines:
        draw.text((text_x, text_y), line, font=body_font, fill=(32, 32, 32, 255))
        text_y += int(body_font.size * 1.45)

    canvas.convert("RGB").save(OUT_DIR / filename, quality=95)


def main():
    for index, (filename, title, body) in enumerate(CARDS, start=1):
        render_card(index, filename, title, body)
    print(f"Created {len(CARDS)} Marathi captioned story images in {OUT_DIR}")


if __name__ == "__main__":
    main()
