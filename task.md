# 上游同步任务（2026-04-13）

## 检查范围
- `upstream-x1xhlol/main`
- `upstream-asgeirtj/main`
- 对比基线：`origin/main`

## upstream-x1xhlol/main

### 主要更新
- 新增英文目录并迁移文件：`CodeBuddy Prompts/`、`Qoder/`、`Trae/`、`Z.ai Code/`。
- 多产品提示词与工具定义有批量更新（如 `Anthropic/`、`OpenAI/`、`Google/`、`VSCode Agent/`、`Windsurf/` 等）。
- 存在目录结构重排（如 Cursor 子目录上提、部分文件重命名/移动）。

### 本地已覆盖（含中文映射目录）
- `CodeBuddy Prompts/Chat Prompt.txt` -> `腾讯 CodeBuddy Prompts/Chat Prompt.txt`（已覆盖）
- `CodeBuddy Prompts/Craft Prompt.txt` -> `腾讯 CodeBuddy Prompts/Craft Prompt.txt`（已覆盖）
- `Qoder/prompt.txt` -> `阿里 Qoder/Qoder/prompt.txt`（已覆盖）
- `Qoder/Quest Action.txt` -> `阿里 Qoder/Qoder/Quest Action.txt`（已覆盖）
- `Qoder/Quest Design.txt` -> `阿里 Qoder/Qoder/Quest Design.txt`（已覆盖）
- `Trae/Builder Prompt.txt` -> `字节跳动（ByteDance）/Trae.ai/Builder Prompt.txt`（已覆盖）
- `Trae/Builder Tools.json` -> `字节跳动（ByteDance）/Trae.ai/Builder Tools.json`（已覆盖）
- `Trae/Chat Prompt.txt` -> `字节跳动（ByteDance）/Trae.ai/Chat Prompt.txt`（已覆盖）
- `Z.ai Code/prompt.txt` -> `智谱清言（Z.ai）/code-cli-prompt.txt`（已覆盖，文件名存在本地约定差异）

### 本次新增落地
- 文档侧新增：`task.md`、`CONTRIBUTING.md`。
- 提示词文件新增：`Anthropic/Claude Code 2.0.txt`、`Anthropic/Claude Code/Prompt.txt`、`Anthropic/Claude Code/Tools.json`、`Anthropic/Claude for Chrome/Prompt.txt`、`Anthropic/Claude for Chrome/Tools.json`、`Anthropic/Sonnet 4.5 Prompt.txt`、`Cursor Prompts/Agent CLI Prompt 2025-08-07.txt`、`Cursor Prompts/Agent Prompt 2.0.txt`、`Cursor Prompts/Agent Prompt 2025-09-03.txt`、`Cursor Prompts/Agent Prompt v1.0.txt`、`Cursor Prompts/Agent Prompt v1.2.txt`、`Cursor Prompts/Agent Tools v1.0.json`、`Cursor Prompts/Chat Prompt.txt`。

### 待后续处理
- 对 `Anthropic/Claude Sonnet 4.6.txt`、`Anthropic/`、`OpenAI/`、`Google/` 等大批量更新做逐文件差异核对与翻译同步。
- 评估是否引入上游英文目录重排，或继续维持本仓库中文目录映射策略。

## upstream-asgeirtj/main

### 主要更新
- 新增英文贡献指南：`CONTRIBUTING.md`。
- 大规模目录扁平化与重组：`OpenAI/`、`Google/`、`xAI/`、`Misc/` 增补/迁移明显。
- 模型版本文件更新密集（尤其 OpenAI Codex/GPT-5.x 与 Google Gemini 系列）。

### 本地已覆盖（含中文映射目录）
- `xAI/grok-3.md`、`xAI/grok-4.md` 等可映射到 `Grok（xAI）/Core_Models/`（已覆盖）
- `OpenAI/codex/gpt-5.md`、`OpenAI/codex/gpt-5.4.md` 等可映射到 `OpenAI/Codex/`（已覆盖）
- `Google/gemini-3-pro.md`、`Google/gemini-3-flash.md`、`Google/gemini-diffusion.md` 可映射到 `Google/Gemini/`（已覆盖）

### 本次新增落地
- 基于上游贡献规范新增本仓库中文版 `CONTRIBUTING.md`（见同目录文件）。

### 待后续处理
- `Misc/` 新增条目（如 `meta-ai.md`、`t3.chat.md` 等）本地尚未建立对应中文收录策略。
- 上游路径规范（如 `OpenAI/codex/` 小写子目录）与本地既有目录大小写/层级不一致，需统一规则后再批量同步。

