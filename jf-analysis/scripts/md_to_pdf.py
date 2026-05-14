#!/usr/bin/env python3
"""
立体分析法报告 Markdown → PDF 转换脚本 (WeasyPrint版)
用法: python md_to_pdf.py input.md output.pdf [--title "报告标题"] [--author "作者"]

依赖: pip install weasyprint markdown --break-system-packages
"""

import argparse
import html
import os
import re
from pathlib import Path

import markdown

# ── CSS 样式 ──
CSS_TEMPLATE = """
@page {
    size: A4;
    margin: 25mm 20mm 20mm 20mm;

    @top-center {
        content: "HEADER_TEXT";
        font-family: "Droid Sans Fallback", Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #8c6f6f;
        border-bottom: 0.5pt solid #f0d9d9;
        padding-bottom: 3mm;
    }

    @bottom-center {
        content: "第 " counter(page) " 页";
        font-family: "Droid Sans Fallback", Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #8c6f6f;
        border-top: 0.8pt solid #c00000;
        padding-top: 2mm;
    }
}

@page :first {
    @top-center { content: none; }
    @bottom-center { content: none; }
}

body {
    font-family: "Droid Sans Fallback", Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.75;
    color: #2f2727;
    text-align: justify;
    background: #ffffff;
}

/* 封面 */
.cover {
    page-break-after: always;
    text-align: center;
    padding-top: 45%;
}
.cover h1 {
    font-size: 28pt;
    color: #c00000;
    margin-bottom: 8mm;
    font-weight: bold;
    letter-spacing: 2pt;
    line-height: 1.25;
}
.cover .subtitle {
    font-size: 14pt;
    color: #8c6f6f;
    margin-bottom: 6mm;
}
.cover .meta {
    font-size: 11pt;
    color: #8c6f6f;
    margin-bottom: 4mm;
}
.cover .divider {
    width: 60%;
    margin: 8mm auto;
    border: none;
    border-top: 1.8pt solid #c00000;
}

/* 一级标题 */
h1 {
    font-size: 20pt;
    color: #c00000;
    margin-top: 16mm;
    margin-bottom: 6mm;
    padding-bottom: 3mm;
    border-bottom: 2pt solid #c00000;
    border-left: 5pt solid #c00000;
    padding-left: 4mm;
    page-break-before: always;
    font-weight: bold;
}

/* 二级标题 */
h2 {
    font-size: 14pt;
    color: #8a0000;
    margin-top: 10mm;
    margin-bottom: 5mm;
    padding-bottom: 1.5mm;
    border-bottom: 0.6pt solid #e2bcbc;
    font-weight: bold;
}

/* 三级标题 */
h3 {
    font-size: 12pt;
    color: #a60000;
    margin-top: 6mm;
    margin-bottom: 3mm;
    font-weight: bold;
}

h4 {
    font-size: 11pt;
    color: #7a0000;
    margin-top: 5mm;
    margin-bottom: 2mm;
    font-weight: bold;
}

/* 段落 */
p {
    margin-top: 1.5mm;
    margin-bottom: 1.5mm;
    orphans: 3;
    widows: 3;
}

/* 引用块 */
blockquote {
    margin: 4mm 0;
    padding: 4mm 4mm 4mm 8mm;
    background: #fff7f7;
    border-left: 3pt solid #c00000;
    color: #5f4b4b;
    font-size: 10pt;
}
blockquote p {
    margin: 1mm 0;
}

/* 粗体 */
strong, b {
    font-weight: bold;
    color: #2b1a1a;
}

/* 行内代码 */
code {
    font-family: "Courier New", Courier, monospace;
    background: #fff0f0;
    color: #c00000;
    padding: 0.5mm 1.5mm;
    border-radius: 2pt;
    font-size: 9.5pt;
}

/* 表格 */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 9.5pt;
}
thead th {
    background: #c00000;
    color: white;
    padding: 3mm;
    text-align: left;
    font-weight: bold;
}
tbody td {
    padding: 2.5mm 3mm;
    border-bottom: 0.5pt solid #e2bcbc;
}
tbody tr:nth-child(even) {
    background: #fff7f7;
}
tbody tr:nth-child(odd) {
    background: #ffffff;
}

/* 分隔线 */
hr {
    border: none;
    border-top: 0.5pt solid #e2bcbc;
    margin: 4mm 0;
}

/* 列表 */
ul, ol {
    margin: 2mm 0;
    padding-left: 8mm;
}
li {
    margin-bottom: 1mm;
}

/* 链接 */
a {
    color: #c00000;
    text-decoration: none;
}
"""


def md_to_html(md_text, title="立体分析报告", subtitle="立体分析法深度研究报告",
               meta_line="", author="jeffy"):
    """将 Markdown 转为带封面的 HTML"""

    # 用 markdown 库转换正文
    html_body = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'nl2br'],
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

    # 保存中间 HTML（便于调试）
    html_path = output_path.with_suffix(".html")
    if not args.no_html:
        html_path.write_text(rendered_html, encoding="utf-8")
        print(f"[OK] HTML 已生成: {html_path}")

    # 转 PDF
    from weasyprint import HTML

    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=rendered_html, base_url=str(input_path.parent.resolve())).write_pdf(str(output_path))
    size_kb = os.path.getsize(output_path) / 1024
    print(f"[OK] PDF 已生成: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
