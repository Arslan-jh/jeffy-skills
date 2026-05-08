#!/usr/bin/env python3
"""
立体分析法报告 Markdown → PDF 转换脚本 (WeasyPrint版)
用法: python md_to_pdf.py input.md output.pdf [--title "报告标题"] [--subtitle "副标题"] [--author "作者"] [--no-html]

依赖: pip install weasyprint markdown --break-system-packages
"""

import argparse
import html
import importlib
import importlib.util
import os
import re
from pathlib import Path


def require_dependency(module_name, install_hint):
    """Return an optional runtime dependency or raise a clear install message."""
    if importlib.util.find_spec(module_name) is None:
        raise RuntimeError(f"缺少依赖 {module_name}。请先安装：{install_hint}")
    return importlib.import_module(module_name)


# ── CSS 样式 ──
CSS_TEMPLATE = """
@page {
    size: A4;
    margin: 24mm 22mm 22mm 22mm;

    @top-center {
        content: "HEADER_TEXT";
        font-family: "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", SimSun, serif;
        font-size: 8pt;
        color: #6b7280;
        border-bottom: 0.4pt solid #d1d5db;
        padding-bottom: 3mm;
    }

    @bottom-center {
        content: counter(page);
        font-family: "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", SimSun, serif;
        font-size: 8pt;
        color: #6b7280;
    }
}

@page :first {
    @top-center { content: none; }
    @bottom-center { content: none; }
}

body {
    font-family: "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", SimSun, "Times New Roman", serif;
    font-size: 10.8pt;
    line-height: 1.68;
    color: #111827;
    text-align: justify;
    hyphens: auto;
}

/* 封面：论文式，克制留白 */
.cover {
    page-break-after: always;
    text-align: center;
    padding-top: 35%;
}
.cover h1 {
    font-size: 26pt;
    color: #111827;
    margin-bottom: 7mm;
    font-weight: 700;
    letter-spacing: 1pt;
    line-height: 1.25;
}
.cover .subtitle {
    font-size: 13pt;
    color: #374151;
    margin-bottom: 6mm;
}
.cover .meta {
    font-size: 10.5pt;
    color: #4b5563;
    margin-bottom: 3mm;
}
.cover .divider {
    width: 42%;
    margin: 9mm auto;
    border: none;
    border-top: 1pt solid #111827;
}

/* 论文正文标题：清楚但不花哨 */
h1, h2, h3, h4 {
    font-family: "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", SimSun, serif;
    color: #111827;
    font-weight: 700;
    page-break-after: avoid;
}

h1 {
    font-size: 19pt;
    text-align: center;
    margin-top: 14mm;
    margin-bottom: 8mm;
    padding-bottom: 3mm;
    border-bottom: 1.2pt solid #111827;
}

h2 {
    font-size: 15pt;
    margin-top: 11mm;
    margin-bottom: 5mm;
    padding-bottom: 2mm;
    border-bottom: 0.6pt solid #d1d5db;
}

h3 {
    font-size: 12.5pt;
    margin-top: 7mm;
    margin-bottom: 3mm;
}

h4 {
    font-size: 11pt;
    margin-top: 5mm;
    margin-bottom: 2mm;
    color: #374151;
}

/* 段落 */
p {
    margin-top: 1.6mm;
    margin-bottom: 1.6mm;
    orphans: 3;
    widows: 3;
}

body > p {
    text-indent: 2em;
}

/* 摘要/引文块 */
blockquote {
    margin: 5mm 0;
    padding: 4mm 5mm;
    background: #f9fafb;
    border-left: 2.2pt solid #4b5563;
    color: #374151;
    font-size: 10.2pt;
    page-break-inside: avoid;
}
blockquote p {
    margin: 1mm 0;
    text-indent: 0;
}

/* 目录（启用 Python-Markdown toc 扩展后可用 [TOC] 生成） */
.toc {
    border: 0.6pt solid #d1d5db;
    padding: 4mm 5mm;
    margin: 5mm 0 8mm 0;
    background: #fcfcfd;
    page-break-inside: avoid;
}
.toc ul {
    margin: 1mm 0;
    padding-left: 6mm;
}
.toc li {
    margin-bottom: 0.5mm;
}

strong, b {
    font-weight: 700;
    color: #111827;
}

code {
    font-family: "Courier New", Courier, monospace;
    background: #f3f4f6;
    color: #991b1b;
    padding: 0.3mm 1mm;
    border-radius: 2pt;
    font-size: 9.5pt;
}

pre {
    background: #f9fafb;
    border: 0.5pt solid #e5e7eb;
    padding: 3mm;
    white-space: pre-wrap;
    font-size: 9.2pt;
    page-break-inside: avoid;
}

/* 表格：论文风格，适合时间线/证据/剧本 */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 5mm 0;
    font-size: 9.3pt;
    page-break-inside: avoid;
}
thead th {
    background: #f3f4f6;
    color: #111827;
    padding: 2.6mm;
    text-align: left;
    font-weight: 700;
    border-top: 1pt solid #111827;
    border-bottom: 0.7pt solid #6b7280;
}
tbody td {
    padding: 2.4mm 2.6mm;
    border-bottom: 0.4pt solid #d1d5db;
    vertical-align: top;
}
tbody tr:nth-child(even) {
    background: #fbfbfc;
}

hr {
    border: none;
    border-top: 0.5pt solid #d1d5db;
    margin: 6mm 0;
}

ul, ol {
    margin: 2mm 0 3mm 0;
    padding-left: 7mm;
}
li {
    margin-bottom: 1.2mm;
}
li p {
    text-indent: 0;
}

/* 脚注 */
.footnote {
    font-size: 8.8pt;
    color: #374151;
    border-top: 0.5pt solid #d1d5db;
    margin-top: 8mm;
    padding-top: 3mm;
}

sup {
    font-size: 7.5pt;
}

a {
    color: #1f4e79;
    text-decoration: none;
}
"""


