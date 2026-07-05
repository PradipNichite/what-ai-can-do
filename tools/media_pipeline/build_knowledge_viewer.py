from __future__ import annotations

import html
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "outputs" / "knowledge-viewer" / "index.html"

SCAN_DIRS = [
    "knowledge",
    "concepts",
    "channel",
    "research/youtube-channel",
    "backlog",
    "modules",
]

META_KEYS = [
    "Status",
    "Pipeline stage",
    "Type",
    "Parent topic",
    "Parent series",
    "Primary renderer",
    "Primary format",
    "Next action",
]


@dataclass
class DocItem:
    title: str
    path: str
    category: str
    status: str
    doc_type: str
    next_action: str
    summary: str
    metadata: dict[str, str]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+)$", line.strip())
        if match:
            return match.group(1).strip()
    return fallback


def extract_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in text.splitlines()[:40]:
        for key in META_KEYS:
            prefix = f"{key}:"
            if line.startswith(prefix):
                metadata[key] = line[len(prefix) :].strip()
    return metadata


def extract_summary(text: str) -> str:
    lines = []
    in_code = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped or stripped.startswith("#"):
            continue
        if re.match(r"^[A-Za-z ]+:", stripped):
            continue
        lines.append(stripped)
        if len(" ".join(lines)) > 220:
            break
    return " ".join(lines)[:260]


def category_for(path: Path) -> str:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if len(parts) >= 2 and parts[0] == "research" and parts[1] == "youtube-channel":
        return "youtube-research"
    return parts[0]


def collect_docs() -> list[DocItem]:
    docs: list[DocItem] = []
    for dirname in SCAN_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            text = read_text(path)
            metadata = extract_metadata(text)
            rel = path.relative_to(ROOT).as_posix()
            docs.append(
                DocItem(
                    title=first_heading(text, path.stem.replace("-", " ").title()),
                    path=rel,
                    category=category_for(path),
                    status=metadata.get("Status", ""),
                    doc_type=metadata.get("Type", ""),
                    next_action=metadata.get("Next action", ""),
                    summary=extract_summary(text),
                    metadata=metadata,
                )
            )
    return docs


