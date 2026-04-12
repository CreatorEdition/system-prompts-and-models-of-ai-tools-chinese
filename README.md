# AI 编程提示词中文项目

<div align="center">

> **最近更新：** 2026-04-12

![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![许可](https://img.shields.io/badge/许可-MIT-green)
![贡献](https://img.shields.io/badge/欢迎-贡献-brightgreen)

</div>

## 📖 项目简介

本项目是对 [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) 的中文翻译与扩展整理，旨在为中文开发者与 AI 爱好者提供常见 AI 编程工具的系统提示词、工具定义及相关模型说明文档。

这些资料可用于学习不同 AI 助手的行为方式、能力边界与交互逻辑，也可作为研究、对比分析和实践参考的素材库。

> **声明：** 本项目仅供学习与研究使用。仓库中的提示词和模型文档仅用于帮助开发者理解相关 AI 工具的工作机制。详细说明请参阅 [DISCLAIMER.md](./DISCLAIMER.md)。

## 📌 当前整理状态

- 当前仓库正在进行一轮结构清理与提交收口，已完成对文档状态失真和目录异常的首轮修复。
- `Anthropic/`、`OpenAI/`、`月之暗面（Moonshot AI）/` 等目录仍存在待审阅的新资料，后续会分批确认、整理并提交。
- `阿里 Qoder/` 已按产品子目录整理，当前以 `Qoder/` 为主；`Vesa/` 目录已预留但尚未正式纳入版本管理。
- `Bolt.new/` 目录名已标准化，避免隐藏字符导致的路径问题。

## 🚀 收录内容

本项目当前收录了 35+ 主流及新兴 AI 编程工具的系统提示词和模型设计资料，包括但不限于：

- **代码编辑器与 IDE 集成工具**：Cursor、VSCode Agent、Windsurf、Xcode、Augment Code、Trae
- **AI 编程助手与代理**：Devin AI、Replit、v0、Bolt.new、Claude Code、Cline、RooCode
- **主流大模型系统提示词**：ChatGPT（OpenAI）、Grok（xAI）、Claude（Anthropic）、Gemini（Google）
- **国内厂商相关工具**：豆包 / Trae（字节跳动）、Qoder（阿里）、CodeBuddy（腾讯）、Z.ai（智谱）、Kimi（月之暗面）
- **专业开发与生成平台**：Lovable、Same.dev、Manus Agent、Leap.new、Amp
- **新兴 AI 工具**：Kiro、Emergent、Traycer AI、Poke、dia、Junie
- **企业与效率工具**：Notion AI、Perplexity
- **开发辅助工具**：Comet Assistant、Cluely、Orchids.app、Warp.dev
- **开源项目与公开提示词**：Bolt、Cline、RooCode、Lumo、Gemini CLI、Codex CLI

## 📂 目录结构

```text
.
├── Amp/                          # Amp AI 开发平台
├── Anthropic/                    # Anthropic Claude 系列（含 Claude Code）
├── Augment Code/                 # Augment Code AI 编程工具
├── Bolt.new/                     # StackBlitz Bolt.new 提示词与工具
├── ChatGPT/                      # OpenAI ChatGPT 模型提示词
├── Cluely/                       # Cluely 企业版与默认提示词
├── Comet Assistant/              # Comet Assistant 系统提示词
├── Confer/                       # Confer 相关提示词
├── Cursor Prompts/               # Cursor 编辑器提示词与工具
├── Devin AI/                     # Devin AI 系统提示词
├── Emergent/                     # Emergent AI 提示词与工具
├── Google/                       # Google AI 工具集合（Gemini、Antigravity）
├── Grok（xAI）/                  # xAI Grok 个性化与角色提示词
├── Junie/                        # Junie AI 提示词
├── Kiro/                         # Kiro AI（Vibe / Spec / Mode）
├── Leap.new/                     # Leap.new 提示词与工具
├── Lovable/                      # Lovable AI 助手相关文档
├── Manus Agent Tools & Prompt/   # Manus Agent 工具与提示词
├── NotionAi/                     # Notion AI 提示词与工具
├── Open Source prompts/          # 开源 AI 工具提示词集合
│   ├── Bolt/                     # Bolt AI 提示词
│   ├── Cline/                    # Cline 助手提示词
│   ├── RooCode/                  # RooCode 提示词
│   ├── Lumo/                     # Lumo 提示词
│   ├── Gemini CLI/               # Gemini CLI 系统提示词
│   └── Codex CLI/                # Codex CLI 系统提示词
├── OpenAI/                       # OpenAI 核心模型、Agents 与历史资料
├── Orchids.app/                  # Orchids 决策与系统提示词
├── Perplexity/                   # Perplexity AI 提示词
├── Poke/                         # Poke Agent 多阶段提示词
├── Proton/                       # Proton 相关资料
├── Replit/                       # Replit 提示词与工具配置
├── Saharsh Gobinath/             # 第三方整理资料
├── Same.dev/                     # Same.dev 平台提示词
├── Traycer AI/                   # Traycer AI 计划与阶段模式
├── VSCode Agent/                 # VSCode Agent 多模型支持文档
├── Warp.dev/                     # Warp 终端 AI 提示词
├── Windsurf/                     # Windsurf 提示词与工具
├── Xcode/                        # Xcode AI 功能提示词
├── v0 Prompts and Tools/         # v0 提示词与工具定义
├── 字节跳动（ByteDance）/        # 字节系相关工具
│   ├── Trae.ai/                  # Trae 智能 IDE
│   └── 豆包（dola、doubao）/     # 豆包编程助手
├── 智谱清言（Z.ai）/             # 智谱 Z.ai 代码助手
├── 月之暗面（Moonshot AI）/      # Moonshot / Kimi 相关提示词
├── 腾讯 CodeBuddy Prompts/       # 腾讯 CodeBuddy 助手
├── 阿里 Qoder/                   # 阿里 Qoder 系列资料
│   └── Qoder/                    # Qoder 主产品提示词
├── DISCLAIMER.md                 # 免责声明
├── LICENSE.md                    # MIT 许可证
├── README.md                     # 项目说明
└── task.md                       # 当前整理任务与状态
```

## 🔍 这个项目能帮你做什么

这些提示词和模型文档可以帮助你：

1. 了解 AI 编程工具的内部工作方式。
2. 优化你与 AI 工具的交互方式。
3. 为开发类似产品提供参考。
4. 学习 AI Agent / Copilot 的设计思路。
5. 对比不同工具在提示词设计上的差异。

## 💡 使用场景

### 面向开发者

- 参考 Claude Code、Cursor 等工具的提示词设计方式进行代码审查辅助。
- 研究工具如何组织上下文、拆解问题与调用工具，用于 Bug 排查与修复。
- 观察不同 AI 助手如何处理代码结构调整，用于重构与优化。
- 借鉴系统提示词中对解释、总结与输出格式的约束方式，用于文档生成。

### 面向内容创作者

- 参考 Perplexity、Comet 等提示词中的信息组织方法。
- 分析不同系统提示对语言风格与任务边界的约束。
- 为中文场景做本地化表达和结构优化。

### 面向研究者与分析人员

- 对比不同产品的系统提示设计取向。
- 研究工具在规划、执行、拒答和安全策略上的差异。
- 基于这些材料整理横向对比报告和趋势观察。

### 面向团队与组织

- 统一整理常用提示词与工具资料。
- 作为新人培训与内部知识沉淀材料。
- 为团队内部的 AI 使用规范提供参考样例。

## ✨ 项目特色

- **覆盖较全**：收录 35+ 主流与新兴 AI 工具资料。
- **持续更新**：持续跟踪新的提示词版本与工具变化。
- **中文友好**：面向中文开发者做本地化整理。
- **实用导向**：兼顾学习价值与实际参考价值。
- **结构清晰**：按工具类型和用途分类整理。

## 🤝 如何贡献

欢迎一起补充更多 AI 工具的中文翻译，或改进现有内容。

### 1. 新增提示词或文档

1. Fork 本仓库。
2. 为对应工具创建目录（如目录尚不存在）。
3. 按现有结构添加文件，例如：

```text
Tool Name/
├── Prompt.txt          # 主系统提示词
├── Tools.json          # 工具/函数定义（如适用）
└── [Version].txt       # 特定版本提示词
```

4. 提交 Pull Request，并简要说明新增内容来源与适用范围。

### 2. 更新现有内容

- 核对更新内容的准确性。
- 在提交信息中写明版本或日期。
- 示例：`文档: 更新 Claude Code 提示词（2026-01-18）`

### 3. 反馈问题

- 先检查是否已有同类 Issue。
- 尽量提供具体文件路径、问题描述和对应截图或上下文。
- 如涉及翻译问题，建议同时附上原文与建议译法。

## 📋 Pull Request 建议模板

提交 PR 时，可以附上以下信息：

- **类型**：新增 / 更新 / 修复 / 文档
- **工具/分类**：对应的 AI 工具名称或目录
- **变更说明**：本次修改的主要内容
- **校验方式**：你如何确认内容准确
- **关联问题**：相关 Issue 或讨论链接

## 📅 后续计划

- 继续审阅并分批提交 `Anthropic/`、`OpenAI/` 与 `月之暗面（Moonshot AI）/` 下的新资料。
- 继续补齐更适合中文开发者的 Rules、实践建议与索引说明。
- 逐步引入更明确的目录规范和协作记录，降低后续整理成本。
- 视情况补充自动化校验脚本，用于扫描占位符、重复目录与异常命名。

## 🔗 相关链接

### 主流工具官网

- [原始英文项目](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- [Cursor](https://cursor.sh/) | [Windsurf](https://codeium.com/windsurf) | [VS Code](https://code.visualstudio.com/)
- [Devin AI](https://www.cognition.ai/) | [Replit](https://replit.com/) | [v0](https://v0.dev/)
- [Lovable](https://lovable.dev/) | [Bolt.new](https://bolt.new/) | [Cline](https://github.com/cline/cline)
- [Anthropic Claude](https://www.anthropic.com/) | [Augment Code](https://augmentcode.com/)

### 新兴工具

- [Warp](https://www.warp.dev/) | [Leap.new](https://leap.new/) | [Same.dev](https://same.dev/)
- [Perplexity](https://www.perplexity.ai/) | [Notion AI](https://www.notion.so/product/ai)
- [Amp](https://withamp.com/) | [Kiro](https://kiro.ai/) | [Z.ai](https://z.ai/)

---

<div align="left">
  <sub>如有任何问题或建议，欢迎提交 Issue。</sub>
</div>

## 📜 许可证

本项目采用 MIT 许可证，详见 [LICENSE.md](./LICENSE.md)。
