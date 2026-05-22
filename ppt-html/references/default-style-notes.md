# Default PPT HTML Style Notes

Use these notes when the user does not provide a template and the local default PDF cannot be inspected.

## Overall Direction

Create a professional enterprise operations / consulting deck. The visual feel should be clean, structured, information-dense, and executive-facing. Prioritize readability, hierarchy, and decision support over decoration.

## Page Setup

- 16:9 landscape slide.
- White or very light neutral background.
- Consistent outer margins.
- Small page footer or section marker is acceptable.
- Use page numbers only when helpful.

## Typography

- Chinese decks: Microsoft YaHei, PingFang SC, Noto Sans CJK, Arial.
- English decks: Aptos, Arial, Helvetica, sans-serif.
- Titles should be strong but not oversized.
- Body copy should be compact and scannable.
- Avoid long paragraphs. Convert prose into grouped bullets, tables, labels, and callouts.

## Color

- Base: white, off-white, dark gray text.
- Accent: deep blue, teal, or restrained orange for emphasis.
- Use accent colors sparingly: section labels, key numbers, active steps, or important callouts.
- Avoid one-note palettes and large decorative gradients.

## Layout Patterns

- Title slide: clear title, subtitle/context, date or owner if available.
- Section divider: large section number or label, concise section title, short guiding line.
- Content slide: title at top, key message under title, then structured body.
- Dense analysis slide: left logic column plus right evidence/table/diagram.
- KPI slide: 3-5 metric cards with short interpretation.
- Timeline slide: horizontal milestones with clear dates/stages.
- Process slide: numbered steps with inputs, actions, outputs, and owners.
- Comparison slide: matrix table with highlighted differentiators.

## Tables And Diagrams

- Tables should have clear header rows, light grid lines, and restrained emphasis.
- Do not overuse borders. Use spacing and background fills for grouping.
- Diagrams should use aligned boxes, arrows, labels, and consistent sizing.
- Each chart or table needs a takeaway, not just raw data.

## Content Rules

- One dominant message per slide.
- Prefer "conclusion first" titles when appropriate.
- Use short evidence lines under key claims.
- When source material is long, synthesize before laying out.
- Preserve important numbers, dates, definitions, and named entities.

## HTML/CSS Rules

- Use fixed 16:9 slide dimensions with print page breaks.
- Avoid viewport-scaled font sizes.
- Avoid overlapping absolute-positioned text unless dimensions are controlled.
- Check that Chinese and English text both fit.
- Make components reusable: `.slide-title`, `.key-message`, `.grid`, `.card`, `.table`, `.timeline`.
