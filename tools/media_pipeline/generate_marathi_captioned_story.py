from html import escape
from pathlib import Path
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "assets" / "images" / "customer-support-mobile-story"
OUT_DIR = ROOT / "assets" / "images" / "customer-support-mobile-story-mr"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

WIDTH = 941
HEIGHT = 1672

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


def html_for_card(index, filename, title, body):
    image_uri = (SRC_DIR / filename).resolve().as_uri()
    return f"""<!doctype html>
<html lang="mr">
<head>
  <meta charset="utf-8">
  <style>
    * {{
      box-sizing: border-box;
    }}
    html, body {{
      margin: 0;
      width: {WIDTH}px;
      height: {HEIGHT}px;
      overflow: hidden;
      background: #111;
      font-family: "Nirmala UI", "Noto Sans Devanagari", "Mangal", system-ui, sans-serif;
    }}
    .card {{
      position: relative;
      width: {WIDTH}px;
      height: {HEIGHT}px;
      background-image: url("{image_uri}");
      background-size: cover;
      background-position: center center;
    }}
    .caption {{
      position: absolute;
      left: 52px;
      right: 52px;
      bottom: 58px;
      min-height: 320px;
      padding: 34px 34px 38px;
      border: 4px solid #ffc44d;
      border-radius: 36px;
      background: rgba(255, 250, 240, 0.95);
      box-shadow: 0 14px 34px rgba(0, 0, 0, 0.33);
    }}
    .step {{
      position: absolute;
      top: 22px;
      right: 22px;
      padding: 7px 18px 9px;
      border-radius: 18px;
      background: #0c2d5f;
      color: #fff;
      font-size: 34px;
      font-weight: 800;
      line-height: 1.05;
    }}
    h1 {{
      margin: 0 95px 20px 0;
      color: #0c2d5f;
      font-size: 50px;
      font-weight: 800;
      line-height: 1.12;
      letter-spacing: 0;
    }}
    p {{
      margin: 0;
      color: #222;
      font-size: 34px;
      line-height: 1.42;
      font-weight: 400;
      letter-spacing: 0;
    }}
  </style>
</head>
<body>
  <main class="card">
    <section class="caption">
      <div class="step">{index}/7</div>
      <h1>{escape(title)}</h1>
      <p>{escape(body)}</p>
    </section>
  </main>
</body>
</html>
"""


def render_card(index, filename, title, body, temp_dir):
    html_path = temp_dir / f"{index:02d}.html"
    out_path = OUT_DIR / filename
    html_path.write_text(html_for_card(index, filename, title, body), encoding="utf-8")

    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={WIDTH},{HEIGHT}",
        f"--screenshot={out_path}",
        html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    if not CHROME.exists():
        raise FileNotFoundError(f"Chrome not found at {CHROME}")
    with tempfile.TemporaryDirectory() as tmp:
        temp_dir = Path(tmp)
        for index, (filename, title, body) in enumerate(CARDS, start=1):
            render_card(index, filename, title, body, temp_dir)
    print(f"Created {len(CARDS)} Marathi captioned story images in {OUT_DIR}")


if __name__ == "__main__":
    main()
