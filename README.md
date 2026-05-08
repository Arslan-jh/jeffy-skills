# jeffy-skills

这是一个用于沉淀个人研究方法与自动化交付流程的 Skills 仓库。目前核心 Skill 是 `jf-analysis`，面向产品、公司、技术、概念、人物或复杂事件的系统性深度研究。

## jf-analysis：立体分析法

`jf-analysis` 采用「立体分析法（3D Analysis）」组织研究报告：

- **X轴：时间线因果链** —— 追踪研究对象从起源到当下的关键节点，回答「它是如何一步步走到今天的」。
- **Y轴：多因素并行展开** —— 在关键时间截面还原竞品、资本、技术、市场、政策、人物、舆论等力量如何同时作用。
- **Z轴：力量内部机制拆解** —— 深入拆解核心力量的内部结构、动机、约束条件和相互影响，解释「为什么会这样走」。

最终目标不是生成零散资料汇总，而是产出一份有因果链、有证据、有判断、有交付形态的深度研究报告。

## 输出形式

默认交付为：

1. 一份结构化 Markdown 研究报告；
2. 一份由 `scripts/md_to_pdf.py` 转换生成的 PDF 报告。

PDF 脚本基于 WeasyPrint 与 Python Markdown，内置封面、页眉页脚、标题层级、引用块、表格和列表样式。当前视觉主色为 `RGB(192, 0, 0)` / `#c00000` 红色，用于标题、分隔线、表头和强调元素。

## 主要文件

| 文件 | 说明 |
|---|---|
| `SKILL.md` | Skill 的核心说明，包含触发场景、研究流程、写作风格、报告结构和质检清单。 |
| `schema.json` | 立体分析法的结构化 schema，用于规范研究对象、X/Y/Z 三轴、洞察和输出要求。 |
| `scripts/md_to_pdf.py` | 将 Markdown 研究报告转换为 PDF 的脚本。 |

## 使用方式

完成 Markdown 报告后，可运行：

```bash
python scripts/md_to_pdf.py input.md output.pdf --title "研究对象名称" --author "jeffy"
```

如缺少依赖，可先安装：

```bash
pip install weasyprint markdown --break-system-packages
```
