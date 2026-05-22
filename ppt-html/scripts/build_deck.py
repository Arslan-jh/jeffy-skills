#!/usr/bin/env python3
"""Render a small JSON slide spec into a print-ready HTML deck."""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT / "assets" / "slide.css"


def esc(value: object) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def render_title(slide: dict, page: int) -> str:
    return f"""  <section class="slide title-slide" data-page="{page}">
    <p class="kicker">{esc(slide.get("kicker", "Presentation"))}</p>
    <h1 class="slide-title">{esc(slide.get("title", ""))}</h1>
    <p class="subtitle">{esc(slide.get("subtitle", ""))}</p>
  </section>"""


def render_section(slide: dict, page: int) -> str:
    number = esc(slide.get("number", f"{page:02d}"))
    return f"""  <section class="slide section-slide" data-page="{page}">
    <div class="section-number">{number}</div>
    <div>
      <p class="kicker">{esc(slide.get("kicker", "Section"))}</p>
      <h2 class="slide-title">{esc(slide.get("title", ""))}</h2>
      <p class="key-message">{esc(slide.get("message", slide.get("subtitle", "")))}</p>
    </div>
  </section>"""


def render_bullets(slide: dict, page: int) -> str:
    bullets = "\n".join(f"      <li>{esc(item)}</li>" for item in slide.get("bullets", []))
    return f"""  <section class="slide" data-page="{page}">
    <p class="kicker">{esc(slide.get("kicker", ""))}</p>
    <h2 class="slide-title">{esc(slide.get("title", ""))}</h2>
    <p class="key-message">{esc(slide.get("message", ""))}</p>
    <ul class="bullets">
{bullets}
    </ul>
  </section>"""


def render_cards(slide: dict, page: int) -> str:
    cards = []
    for card in slide.get("cards", []):
        cards.append(
            f"""      <article class="card">
        <h3>{esc(card.get("title", ""))}</h3>
        <p>{esc(card.get("body", ""))}</p>
      </article>"""
        )
    columns = "three" if len(cards) >= 3 else "two"
    return f"""  <section class="slide" data-page="{page}">
    <p class="kicker">{esc(slide.get("kicker", ""))}</p>
    <h2 class="slide-title">{esc(slide.get("title", ""))}</h2>
    <p class="key-message">{esc(slide.get("message", ""))}</p>
    <div class="grid {columns}">
{chr(10).join(cards)}
    </div>
  </section>"""


def render_table(slide: dict, page: int) -> str:
    headers = slide.get("headers", [])
    rows = slide.get("rows", [])
    thead = "".join(f"<th>{esc(header)}</th>" for header in headers)
    body_rows = []
    for row in rows:
        body_rows.append("      <tr>" + "".join(f"<td>{esc(cell)}</td>" for cell in row) + "</tr>")
    return f"""  <section class="slide" data-page="{page}">
    <p class="kicker">{esc(slide.get("kicker", ""))}</p>
    <h2 class="slide-title">{esc(slide.get("title", ""))}</h2>
    <p class="key-message">{esc(slide.get("message", ""))}</p>
    <table class="data-table">
      <thead><tr>{thead}</tr></thead>
      <tbody>
{chr(10).join(body_rows)}
      </tbody>
    </table>
  </section>"""


def render_timeline(slide: dict, page: int) -> str:
    items = slide.get("items", [])
    milestones = []
    for item in items:
        milestones.append(
            f"""      <article class="milestone">
        <strong>{esc(item.get("label", ""))}</strong>
        <p>{esc(item.get("body", ""))}</p>
      </article>"""
        )
    count = max(1, len(items))
    return f"""  <section class="slide" data-page="{page}">
    <p class="kicker">{esc(slide.get("kicker", ""))}</p>
    <h2 class="slide-title">{esc(slide.get("title", ""))}</h2>
    <p class="key-message">{esc(slide.get("message", ""))}</p>
    <div class="timeline" style="--items: {count}">
{chr(10).join(milestones)}
    </div>
  </section>"""


RENDERERS = {
    "title": render_title,
    "section": render_section,
    "bullets": render_bullets,
    "cards": render_cards,
    "table": render_table,
    "timeline": render_timeline,
}


def render_deck(spec: dict) -> str:
    css = CSS_PATH.read_text(encoding="utf-8")
    slides = []
    for index, slide in enumerate(spec.get("slides", []), start=1):
        renderer = RENDERERS.get(slide.get("type", "bullets"), render_bullets)
        slides.append(renderer(slide, index))
    title = esc(spec.get("title", "PPT HTML Deck"))
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
{css}
  </style>
</head>
<body>
{chr(10).join(slides)}
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: build_deck.py input.json output.html", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    spec = json.loads(input_path.read_text(encoding="utf-8-sig"))
    output_path.write_text(render_deck(spec), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
