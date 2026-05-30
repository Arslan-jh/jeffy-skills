#!/usr/bin/env python3
"""Render a deck JSON into a browser-previewable HTML slide deck."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


CSS = """
@page { size: 16in 9in; margin: 0; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f3f3f3;
  font-family: "Microsoft YaHei", "PingFang SC", Arial, sans-serif;
  color: #1f1f1f;
}
.deck { padding: 24px; display: grid; gap: 24px; }
.slide {
  width: 1280px;
  height: 720px;
  background: white;
  padding: 48px 54px;
  position: relative;
  overflow: hidden;
  border: 1px solid #ddd;
}
.slide::after {
  content: attr(data-page);
  position: absolute;
  right: 34px;
  bottom: 24px;
  color: #999;
  font-size: 13px;
}
h1 {
  margin: 0 0 32px;
  color: #c00000;
  font-size: 34px;
  line-height: 1.18;
  font-weight: 700;
}
.role {
  margin-bottom: 10px;
  color: #777;
  font-size: 15px;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}
.card {
  min-height: 160px;
  border: 1px solid #d9d9d9;
  padding: 20px 22px;
  background: #fff;
}
.card h2 {
  margin: 0 0 14px;
  font-size: 22px;
  line-height: 1.25;
}
ul { margin: 0; padding-left: 1.2em; }
li { margin: 8px 0; font-size: 18px; line-height: 1.42; }
.summary {
  border-left: 5px solid #c00000;
  padding-left: 18px;
  font-size: 22px;
  line-height: 1.45;
}
@media print {
  body { background: white; }
  .deck { padding: 0; gap: 0; display: block; }
  .slide { border: 0; page-break-after: always; width: 16in; height: 9in; }
}
"""


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def render_points(points: list[dict]) -> str:
    cards = []
    for point in points[:4]:
        heading = esc(point.get("heading", ""))
        body = point.get("body", [])
        if isinstance(body, str):
            body = [body]
        items = "".join(f"<li>{esc(item)}</li>" for item in body[:4])
        cards.append(f'<article class="card"><h2>{heading}</h2><ul>{items}</ul></article>')
    return f'<div class="grid">{"".join(cards)}</div>'


def render_slide(slide: dict, idx: int) -> str:
    role = esc(slide.get("role", ""))
    title = esc(slide.get("title", ""))
    points = slide.get("points", [])
    summary = esc(slide.get("summary", ""))
    body = render_points(points) if points else f'<div class="summary">{summary}</div>'
    return f"""
<section class="slide" data-page="{idx:02d}">
  <div class="role">{role}</div>
  <h1>{title}</h1>
  {body}
</section>"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_html", type=Path)
    args = parser.parse_args()

    deck = json.loads(args.input_json.read_text(encoding="utf-8"))
    slides = deck.get("slides", [])
    rendered = "\n".join(render_slide(slide, i) for i, slide in enumerate(slides, 1))
    title = esc(deck.get("title", "PPT预览"))
    html_doc = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>{CSS}</style>
</head>
<body>
  <main class="deck">
    {rendered}
  </main>
</body>
</html>
"""
    args.output_html.parent.mkdir(parents=True, exist_ok=True)
    args.output_html.write_text(html_doc, encoding="utf-8")


if __name__ == "__main__":
    main()