def render_html(docs: list[DocItem]) -> str:
    data = json.dumps([asdict(doc) for doc in docs], ensure_ascii=False)
    escaped_data = data.replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>What AI Can Do - Knowledge Viewer</title>
  <style>
    :root {{
      --bg: #f7f7f4;
      --panel: #ffffff;
      --ink: #202124;
      --muted: #666a70;
      --line: #ddd8ce;
      --accent: #0f766e;
      --accent-soft: #d8f3ee;
      --warn: #a16207;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--ink);
    }}
    header {{
      padding: 24px clamp(16px, 4vw, 42px) 18px;
      border-bottom: 1px solid var(--line);
      background: #fbfaf7;
      position: sticky;
      top: 0;
      z-index: 5;
    }}
    h1 {{
      margin: 0 0 6px;
      font-size: 28px;
      line-height: 1.15;
      letter-spacing: 0;
    }}
    .subtitle {{
      margin: 0;
      color: var(--muted);
      font-size: 14px;
    }}
    .controls {{
      display: grid;
      grid-template-columns: minmax(220px, 1fr) 180px 180px;
      gap: 10px;
      padding: 16px clamp(16px, 4vw, 42px);
      border-bottom: 1px solid var(--line);
      background: var(--bg);
    }}
    input, select {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 14px;
      background: white;
      color: var(--ink);
    }}
    main {{
      display: grid;
      grid-template-columns: 260px minmax(0, 1fr);
      gap: 18px;
      padding: 18px clamp(16px, 4vw, 42px) 42px;
    }}
    aside {{
      position: sticky;
      top: 137px;
      align-self: start;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      padding: 14px;
    }}
    .stat {{
      display: flex;
      justify-content: space-between;
      gap: 10px;
      padding: 8px 0;
      border-bottom: 1px solid #eee9df;
      font-size: 14px;
    }}
    .stat:last-child {{ border-bottom: 0; }}
    .stat strong {{ color: var(--accent); }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 14px;
    }}
    .card {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      padding: 14px;
      min-height: 210px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .card h2 {{
      margin: 0;
      font-size: 18px;
      line-height: 1.25;
      letter-spacing: 0;
    }}
    .meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .pill {{
      border-radius: 999px;
      padding: 4px 8px;
      background: var(--accent-soft);
      color: #115e59;
      font-size: 12px;
      line-height: 1;
    }}
    .pill.status {{
      background: #fef3c7;
      color: var(--warn);
    }}
    .summary {{
      color: var(--muted);
      font-size: 13px;
      line-height: 1.45;
      margin: 0;
      flex: 1;
    }}
    .path {{
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
      font-size: 12px;
      overflow-wrap: anywhere;
    }}
    a {{
      color: var(--accent);
      text-decoration: none;
      font-weight: 650;
      font-size: 13px;
    }}
    a:hover {{ text-decoration: underline; }}
    .empty {{
      padding: 30px;
      border: 1px dashed var(--line);
      border-radius: 8px;
      color: var(--muted);
      background: white;
      text-align: center;
    }}
    @media (max-width: 820px) {{
      .controls {{ grid-template-columns: 1fr; }}
      main {{ grid-template-columns: 1fr; }}
      aside {{ position: static; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Knowledge Viewer</h1>
    <p class="subtitle">Markdown remains the source of truth. This page is a generated navigation layer.</p>
  </header>
  <section class="controls">
    <input id="search" type="search" placeholder="Search ideas, concepts, statuses, paths...">
    <select id="category"></select>
    <select id="status"></select>
  </section>
  <main>
    <aside>
      <div class="stat"><span>Total docs</span><strong id="total">0</strong></div>
      <div class="stat"><span>Visible</span><strong id="visible">0</strong></div>
      <div class="stat"><span>Categories</span><strong id="categories">0</strong></div>
      <div class="stat"><span>With status</span><strong id="withStatus">0</strong></div>
    </aside>
    <section>
      <div id="cards" class="grid"></div>
      <div id="empty" class="empty" hidden>No matching documents.</div>
    </section>
  </main>
  <script>
    const docs = {escaped_data};
    const search = document.querySelector("#search");
    const category = document.querySelector("#category");
    const status = document.querySelector("#status");
    const cards = document.querySelector("#cards");
    const empty = document.querySelector("#empty");

    function unique(values) {{
      return [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b));
    }}

    function fillSelect(el, label, values) {{
      el.innerHTML = `<option value="">${{label}}</option>` + values.map(v => `<option value="${{escapeHtml(v)}}">${{escapeHtml(v)}}</option>`).join("");
    }}

    function escapeHtml(value) {{
      return String(value).replace(/[&<>"']/g, ch => ({{
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        "\\"": "&quot;",
        "'": "&#39;"
      }}[ch]));
    }}

    function matches(doc) {{
      const q = search.value.trim().toLowerCase();
      const haystack = [doc.title, doc.path, doc.category, doc.status, doc.doc_type, doc.summary, doc.next_action].join(" ").toLowerCase();
      return (!q || haystack.includes(q))
        && (!category.value || doc.category === category.value)
        && (!status.value || doc.status === status.value);
    }}

    function render() {{
      const filtered = docs.filter(matches);
      cards.innerHTML = filtered.map(doc => {{
        const pills = [
          doc.category ? `<span class="pill">${{escapeHtml(doc.category)}}</span>` : "",
          doc.status ? `<span class="pill status">${{escapeHtml(doc.status)}}</span>` : "",
          doc.doc_type ? `<span class="pill">${{escapeHtml(doc.doc_type)}}</span>` : ""
        ].join("");
        return `<article class="card">
          <div class="meta">${{pills}}</div>
          <h2>${{escapeHtml(doc.title)}}</h2>
          <p class="summary">${{escapeHtml(doc.summary || doc.next_action || "No summary available yet.")}}</p>
          <div class="path">${{escapeHtml(doc.path)}}</div>
          <a href="../../${{encodeURI(doc.path)}}">Open source</a>
        </article>`;
      }}).join("");
      empty.hidden = filtered.length !== 0;
      document.querySelector("#total").textContent = docs.length;
      document.querySelector("#visible").textContent = filtered.length;
      document.querySelector("#categories").textContent = unique(docs.map(d => d.category)).length;
      document.querySelector("#withStatus").textContent = docs.filter(d => d.status).length;
    }}

    fillSelect(category, "All categories", unique(docs.map(d => d.category)));
    fillSelect(status, "All statuses", unique(docs.map(d => d.status)));
    [search, category, status].forEach(el => el.addEventListener("input", render));
    render();
  </script>
</body>
</html>
"""


def main() -> None:
    docs = collect_docs()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_html(docs), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(docs)} documents")


if __name__ == "__main__":
    main()
