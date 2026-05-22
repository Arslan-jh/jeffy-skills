---
name: ppt-html
description: 将 PPT、演示文稿、汇报材料、培训课件、咨询报告、经营分析、战略汇报等内容先制作成精美的 HTML 幻灯片。适用于用户要求“做 PPT”“写一套 slides”“生成演示文稿”“先输出 HTML 格式”“根据模板排版 PPT”等场景。支持用户提供 PPT/PDF/图片/HTML 模板作为样式参考；如果用户不提供模板，优先参考本机默认文件 C:\Users\lenovo\Desktop\卓越运营PPT材料排版与样式参考.pdf，不可用时使用内置默认样式说明。
---

# PPT HTML

用于先生成可在浏览器预览、可打印为 PDF、后续也可转换为 PPTX 的 HTML 幻灯片。除非用户明确要求拆分文件，默认交付一个包含 HTML 与 CSS 的完整文件。

## 工作流程

1. 只在必要信息缺失时追问：主题、受众、原始材料、页数、语言、是否有模板或风格参考。
2. 如果用户提供 PPT、PDF、图片、网页或模板，先分析模板再写内容。重点提取版式结构、字体层级、配色、页眉页脚、图表样式、表格样式、章节页、信息密度和留白方式。
3. 如果用户没有提供模板，优先尝试读取本机默认参考文件：
   `C:\Users\lenovo\Desktop\卓越运营PPT材料排版与样式参考.pdf`
4. 如果默认 PDF 不存在或无法读取，再加载 `references/default-style-notes.md` 作为默认风格依据。
5. 先在内部形成幻灯片大纲，再生成 HTML。每一页必须有一个明确主信息。
6. 以 `assets/deck.html` 和 `assets/slide.css` 作为基础模板生成页面。
7. 交付前检查打印效果：16:9 页面、一页一张幻灯片、文字不溢出、表格不裁切、元素不重叠。

## 输出标准

- 使用 16:9 横版幻灯片。
- 每页使用 `<section class="slide ...">` 表示。
- 除非用户要求拆分文件，否则将 CSS 内联到 HTML 中。
- 文案要像 PPT，而不是长文章。
- 每页标题尽量表达结论、判断或动作，而不是泛泛的主题词。
- 多用结构化表达：KPI 卡片、对比表、时间线、流程图、矩阵、经营模型、问题树、重点提示框。
- 避免装饰性过强的背景、花哨渐变、营销落地页式 hero 和无信息量插画。
- 中文材料优先使用 Microsoft YaHei、PingFang SC、Noto Sans CJK、Arial 等字体。
- 默认采用克制的商务风格：浅色背景、清晰层级、统一间距、少量强调色。

## 默认风格

当用户没有提供模板时，先使用本机默认 PDF。无法读取 PDF 时，加载 `references/default-style-notes.md`。

默认风格方向是“卓越运营 / 企业经营 / 咨询汇报”类材料：

- 页面干净、结构清楚、信息密度较高。
- 强调标题、关键结论、表格、流程、指标和管理动作。
- 使用白色或浅灰背景，深色正文，蓝绿色或少量橙色作为强调色。
- 版面应服务于管理判断和执行沟通，而不是营销展示。

不要把桌面上的默认 PDF 复制进公开仓库，除非用户明确要求发布该文件。

## 资源说明

- `assets/deck.html`：单文件 HTML 起始模板，包含常见页面结构。
- `assets/slide.css`：可复用的 16:9、可打印幻灯片样式。
- `references/default-style-notes.md`：默认商务/卓越运营风格说明。
- `scripts/build_deck.py`：可选脚本，把结构化 JSON 幻灯片规格渲染成 HTML。

如果内容已经结构化，或者需要稳定复用同一套生成流程，优先使用脚本。如果用户要高定制、高设计感页面，可以直接基于 HTML/CSS 模板手工生成。

## JSON 渲染脚本

脚本输入示例：

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

运行方式：

```bash
python scripts/build_deck.py input.json output.html
```

当前支持的页面类型：`title`、`section`、`bullets`、`table`、`cards`、`timeline`。

## 质量检查

交付前至少检查：

- 是否一页只有一个主信息。
- 标题、正文、表格、卡片是否层级一致。
- 是否有文字溢出、遮挡或裁切。
- 是否适合直接在浏览器打开。
- 打印为 PDF 时是否每页对应一张幻灯片。
