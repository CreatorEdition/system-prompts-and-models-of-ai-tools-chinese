---
name: docx (Word文档处理)
description: 提供全面的文档创建、编辑和分析功能，支持修订(跟踪更改)、评论、保留格式和提取文本。
when_to_use: "当 Claude 需要处理专业文档 (.docx 文件) 时：(1) 创建新文档，(2) 修改或编辑内容，(3) 处理修订(被跟踪的更改)，(4) 添加评论，或进行任何其他文档任务"
version: 0.0.1
---

# DOCX 创建、编辑与分析

> 更新地址：[https://github.com/CreatorEdition/system-prompts-and-models-of-ai-tools-chinese]

## 概览

用户可能会要求你创建、编辑或分析 .docx 文件的内容。一个 .docx 文件本质上是一个 ZIP 压缩包，包含了 XML 文件以及你可以读取或编辑的其他资源。你拥有针对不同任务的不同工具和工作流。

## 工作流决策树

### 读取/分析内容
使用下方的 “提取文本” (Text extraction) 或 “读取原始 XML” (Raw XML access) 部分。

### 创建新文档
使用 “创建一个新的 Word 文档” (Creating a new Word document) 工作流。

### 编辑现有文档
- **你自己创建的文档 + 简单的更改**
  使用 “基础 OOXML 编辑” (Basic OOXML editing) 工作流。

- **其他人创建的文档**
  使用 **“红线标注重审工作流” (Redlining workflow)**（推荐默认项）。

- **法律、学术、商业或政府文档**
  使用 **“红线标注重审工作流” (Redlining workflow)**（强制要求）。

## 读取与分析内容

### 提取文本
如果你只需要读取文档的文本内容，你应该使用 pandoc 将文档转换为 markdown。Pandoc 提供了对于保留文档结构极佳的支持，并能显示修订记录：
```bash
# 将包含修订记录的文档转换为 markdown
pandoc --track-changes=all path-to-file.docx -o output.md
# 可选参数项: --track-changes=accept/reject/all
```

### 访问原始 XML (Raw XML access)
以下情况你需要访问原始 XML：评论、复杂格式化、文档结构、嵌入式媒体和元数据。要处理这些特性的任何一项，你都需要解包文档读取其原始 XML 内容。

#### 解包文件
`python ooxml/scripts/unpack.py <office_file> <output_directory>`

#### 关键文件结构
* `word/document.xml` - 主要文档正文内容
* `word/comments.xml` - document.xml 里面引用的评论
* `word/media/` - 嵌入的图像及其它媒体文件
* 修订（跟踪更改）操作使用 `<w:ins>` (插入) 和 `<w:del>` (删除) 标签

## 创建一个新的 Word 文档

当从头开始创建一个新的 Word 文档时，请使用 **docx-js**，它允许你利用 JavaScript/TypeScript 创建 Word 文档。

### 工作流
1. **强制项 - 通读整份文件**：完整从头到尾阅读 [`docx-js.md`](docx-js.md)（约 500 行）。**绝对不要在阅读此文件时设置任何范围限制。** 在着手开始文档创建前，必须阅读其全部文件内容以获取详细的语法、关键的排版格式规则以及最佳实践。
2. 使用 Document、Paragraph、TextRun 组件创建一个 JavaScript/TypeScript 文件（你可以假设所有的依赖项都已经安装，如果没有，请参考下方的依赖项部分）。
3. 使用 Packer.toBuffer() 导出为 .docx。

## 编辑现有的 Word 文档

在编辑现有的 Word 文档时，你需要基于原始的 Office Open XML (OOXML) 格式进行操作。包括解包 .docx 文件，编辑 XML 内容，最后再重新打包。

### 工作流
1. **强制项 - 通读整份文件**：完整从头到尾阅读 [`ooxml.md`](ooxml.md)（约 500 行）。**绝对不要在阅读此文件时设置任何范围限制。** 在继续操作之前，阅读完整的文件内容以获取详细语法、验证规则和代码范式。
2. 解包文档：`python ooxml/scripts/unpack.py <office_file> <output_directory>`
3. 编辑 XML 文件（主要指 `word/document.xml` 和 `word/comments.xml`）。
4. **关键**：在每次编辑后立即验证并修复所有发生的验证错误，然后再继续下一步骤：`python ooxml/scripts/validate.py <dir> --original <file>`
5. 打包最终文档：`python ooxml/scripts/pack.py <input_directory> <office_file>`

## 用于文档审阅的红线标注重审工作流 (Redlining workflow)

此工作流不仅允许你在 OOXML 中实施修订记录前通过 markdown 筹划出全面的修订，还允许你跟踪完整的变更状况。**关键**：为保证最终完整呈现的所有修订变动记录被记入，你必须有系统地实施所有的更改。

### 全面追踪修订变更系统工作流

1. **获取 markdown 展示结果**：使用 pandoc 将文档连带着所有跟踪更改记录转换成 markdown 文本：
```bash
   pandoc --track-changes=all path-to-file.docx -o current.md
```

2. **制定详细入微的变动清单**：制作包含一切需改动调整等各个修订待办项的一个详细检查清单，按先后执行次序陈列任务项：
   - 每个待办项都应以 `[ ]` 开头。
   - **不要使用 Markdown 行号**，因为它无法稳定映射到内部 XML 结构。
   - **应优先使用以下定位方式：**
     - 章节号或条款号（例如 `"Section 3.2"`、`"Article IV"`）
     - 原文中可唯一定位的编号
     - 可用于 `grep` 的唯一上下文片段或正则
     - 文档中的自然结构描述（例如“首段”“签名区块”）
   - 示例：`[ ] 第 8 节：将 "30 天" 改为 "60 天"（grep： "notice period of.*days prior"）`
   - 同时要考虑到 Word 的文本可能被拆分到多个 `<w:t>` 节点中，不能假设一段文字始终连续存放。
   - 保存输出名为： `revision-checklist.md`。

3. **配置搭稳建立能行起承轨变更履迹追踪等基设条件构筑运作体系 (Setup tracked changes infrastructure)**：
   - 实行解包释出这文档文件： `python ooxml/scripts/unpack.py <office_file> <output_directory>`
   - 执行装配运载搭架用之命令语： `python skills/docx/scripts/setup_redlining.py <unpacked_directory>`
   - 该脚本会自动完成以下设置：
     - 创建 `word/people.xml`，为修订记录建立作者信息。
     - 更新 `[Content_Types].xml`，纳入 `people.xml`。
     - 更新 `word/_rels/document.xml.rels`，加入对 `people.xml` 的关系声明。
     - 在 `word/settings.xml` 中加入 `<w:trackRevisions/>`，启用修订追踪。
     - 生成一个 8 位十六进制的 RSID（例如 `"6CEA06C3"`）。
     - 将生成出的 RSID 输出到终端，供后续使用。
   - **关键要求**：务必记录这个 RSID。后续所有涉及“修订追踪”的 XML 更改，都必须持续使用同一个 RSID。

4. **要成章法讲次序步步系统不乱条理推进地按清真单逐项应用履行那些要改之处的行动**：
   - **必须完整阅读 [`ooxml.md`](ooxml.md)**，尤其要仔细理解其中关于 “Tracked Change Patterns” 的部分。阅读时不要人为限制查看范围。
   - 如果将具体修改分派给子代理或其他执行单元，它们在动手前也必须完整阅读同一部分说明。
   - 按 `revision-checklist.md` 中的顺序逐项实施修改，不要跳项，也不要并发地随意改动。
   - 使用稳定的文本定位方式查找对应 XML 位置，并在每次修改后及时验证输出。