def md_to_html(md_text, title="立体分析报告", subtitle="立体分析法深度研究报告",
               meta_line="", author="jeffy"):
    """将 Markdown 转为带封面的 HTML"""

    markdown = require_dependency("markdown", "pip install markdown")

    # 用 markdown 库转换正文
    html_body = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'nl2br', 'toc', 'footnotes', 'sane_lists'],
        output_format='html5'
    )

    # 移除正文中的第一个 h1（会用在封面上）
    first_h1_match = re.search(r'<h1>(.*?)</h1>', html_body)
    if first_h1_match:
        extracted_title = html.unescape(first_h1_match.group(1))
        if not title or title == "立体分析报告":
            title = extracted_title
        html_body = html_body.replace(first_h1_match.group(0), '', 1)

    safe_title = html.escape(title, quote=True)
    safe_subtitle = html.escape(subtitle, quote=True)
    safe_meta_line = html.escape(meta_line, quote=True)
    safe_author = html.escape(author, quote=True)

    # 替换 CSS 中的页眉占位符。CSS content 字符串需要单独转义引号和反斜杠。
    header_text = f"{title}  |  立体分析法深度研究报告"
    header_text = header_text.replace("\\", "\\\\").replace('"', '\\"')
    css = CSS_TEMPLATE.replace("HEADER_TEXT", header_text)

    # 构建封面
    meta_html = f"<div class='meta'>{safe_meta_line}</div>" if safe_meta_line else ""
    cover_html = f"""
    <div class="cover">
        <h1 style="page-break-before: avoid; border: none;">{safe_title}</h1>
        <div class="subtitle">{safe_subtitle}</div>
        {meta_html}
        <hr class="divider">
        <div class="meta">作者: {safe_author}</div>
    </div>
    """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <style>{css}</style>
</head>
<body>
{cover_html}
{html_body}
</body>
</html>"""

    return full_html


def main():
    parser = argparse.ArgumentParser(description="立体分析法报告 Markdown → PDF")
    parser.add_argument("input", help="输入的 Markdown 文件路径")
    parser.add_argument("output", help="输出的 PDF 文件路径")
    parser.add_argument("--title", default=None, help="报告标题；默认使用 Markdown 第一个 H1")
    parser.add_argument("--subtitle", default="立体分析法深度研究报告", help="封面副标题")
    parser.add_argument("--author", default="jeffy", help="作者名")
    parser.add_argument("--no-html", action="store_true", help="只输出 PDF，不保留中间 HTML")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    with input_path.open("r", encoding="utf-8") as f:
        md_text = f.read()

    # 提取元信息
    meta_line = ""
    for line in md_text.split("\n"):
        stripped = line.strip().lstrip(">").strip()
        if "研究时间" in stripped or "所属领域" in stripped or "研究对象类型" in stripped:
            meta_line = stripped
            break

    rendered_html = md_to_html(
        md_text,
        title=args.title or "立体分析报告",
        subtitle=args.subtitle,
        meta_line=meta_line,
        author=args.author,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 保存中间 HTML（便于调试）
    html_path = output_path.with_suffix(".html")
    if not args.no_html:
        html_path.write_text(rendered_html, encoding="utf-8")
        print(f"[OK] HTML 已生成: {html_path}")

    # 转 PDF
    weasyprint = require_dependency("weasyprint", "pip install weasyprint")

    weasyprint.HTML(string=rendered_html, base_url=str(input_path.parent.resolve())).write_pdf(str(output_path))
    size_kb = os.path.getsize(output_path) / 1024
    print(f"[OK] PDF 已生成: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
