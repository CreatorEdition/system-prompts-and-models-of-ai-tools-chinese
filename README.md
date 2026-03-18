# AI 编程提示词中文项目

<div align="center">

> **最近更新：** 2026-03-01

![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![许可](https://img.shields.io/badge/许可-MIT-green)
![贡献](https://img.shields.io/badge/欢迎-贡献-brightgreen)

</div>

## 📖 项目简介

本项目是对 [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) 的中文翻译与扩展整理，旨在为中文开发者与 AI 爱好者提供常见 AI 编程工具的系统提示词、工具定义及相关模型说明文档。

通过这些资料，你可以更深入地了解不同 AI 助手的行为方式、能力边界与交互逻辑，并将其用于学习、研究、对比分析和实践参考。

> **声明：** 本项目仅供学习与研究使用。仓库中的提示词和模型文档仅用于帮助开发者理解相关 AI 工具的工作机制。详细说明请参阅 [DISCLAIMER.md](./DISCLAIMER.md)。

## 🚀 收录内容

本项目当前收录了 35+ 主流及新兴 AI 编程工具的系统提示词和模型设计资料，包括但不限于：

- **代码编辑器与 IDE 集成工具**：Cursor、VSCode Agent、Windsurf、Xcode、Augment Code、Trae
- **AI 编程助手与代理**：Devin AI、Replit、v0、Bolt、Cline、RooCode、Claude Code
- **主流大模型系统提示词**：ChatGPT（OpenAI）、Grok（xAI）、Claude（Anthropic）、Gemini（Google）
- **国内厂商相关工具**：豆包 / Trae（字节跳动）、Qoder（阿里）、CodeBuddy（腾讯）、Z.ai（智谱）
- **专业开发与生成平台**：Lovable、Same.dev、Manus Agent、Leap.new、Amp
- **新兴 AI 工具**：Kiro、Emergent、Traycer AI、Poke、dia、Junie
- **企业与效率工具**：Notion AI、Perplexity
- **开发辅助工具**：Comet Assistant、Cluely、Orchids.app、Warp.dev
- **开源项目与公开提示词**：Bolt、Cline、RooCode、Lumo、Gemini CLI、Codex CLI

## 📂 目录结构

```text
.
├── Cursor Prompts/               # Cursor 编辑器提示词与工具
├── VSCode Agent/                 # VSCode Agent 多模型支持文档
├── Windsurf/                     # Windsurf 提示词与工具
├── Devin AI/                     # Devin AI 系统提示词
├── Replit/                       # Replit 提示词与工具配置
├── v0 Prompts and Tools/         # v0 提示词与工具定义
├── Lovable/                      # Lovable AI 助手相关文档
├── Same.dev/                     # Same.dev 平台提示词
├── Manus Agent Tools & Prompt/   # Manus Agent 工具与提示词
├── Open Source prompts/          # 开源 AI 工具提示词集合
│   ├── Bolt/                     # Bolt AI 提示词
│   ├── Cline/                    # Cline 助手提示词
│   ├── RooCode/                  # RooCode 提示词
│   ├── Lumo/                     # Lumo 提示词
│   ├── Gemini CLI/               # Gemini CLI 系统提示词
│   └── Codex CLI/                # Codex CLI 系统提示词
├── Google/                       # Google AI 工具集合（Gemini、Antigravity）
├── Anthropic/                    # Anthropic Claude 系列（含 Claude Code）
├── ChatGPT/                      # OpenAI ChatGPT 模型提示词
├── Grok/                         # xAI Grok 个性化与角色提示词
├── 字节跳动（ByteDance）/        # 字节系相关工具
│   ├── Trae.ai/                  # Trae 智能 IDE
│   └── 豆包（dola、doubao）/     # 豆包编程助手
├── 腾讯 CodeBuddy Prompts/       # 腾讯 CodeBuddy 助手
├── 阿里 Qoder/                   # 阿里 Qoder 编程助手
├── 智谱清言（Z.ai）/             # 智谱 Z.ai 代码助手
├── Xcode/                        # Xcode AI 功能提示词
├── Augment Code/                 # Augment Code AI 编程工具
├── Amp/                          # Amp AI 开发平台
├── Kiro/                         # Kiro AI（Vibe / Spec / Mode）
├── Emergent/                     # Emergent AI 提示词与工具
├── Traycer AI/                   # Traycer AI 计划与阶段模式
├── Leap.new/                     # Leap.new 提示词与工具
├── Poke/                         # Poke Agent 多阶段提示词
├── Orchids.app/                  # Orchids 决策与系统提示词
├── dia/                          # dia AI 提示词
├── Warp.dev/                     # Warp 终端 AI 提示词
├── Junie/                        # Junie AI 提示词
├── NotionAi/                     # Notion AI 提示词与工具
├── Perplexity/                   # Perplexity AI 提示词
├── Comet Assistant/              # Comet Assistant 系统提示词
├── Cluely/                       # Cluely 企业版与默认提示词
├── add_headers.py                # 批量添加标准头部的工具脚本
├── DISCLAIMER.md                 # 免责声明
└── LICENSE.md                    # MIT 许可证
````

## 🔍 这个项目能帮你做什么

这些提示词和模型文档可以帮助你：

1. 了解 AI 编程工具的内部工作方式
2. 优化你与 AI 工具的交互方式
3. 为开发类似产品提供参考
4. 学习 AI Agent / Copilot 的设计思路
5. 对比不同工具在提示词设计上的差异

## 💡 使用场景

### 🎯 面向开发者

* **代码审查辅助**：参考 Claude Code、Cursor 等工具的提示词设计方式
* **Bug 排查与修复**：研究工具如何组织上下文、拆解问题与调用工具
* **重构与优化**：观察不同 AI 助手如何处理代码结构调整
* **文档生成**：借鉴系统提示词中对解释、总结与输出格式的约束方式

### 📝 面向内容创作者

* **写作辅助**：参考 Perplexity、Comet 等提示词中的信息组织方法
* **内容改写与翻译**：分析不同系统提示对语言风格与任务边界的约束
* **多语言内容适配**：为中文场景做本地化表达和结构优化

### 🎨 面向设计师与无代码创作者

* **快速原型搭建**：参考 Lovable、v0、Replit 等工具的提示词结构
* **界面与交互建议**：观察 AI 助手如何生成设计建议与组件描述
* **组件生成与页面规划**：理解工具如何把自然语言需求转成前端产物

### 🔬 面向研究者与分析人员

* **提示词研究**：对比不同产品的系统提示设计取向
* **能力边界分析**：研究工具在规划、执行、拒答和安全策略上的差异
* **报告与综述写作**：基于这些材料整理横向对比报告和趋势观察

### 🏢 面向团队与组织

* **知识沉淀**：统一整理常用提示词与工具资料
* **新人培训**：帮助团队成员快速理解不同 AI 工具的特点
* **流程标准化**：为团队内部的 AI 使用规范提供参考样例

## ✨ 项目特色

* 📚 **覆盖较全**：收录 35+ 主流与新兴 AI 工具资料
* 🔄 **持续更新**：持续跟踪新的提示词版本与工具变化
* 🌏 **中文友好**：面向中文开发者做本地化整理
* 🛠️ **实用导向**：兼顾学习价值与实际参考价值
* 🎯 **结构清晰**：按工具类型和用途分类整理

## 🤝 如何贡献

欢迎一起补充更多 AI 工具的中文翻译，或改进现有内容。

### 1. 新增提示词或文档

1. Fork 本仓库
2. 为对应工具创建目录（如目录尚不存在）
3. 按现有结构添加文件，例如：

```text
Tool Name/
├── Prompt.txt          # 主系统提示词
├── Tools.json          # 工具/函数定义（如适用）
└── [Version].txt       # 特定版本提示词
```

4. 提交 Pull Request，并简要说明新增内容来源与适用范围

### 2. 更新现有内容

* 核对更新内容的准确性
* 在提交信息中写明版本或日期
* 示例：`update: Claude Code prompt - 2026-01-18`

### 3. 反馈问题

* 先检查是否已有同类 Issue
* 尽量提供具体文件路径、问题描述和对应截图/上下文
* 如涉及翻译问题，建议同时附上原文与建议译法

## ✅ 贡献建议

提交内容时，建议尽量满足以下几点：

* **准确性**：确认提示词版本、来源和内容无误
* **一致性**：保持目录结构、标题格式和头部说明统一
* **可读性**：避免生硬直译，优先自然、准确的中文表达
* **可追溯性**：尽量注明原始来源或更新依据
* **完整性**：新增文件时补齐说明、日期和必要上下文

> **💡 提示：** 提交新文件时，建议使用统一头部格式：

```markdown
# 产品名 文件名 系统提示

> 此文件包含“产品名 - 文件名”的系统提示词
> 更新时间：YYYY-MM-DD（如文件中含有日期）
> 更新地址：[https://github.com/CreatorEdition/system-prompts-and-models-of-ai-tools-chinese]

---
```

## 📋 Pull Request 建议模板

提交 PR 时，可以附上以下信息：

* **类型**：新增 / 更新 / 修复 / 文档
* **工具/分类**：对应的 AI 工具名称或目录
* **变更说明**：本次修改的主要内容
* **校验方式**：你如何确认内容准确
* **关联问题**：相关 Issue 或讨论链接

## 📅 后续计划

本仓库将持续更新并逐步增加以下内容：

* **中文编程 Rules**：更适合中文开发者的规则与实践建议
* **更多 AI 工具提示词**：持续跟进新的系统提示词与工具定义
* **提示词优化建议**：总结面向中文用户的使用技巧
* **实践案例分享**：收集真实开发场景中的应用示例

希望逐步将这个仓库建设成一个更完整的中文 AI 工具资料库，帮助更多开发者高效使用 AI 辅助编程工具。

## 🔗 相关链接

### 主流工具官网

* [原始英文项目](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
* [Cursor](https://cursor.sh/) | [Windsurf](https://codeium.com/windsurf) | [VS Code](https://code.visualstudio.com/)
* [Devin AI](https://www.cognition.ai/) | [Replit](https://replit.com/) | [v0](https://v0.dev/)
* [Lovable](https://lovable.dev/) | [Bolt](https://bolt.new/) | [Cline](https://github.com/cline/cline)
* [Anthropic Claude](https://www.anthropic.com/) | [Augment Code](https://augmentcode.com/)

### 新兴工具

* [Warp](https://www.warp.dev/) | [Leap.new](https://leap.new/) | [Same.dev](https://same.dev/)
* [Perplexity](https://www.perplexity.ai/) | [Notion AI](https://www.notion.so/product/ai)
* [Amp](https://withamp.com/) | [Kiro](https://kiro.ai/) | [Z.ai](https://z.ai/)

---

<div align="left">
  <sub>如有任何问题或建议，欢迎提交 Issue。</sub>
</div>

## 📜 许可证

本项目采用 MIT 许可证，详见 [LICENSE.md](./LICENSE.md)。

<div align="center">

**如果这个项目对你有帮助，欢迎点亮一颗 Star ⭐**

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=CreatorEdition/system-prompts-and-models-of-ai-tools-chinese\&type=date\&legend=top-left)](https://www.star-history.com/#CreatorEdition/system-prompts-and-models-of-ai-tools-chinese&type=date&legend=top-left)

[⬆ 返回顶部](#ai-编程提示词中文项目)

</div>