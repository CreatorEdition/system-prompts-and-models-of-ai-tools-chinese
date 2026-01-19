# AI中文编程提示词项目

<div align="center">

> **Latest Update:** 2026-01-19
  
![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![许可](https://img.shields.io/badge/许可-MIT-green)
![贡献](https://img.shields.io/badge/欢迎-贡献-brightgreen)

</div>

## 📖 项目简介

本项目是对[system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)的中文翻译及扩充版本，旨在为中文开发者和AI爱好者提供各种流行AI编程工具的系统提示词和模型设计文档。通过这些资料，您可以深入了解各类AI助手的工作原理，以及如何更有效地与它们交互。

> **声明：** 本项目仅供学习研究使用。项目中的所有提示词和模型文档仅用于帮助开发者理解AI工具的工作原理。详细的免责声明请查看[DISCLAIMER.md](./DISCLAIMER.md)文件。

## 🚀 项目内容

本项目收录了超过 35+ 主流 AI 编程工具的系统提示词和模型设计文档，包括但不限于：

- **代码编辑器集成工具**: Cursor, VSCode Agent, Windsurf, Xcode, Augment Code, Trae (ByteDance)
- **AI 编程助手**: Devin AI, Replit, v0, Bolt, Cline, RooCode, Claude Code
- **主流大模型提示词**: ChatGPT (OpenAI), Grok (xAI), Claude (Anthropic), Gemini (Google)
- **国内厂商工具**: 豆包/Trae (字节跳动), Qoder (阿里), CodeBuddy (腾讯), Z.ai (智谱)
- **专业开发平台**: Lovable, Same.dev, Manus Agent, Leap.new, Amp
- **新兴 AI 工具**: Kiro, Emergent, Traycer AI, Poke, dia, Junie
- **企业级工具**: NotionAI, Perplexity
- **开发辅助工具**: Comet Assistant, Cluely, Orchids.app, Warp.dev
- **开源项目**: Bolt, Cline, RooCode, Lumo, Gemini CLI, Codex CLI
 

## 📂 目录结构

```
.
├── Cursor Prompts/               # Cursor 编辑器的提示词与工具
├── VSCode Agent/                 # VSCode Agent 多模型支持文档
├── Windsurf/                     # Windsurf 提示词与工具
├── Devin AI/                     # Devin AI 的系统提示词
├── Replit/                       # Replit 的提示词和工具配置
├── v0 Prompts and Tools/         # v0 的提示词和工具定义
├── Lovable/                      # Lovable AI 助手完整文档
├── Same.dev/                     # Same.dev 平台的提示词
├── Manus Agent Tools & Prompt/   # Manus Agent 的工具和提示词
├── Open Source prompts/          # 开源 AI 工具提示词集合
│   ├── Bolt/                     # Bolt AI 提示词
│   ├── Cline/                    # Cline 助手提示词
│   ├── RooCode/                  # RooCode 提示词
│   ├── Lumo/                     # Lumo 提示词
│   ├── Gemini CLI/               # Google Gemini CLI 系统提示词
│   └── Codex CLI/                # OpenAI Codex CLI 提示词
├── Google/                       # Google AI 工具集合 (Gemini, Antigravity)
├── Anthropic/                    # Anthropic Claude 全系 (含 Claude Code)
├── ChatGPT/                      # OpenAI ChatGPT 模型提示词
├── Grok/                         # xAI Grok 个性化与角色提示词
├── 字节跳动（ByteDance）/        # 字节系工具
│   ├── Trae.ai/                  # Trae 智能IDE
│   └── 豆包（dola、doubao）/     # 豆包编程助手
├── 腾讯 CodeBuddy Prompts/       # 腾讯 CodeBuddy 助手
├── 阿里 Qoder/                   # 阿里 Qoder 编程助手
├── 智谱清言（Z.ai）/             # 智谱 Z.ai 代码助手
├── Xcode/                        # Xcode AI 功能提示词
├── Augment Code/                 # Augment Code AI 编程工具
├── Amp/                          # Amp AI 开发平台
├── Kiro/                         # Kiro AI (Vibe/Spec/Mode)
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
├── Comet Assistant/              # Comet 助手系统提示词
├── Cluely/                       # Cluely 企业版与默认提示词
├── add_headers.py                # 批量添加标准头部的工具脚本
├── DISCLAIMER.md                 # 免责声明
└── LICENSE.md                    # MIT 许可证
```

## 🔍 使用方法

这些提示词和模型设计文档可以帮助您：

1. **了解AI编程工具的内部工作机制**
2. **优化您与AI编程工具的交互方式**
3. **为开发类似工具提供参考**
4. **学习AI代理设计的最佳实践**

## 🤝 贡献

欢迎贡献更多AI工具的中文翻译或改进现有翻译！请遵循以下步骤：

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-translation`)
3. 提交您的更改 (`git commit -m '添加对XX工具的翻译'`)
4. 推送到分支 (`git push origin feature/amazing-translation`)
5. 开启一个Pull Request

> **💡 提示：** 提交新文件时，请使用标准头部格式以保持规范统一：
>
> ```markdown
> # 产品名 文件名 系统提示
>
> > 此文件包含 "产品名" - "文件名" 的系统提示词
> > 更新时间：YYYY-MM-DD（如文件中含有日期）
> > 更新地址：[https://github.com/CreatorEdition/system-prompts-and-models-of-ai-tools-chinese]
>
> ---
> ```
>



## 📅 后续计划

本仓库将持续更新并增加以下内容：

- **中文编程Rules** - 为中文开发者提供更适合的编程规则和指南
- **更多AI工具提示词** - 持续追踪并翻译最新AI工具的系统提示词
- **提示词优化建议** - 针对中文用户的提示词使用技巧和优化方法
- **实践案例分享** - 收集在实际开发过程中使用这些提示词的成功案例

我致力于建立一个完整的中文AI工具资源库，帮助更多开发者充分利用AI辅助编程的潜力。

## ✨ 项目特色

- 📚 **全面覆盖**: 收录 35+ 主流和新兴 AI 编程工具
- 🔄 **持续更新**: 跟踪最新版本的提示词变化
- 🌏 **中文友好**: 为中文开发者提供本地化文档
- 🛠️ **实用性强**: 包含工具配置和实际应用案例
- 🎯 **结构清晰**: 按工具类型和功能分类整理

## 🔗 相关链接

### 主流工具官网
- [原始英文项目](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- [Cursor](https://cursor.sh/) | [Windsurf](https://codeium.com/windsurf) | [VSCode](https://code.visualstudio.com/)
- [Devin AI](https://www.cognition.ai/) | [Replit](https://replit.com/) | [v0](https://v0.dev/)
- [Lovable](https://lovable.dev/) | [Bolt](https://bolt.new/) | [Cline](https://github.com/cline/cline)
- [Anthropic Claude](https://www.anthropic.com/) | [Augment Code](https://augmentcode.com/)

### 新兴工具
- [Warp](https://www.warp.dev/) | [Leap.new](https://leap.new/) | [Same.dev](https://same.dev/)
- [Perplexity](https://www.perplexity.ai/) | [NotionAI](https://www.notion.so/product/ai)
- [Amp](https://withamp.com/) | [Kiro](https://kiro.ai/) | [Z.ai](https://z.ai/)

---

<div align="left">
  <sub>如有任何问题或建议，欢迎提交Issue</sub>
</div>

## 📜 许可

本项目采用MIT许可证 - 详见LICENSE文件

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=CreatorEdition/system-prompts-and-models-of-ai-tools-chinese&type=date&legend=top-left)](https://www.star-history.com/#CreatorEdition/system-prompts-and-models-of-ai-tools-chinese&type=date&legend=top-left)