## 本轮同步（2026-04-15）

### 已确认并从上游补齐的缺失文件
- `Anthropic/Claude Sonnet 4.6.txt`（来自 `upstream-x1xhlol/main`）
- `Anthropic/claude.ai-human-readable.md`
- `Anthropic/claude-cowork.md`
- `Anthropic/claude-desktop-code.md`
- `Anthropic/claude-opus-4.6.md`
- `Anthropic/claude-opus-4.6-no-tools.md`
- `Anthropic/claude-sonnet-4.6.md`
- `Anthropic/claude-sonnet-4.6-no-tools.md`
- `Anthropic/raw/claude-opus-4.6-raw.md`
- `Anthropic/raw/claude-sonnet-4.6-raw.md`
- `OpenAI/gpt-5.3-instant.md`
- `OpenAI/gpt-5.4-thinking.md`
- `Google/nano-banana-2-api.md`
- `Misc/meta-ai.md`

### 已有本地等价内容，暂不重复新建
- `OpenAI/`、`Google/`、`xAI/`、`Misc/` 中其余大部分新增路径，本地已有旧层级或中文映射版本，可在后续批次中按“是否需要保留上游新扁平路径”再决定是否补新文件。
- `Misc/Notion-AI.md`、`Misc/qwen-3.6-plus.md` 等条目已有本地同名或近似同名中文内容，优先在后续批次中决定是否保留双路径。

### 翻译批次状态
- 已启动子代理并行处理 Anthropic 4.6 系列、Anthropic 说明类文档、OpenAI/Google/Misc 增量翻译。
- 本轮先完成原文同步入库，避免遗漏；子代理产出的中文版本在下一步直接覆盖这些新文件。

### 待下一步处理
- 校对并落地 `Anthropic/Claude Sonnet 4.6.txt`、`Anthropic/claude-opus-4.6.md`、`Anthropic/claude-sonnet-4.6.md` 的完整中文译文。
- 评估是否补齐 `Anthropic/old/` 历史文件到本地，以便与 upstream-asgeirtj 的新结构对齐。
- 决定是否为 `OpenAI/`、`Google/`、`Misc/` 新扁平路径保留与旧层级并存的双轨收录策略。
## 本轮同步（2026-04-17）

### 上游增量检查结果
- 已重新抓取 `upstream-x1xhlol/main` 与 `upstream-asgeirtj/main`。
- 与上次自动化记录相比，`upstream-asgeirtj/main` 新增了 `Anthropic/Official/claude-opus-4.7.md`，并继续更新 `Anthropic/claude-opus-4.6.md`、`Anthropic/claude-sonnet-4.6.md`、`OpenAI/gpt-5.4-thinking.md` 等既有文件。
- `Anthropic/Official/README.md` 仅为上游档案链接说明，不属于新的提示词正文文件，当前先记录来源，不在本地单独建立对应中文文件。

### 本地缺失并已补齐的文件
- `Anthropic/Official/claude-opus-4.7.md` -> `Anthropic/claude-opus-4.7.md`

### 本轮待合并的翻译批次
- Anthropic 4.6 主提示词：`Anthropic/claude-opus-4.6.md`、`Anthropic/claude-opus-4.6-no-tools.md`
- Anthropic 4.6 Sonnet 系列：`Anthropic/claude-sonnet-4.6.md`、`Anthropic/claude-sonnet-4.6-no-tools.md`、`Anthropic/Claude Sonnet 4.6.txt`
- Anthropic 说明与辅助文档：`Anthropic/claude.ai-human-readable.md`、`Anthropic/claude-cowork.md`、`Anthropic/claude-desktop-code.md`、`Anthropic/claude-opus-4.7.md`
- Anthropic raw：`Anthropic/raw/claude-opus-4.6-raw.md`、`Anthropic/raw/claude-sonnet-4.6-raw.md`
- OpenAI / Google / Misc：`OpenAI/gpt-5.3-instant.md`、`OpenAI/gpt-5.4-thinking.md`、`Google/nano-banana-2-api.md`、`Misc/meta-ai.md`

### 下一步处理原则
- 继续维持“先补齐缺失原文，再就地覆盖中文译文”的策略，避免上游新增文件漏收。
- 对上游目录重排但本地已有稳定中文映射的路径，优先记录映射关系，不重复制造双份同义文件。
