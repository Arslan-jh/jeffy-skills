---
name: ppt-html
description: Create PowerPoint-style presentation decks as polished HTML slides. Use when the user asks to make a PPT, slide deck, presentation, training deck, report deck, strategy deck, consulting deck, business review, or asks to output PPT content as HTML first. Supports user-provided templates or style references; if none is provided, use the local default style reference at C:\Users\lenovo\Desktop\卓越运营PPT材料排版与样式参考.pdf when available, otherwise use bundled default style notes.
---

# PPT HTML

Create browser-previewable, print-ready HTML slide decks before any PPTX conversion. Prefer a complete HTML file unless the user asks for separate assets.

## Workflow

1. Clarify only missing essentials: topic, audience, source material, desired slide count, language, and whether the user has a template.
2. If the user provides a PPT/PDF/image/template, inspect it before drafting. Extract layout patterns, typography, colors, page furniture, chart/table style, section dividers, and density.
3. If no template is provided, first try the local reference PDF:
   `C:\Users\lenovo\Desktop\卓越运营PPT材料排版与样式参考.pdf`
4. If the local PDF is unavailable or cannot be read, load `references/default-style-notes.md`.
5. Build an internal slide outline before writing HTML. Each slide needs one dominant message.
6. Produce HTML slides using `assets/deck.html` and `assets/slide.css` as the baseline style.
7. Validate print behavior: 16:9 pages, one slide per printed page, no text overflow, no clipped tables, no incoherent overlaps.

## Output Standard

- Use 16:9 slides.
- Represent slides as `<section class="slide ...">`.
- Include CSS inline for single-file deliverables unless separate files are requested.
- Keep slide text concise and executive-friendly.
- Use structured visual forms: KPI cards, comparison tables, timelines, process flows, matrices, operating models, issue trees, and callouts.
- Avoid article-like paragraphs, decorative clutter, and generic marketing hero layouts.
- Use Chinese typography defaults when the deck is Chinese: Microsoft YaHei, PingFang SC, Noto Sans CJK, Arial.
- Prefer restrained business styling: clean backgrounds, clear hierarchy, consistent spacing, and selective accent colors.

## Default Style

When using the default reference style, load `references/default-style-notes.md`. Treat it as the fallback representation of the desktop PDF rather than a replacement for inspecting a user-provided or local template.

Do not copy the desktop PDF into public repositories unless the user explicitly requests that file to be published.

## Assets

- `assets/deck.html`: single-file HTML starter with common slide structures.
- `assets/slide.css`: reusable CSS for print-ready 16:9 slides.
- `scripts/build_deck.py`: optional helper that renders a JSON slide spec into HTML.

Use the script when the slide content is already structured or when repeatability matters. For custom high-design decks, edit from the HTML/CSS assets directly.

## JSON Render Helper

The optional render script accepts:

```json
{
  "title": "Deck title",
  "slides": [
    {
      "type": "title",
      "title": "Main title",
      "subtitle": "Subtitle"
    },
    {
      "type": "bullets",
      "title": "Slide title",
      "kicker": "Section label",
      "bullets": ["Point one", "Point two"]
    }
  ]
}
```

Run:

```bash
python scripts/build_deck.py input.json output.html
```

Supported slide types: `title`, `section`, `bullets`, `table`, `cards`, `timeline`.
