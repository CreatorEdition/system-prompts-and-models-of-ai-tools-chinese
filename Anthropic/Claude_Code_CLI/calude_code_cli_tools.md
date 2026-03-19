# Claude Code 内部工具技术参考

> **Claude Code 内部工具的完整技术文档**

本文档提供 Claude Code 内部工具的完整技术细节，包括参数结构、实现行为和使用模式。


### Claude Sonnet 4.5

**技术详情：**
- **模型 ID：** `claude-sonnet-4-5-20250929`
- **模型名称：** Sonnet 4.5
- **发布日期：** 2025 年 9 月 29 日
- **当前日期：** 2025 年 10 月 17 日
- **知识截止时间：** 2025 年 1 月

---

## 目录

1. [文件操作](#file-operations)
2. [执行工具](#execution-tools)
3. [代理管理](#agent-management)
4. [规划与跟踪](#planning--tracking)
5. [用户交互](#user-interaction)
6. [网页操作](#web-operations)
7. [IDE 集成](#ide-integration)
8. [MCP 资源](#mcp-resources)
9. [完整实现摘要](#complete-implementation-summary)

---

## 文件操作

### Read 工具

**用途：** 从本地文件系统读取文件内容，支持多模态文件和局部读取。

**技术实现：**

Read 工具提供直接的文件系统访问能力，并带有智能内容解析：
- 在具备相应权限的前提下访问机器上的任意文件
- 默认读取上限：从文件开头读取 2000 行
- 行截断：每行最多 2000 个字符
- 输出格式：类似 `cat -n`，行号从 1 开始
- 行前缀格式：`空格 + 行号 + 制表符 + 内容`

**多模态能力：**

该工具通过专门的处理器支持多种文件格式：
- **图片（PNG、JPG 等）：** 由于 Claude Code 是多模态模型，可直接以视觉内容形式呈现
- **PDF 文件：** 按页处理，同时提取文本和视觉内容
- **Jupyter 笔记本（`.ipynb`）：** 返回所有单元格及其输出，整合代码、文本和可视化内容

**错误处理：**

- 空文件会触发系统提醒警告，而不是返回正文内容
- 无效路径会返回相应错误信息
- 权限不足错误会直接暴露给用户

**限制：**

- 不能读取目录（应改用 Bash `ls` 命令）
- 必须使用绝对路径
- 完全支持截图和临时文件

**参数结构：**

```typescript
interface ReadTool {
  file_path: string;      // Absolute path to file (required)
  offset?: number;        // Starting line number (optional)
  limit?: number;         // Number of lines to read (optional)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "additionalProperties": false,
  "required": ["file_path"],
  "properties": {
    "file_path": {
      "type": "string",
      "description": "The absolute path to the file to read"
    },
    "offset": {
      "type": "number",
      "description": "The line number to start reading from. Only provide if the file is too large to read at once"
    },
    "limit": {
      "type": "number",
      "description": "The number of lines to read. Only provide if the file is too large to read at once."
    }
  }
}
```

**行为摘要：**
- 默认读取：前 2000 行
- 行号方式：从 1 开始（`cat -n` 风格）
- 行截断：2000 字符
- 状态：无状态，可多次调用

---

### Write 工具

**用途：** 创建新文件，或在内建安全机制保护下完整覆盖已有文件。

**技术实现：**

Write 工具提供原子化文件写入能力，并强制执行安全检查：
- 完整覆盖已有文件（不支持局部更新）
- 对已有文件强制执行“先读后写”校验
- 要求使用绝对路径（不支持相对路径）
- 原子写入：文件要么完整写入，要么保持不变

**安全机制：**

内建的防误覆盖保护包括：
- **先读后写约束：** 如果当前会话中尚未读取某个已存在文件，系统会直接让写入失败
- **会话跟踪：** 维护当前会话中已读取文件的记录，用于校验写入是否合法
- **最佳实践约束：** 对已有文件优先使用 Edit 工具，Write 只应用于新文件

**设计理念：**

- 修改已有文件时优先使用 Edit 工具
- 仅在真正创建新文件时使用 Write
- 除非用户明确要求，否则避免主动创建文档文件（如 `*.md`、`README`）
- 除非用户明确要求，否则不要插入 emoji

**参数结构：**

```typescript
interface WriteTool {
  file_path: string;      // Absolute path (must be absolute, not relative) (required)
  content: string;        // Complete file content (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["file_path", "content"],
  "additionalProperties": false,
  "properties": {
    "file_path": {
      "type": "string",
      "description": "要写入文件的绝对路径（必须为绝对路径，不能是相对路径）"
    },
    "content": {
      "type": "string",
      "description": "要写入文件的内容"
    }
  }
}
```

**强制规则：**
- 先读后写：系统会对已有文件强制执行
- 路径校验：必须是绝对路径
- 会话状态：跟踪当前对话中已经读取过的文件

---

### Edit Tool

**用途：** 在文件中执行精确、外科手术式的字符串替换，要求完全匹配。

**技术实现：**

Edit 工具通过精确字符串匹配来执行替换：
- 基于精确字符串匹配工作（不是正则，也不是模糊模式）
- 要求在当前会话中先读取过对应文件
- 保留文件编码和换行符
- 原子操作（文件要么完整更新，要么完全不变）

**字符串匹配机制：**

该工具使用精确字符串匹配，并具有以下行为：
- **唯一性要求：** `old_string` 在文件中必须恰好匹配一次（除非设置 `replace_all=true`）
- **空白敏感：** 会严格保留源文件中的缩进（Tab / 空格）
- **行号前缀处理：** 真正的文件内容是行号前缀（`空格 + 行号 + 制表符`）之后的部分
- **失败条件：** 如果 `old_string` 不唯一，操作会失败（以避免歧义编辑）

**替换模式：**

1. **单次替换（默认）：** 替换一个唯一匹配项
   - 如果 `old_string` 出现多次或一次也不出现，则操作失败
   - 使用场景：对特定代码位置做精细修改

2. **全部替换（`replace_all=true`）：** 替换所有匹配项
   - 适用于整个文件内的变量重命名
   - 不要求唯一匹配
   - 使用场景：重构、批量替换

**安全机制：**

- **Read-before-edit enforcement:** System validates file was read at least once in conversation
- **Content validation:** `new_string` must differ from `old_string`
- **Indentation preservation:** Exact whitespace matching from Read tool output
- **Session tracking:** Maintains list of read files for validation

**参数结构：**

```typescript
interface EditTool {
  file_path: string;      // Absolute path (must be absolute, not relative) (required)
  old_string: string;     // Exact text to find and replace (required)
  new_string: string;     // Replacement text (must be different from old_string) (required)
  replace_all?: boolean;  // Replace all occurrences (default: false)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["file_path", "old_string", "new_string"],
  "additionalProperties": false,
  "properties": {
    "file_path": {
      "type": "string",
      "description": "The absolute path to the file to modify"
    },
    "old_string": {
      "type": "string",
      "description": "The text to replace"
    },
    "new_string": {
      "type": "string",
      "description": "The text to replace it with (must be different from old_string)"
    },
    "replace_all": {
      "type": "boolean",
      "default": false,
      "description": "Replace all occurences of old_string (default false)"
    }
  }
}
```

**Common Use Cases:**
- Bug fixes in specific code sections
- Updating function implementations
- Variable/function renaming (with `replace_all`)
- Configuration changes
- Documentation updates

---

### Glob Tool

**Purpose:** Fast file pattern matching that works with any codebase size.

**技术实现：**

High-performance file search using glob patterns:
- Fast pattern matching optimized for any codebase size
- Returns file paths sorted by modification time (most recent first)
- Supports parallel execution (call multiple times in single message)
- Integrates with Task tool for complex searches

**Pattern Syntax:**

Standard glob patterns supported:
- `*` - Matches any characters except `/` (single directory level)
- `**` - Matches any characters including `/` (recursive, all subdirectories)
- `?` - Matches exactly one character
- `{a,b}` - Matches either `a` or `b` (alternation)
- `[abc]` - Matches any single character in brackets (character class)
- `[a-z]` - Matches any character in range
- `[!abc]` - Matches any character NOT in brackets (negation)

**Common Patterns:**
- `**/*.js` - All JavaScript files recursively
- `src/**/*.{ts,tsx}` - All TypeScript files in src/ directory
- `test/**/*.[jt]s` - All .js or .ts files in test/ directory
- `*.json` - All JSON files in current directory

**参数结构：**

```typescript
interface GlobTool {
  pattern: string;        // Glob pattern to match files against (required)
  path?: string;         // Directory to search in (defaults to cwd)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["pattern"],
  "additionalProperties": false,
  "properties": {
    "pattern": {
      "type": "string",
      "description": "The glob pattern to match files against"
    },
    "path": {
      "type": "string",
      "description": "The directory to search in. If not specified, the current working directory will be used. IMPORTANT: Omit this field to use the default directory. DO NOT enter \"undefined\" or \"null\" - simply omit it for the default behavior. Must be a valid directory path if provided."
    }
  }
}
```

**Important Notes:**
- Omit `path` field to use current working directory (default behavior)
- Never set `path` to "undefined" or "null" - simply omit the field
- Results sorted by modification time (most recent first)
- Works efficiently even with large codebases

---

### Grep Tool

**Purpose:** High-performance content search using ripgrep.

**技术实现：**
- "A powerful search tool **built on ripgrep**"
- "**ALWAYS** use Grep for search tasks. **NEVER** invoke `grep` or `rg` as a Bash command. The Grep tool has been optimized for correct permissions and access"
- "Supports **full regex syntax** (e.g., \"log.*Error\", \"function\\s+\\w+\")"
- "**Output modes: \"content\" shows matching lines, \"files_with_matches\" shows only file paths (default), \"count\" shows match counts**"
- "Pattern syntax: Uses **ripgrep (not grep)** - literal braces need escaping (use `interface\\{\\}` to find `interface{}` in Go code)"
- "**Multiline matching: By default patterns match within single lines only**. For cross-line patterns like `struct \\{[\\s\\S]*?field`, use `multiline: true`"

**Tool Access:**
- "Use Task tool for open-ended searches requiring multiple rounds"
- "You can call multiple tools in a single response. It is always better to speculatively perform multiple searches in parallel"

**Parameters:**
```typescript
interface GrepTool {
  pattern: string;              // Regex pattern to search for (required)
  path?: string;                // File or directory to search in (defaults to cwd)
  output_mode?: 'content' | 'files_with_matches' | 'count';  // Default: "files_with_matches"
  glob?: string;                // Glob pattern to filter files (e.g., "*.js", "*.{ts,tsx}")
  type?: string;                // File type (js, py, rust, go, java, etc.) - more efficient than include
  '-i'?: boolean;               // Case insensitive search
  '-n'?: boolean;               // Show line numbers (requires output_mode: "content")
  '-A'?: number;                // Lines after match (requires output_mode: "content")
  '-B'?: number;                // Lines before match (requires output_mode: "content")
  '-C'?: number;                // Lines before AND after (requires output_mode: "content")
  multiline?: boolean;          // Enable multiline mode (default: false)
  head_limit?: number;          // Limit output to first N lines/entries
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["pattern"],
  "additionalProperties": false,
  "properties": {
    "pattern": {
      "type": "string",
      "description": "The regular expression pattern to search for in file contents"
    },
    "path": {
      "type": "string",
      "description": "File or directory to search in (rg PATH). Defaults to current working directory."
    },
    "output_mode": {
      "type": "string",
      "enum": ["content", "files_with_matches", "count"],
      "description": "Output mode: \"content\" shows matching lines (supports -A/-B/-C context, -n line numbers, head_limit), \"files_with_matches\" shows file paths (supports head_limit), \"count\" shows match counts (supports head_limit). Defaults to \"files_with_matches\"."
    },
    "glob": {
      "type": "string",
      "description": "Glob pattern to filter files (e.g. \"*.js\", \"*.{ts,tsx}\") - maps to rg --glob"
    },
    "type": {
      "type": "string",
      "description": "File type to search (rg --type). Common types: js, py, rust, go, java, etc. More efficient than include for standard file types."
    },
    "-i": {
      "type": "boolean",
      "description": "Case insensitive search (rg -i)"
    },
    "-n": {
      "type": "boolean",
      "description": "Show line numbers in output (rg -n). Requires output_mode: \"content\", ignored otherwise."
    },
    "-A": {
      "type": "number",
      "description": "Number of lines to show after each match (rg -A). Requires output_mode: \"content\", ignored otherwise."
    },
    "-B": {
      "type": "number",
      "description": "Number of lines to show before each match (rg -B). Requires output_mode: \"content\", ignored otherwise."
    },
    "-C": {
      "type": "number",
      "description": "Number of lines to show before and after each match (rg -C). Requires output_mode: \"content\", ignored otherwise."
    },
    "multiline": {
      "type": "boolean",
      "description": "Enable multiline mode where . matches newlines and patterns can span lines (rg -U --multiline-dotall). Default: false."
    },
    "head_limit": {
      "type": "number",
      "description": "Limit output to first N lines/entries, equivalent to \"| head -N\". Works across all output modes: content (limits output lines), files_with_matches (limits file paths), count (limits count entries). When unspecified, shows all results from ripgrep."
    }
  }
}
```

**Core Implementation:**
- Uses ripgrep binary (explicitly stated)
- Default output_mode: "files_with_matches"
- Context flags (-A/-B/-C) only work with output_mode: "content"
- Multiline mode disabled by default (patterns match single lines only)

---

### NotebookEdit Tool

**Purpose:** Edit Jupyter notebook cells with replace, insert, delete operations.

**技术实现：**
- "Completely replaces the contents of a specific cell in a Jupyter notebook (.ipynb file)"
- "The notebook_path parameter must be an **absolute path, not a relative path**"
- "The cell_number is **0-indexed**"
- "Use **edit_mode=insert** to add a new cell at the index specified by cell_number"
- "Use **edit_mode=delete** to delete the cell at the index specified by cell_number"

**Parameters:**
```typescript
interface NotebookEditTool {
  notebook_path: string;      // Absolute path to .ipynb file (required, must be absolute)
  new_source: string;         // New cell content (required)
  cell_id?: string;           // Cell ID to edit/insert after
  cell_type?: 'code' | 'markdown';  // Cell type (required for edit_mode=insert)
  edit_mode?: 'replace' | 'insert' | 'delete';  // Default: "replace"
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["notebook_path", "new_source"],
  "additionalProperties": false,
  "properties": {
    "notebook_path": {
      "type": "string",
      "description": "The absolute path to the Jupyter notebook file to edit (must be absolute, not relative)"
    },
    "new_source": {
      "type": "string",
      "description": "The new source for the cell"
    },
    "cell_id": {
      "type": "string",
      "description": "The ID of the cell to edit. When inserting a new cell, the new cell will be inserted after the cell with this ID, or at the beginning if not specified."
    },
    "cell_type": {
      "type": "string",
      "enum": ["code", "markdown"],
      "description": "The type of the cell (code or markdown). If not specified, it defaults to the current cell type. If using edit_mode=insert, this is required."
    },
    "edit_mode": {
      "type": "string",
      "enum": ["replace", "insert", "delete"],
      "description": "The type of edit to make (replace, insert, delete). Defaults to replace."
    }
  }
}
```

**Cell Indexing:**
- 0-indexed (first cell is index 0)
- Identifies cells by cell_id
- When inserting, new cell added after specified cell_id

---

## Execution Tools

### Bash Tool

**Purpose:** Execute commands in a persistent shell session with state preservation.

**技术实现：**
- "Executes a given bash command in a **persistent shell session** with optional timeout"
- "The command argument is required"
- "You can specify an optional timeout in milliseconds (up to **600000ms / 10 minutes**). If not specified, commands will timeout after **120000ms (2 minutes)**"
- "If the output exceeds **30000 characters**, output will be truncated before being returned to you"
- "You can use the `run_in_background` parameter to run the command in the background, which allows you to continue working while the command runs"
- "**Never use `run_in_background` to run 'sleep' as it will return immediately**. You do not need to use '&' at the end of the command when using this parameter"

**Command Restrictions:**
- "**Avoid** using Bash with the `find`, `grep`, `cat`, `head`, `tail`, `sed`, `awk`, or `echo` commands, unless explicitly instructed or when these commands are truly necessary for the task"
- "**NEVER** use bash for file operations (cat/head/tail, grep, find, sed/awk, echo >/cat <<EOF)"

**Multiple Commands:**
- "When issuing multiple commands: **If the commands are independent** and can run in parallel, make **multiple Bash tool calls in a single message**"
- "**If the commands depend on each other** and must run sequentially, use a single Bash call with '&&' to chain them together"
- "Use ';' only when you need to run commands sequentially but don't care if earlier commands fail"
- "**DO NOT use newlines to separate commands** (newlines are ok in quoted strings)"

**Working Directory:**
- "Try to maintain your current working directory throughout the session by **using absolute paths and avoiding usage of `cd`**. You may use `cd` if the User explicitly requests it"

**Parameters:**
```typescript
interface BashTool {
  command: string;              // Shell command to execute (required)
  description?: string;         // Clear, concise description (5-10 words)
  timeout?: number;             // Milliseconds (max 600000)
  run_in_background?: boolean;  // Run command in background (default: false)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["command"],
  "additionalProperties": false,
  "properties": {
    "command": {
      "type": "string",
      "description": "The command to execute"
    },
    "description": {
      "type": "string",
      "description": "Clear, concise description of what this command does in 5-10 words, in active voice. Examples:\nInput: ls\nOutput: List files in current directory\n\nInput: git status\nOutput: Show working tree status\n\nInput: npm install\nOutput: Install package dependencies\n\nInput: mkdir foo\nOutput: Create directory 'foo'"
    },
    "timeout": {
      "type": "number",
      "description": "Optional timeout in milliseconds (max 600000)"
    },
    "run_in_background": {
      "type": "boolean",
      "description": "Set to true to run this command in the background. Use BashOutput to read the output later."
    }
  }
}
```

**Operational Limits:**
- Default timeout: 120000ms (2 minutes)
- Maximum timeout: 600000ms (10 minutes)
- Output truncated at 30000 characters

**Git Safety:**
- "**NEVER** update the git config"
- "**NEVER** run destructive/irreversible git commands (like push --force, hard reset, etc) unless the user explicitly requests them"
- "**NEVER** skip hooks (--no-verify, --no-gpg-sign, etc) unless the user explicitly requests it"
- "**NEVER** run force push to main/master, warn the user if they request it"

---

### BashOutput Tool

**Purpose:** Retrieve incremental output from background shells.

**技术实现：**
- "Retrieves output from a running or completed background bash shell"
- "Takes a shell_id parameter identifying the shell"
- "**Always returns only new output since the last check**"
- "Returns stdout and stderr output along with shell status"
- "Supports optional regex filtering to show only lines matching a pattern"
- "Any lines that do not match will **no longer be available to read**" (when using filter)

**Parameters:**
```typescript
interface BashOutputTool {
  bash_id: string;        // ID of background shell (required)
  filter?: string;        // Optional regex to filter output lines
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["bash_id"],
  "additionalProperties": false,
  "properties": {
    "bash_id": {
      "type": "string",
      "description": "The ID of the background shell to retrieve output from"
    },
    "filter": {
      "type": "string",
      "description": "Optional regular expression to filter the output lines. Only lines matching this regex will be included in the result. Any lines that do not match will no longer be available to read."
    }
  }
}
```

**Behavior:**
- Returns ONLY new output since last check
- Non-blocking (returns immediately)
- Filter permanently removes non-matching lines

---

### KillShell Tool

**Purpose:** Terminate background bash shells.

**技术实现：**
- "Kills a running background bash shell by its ID"
- "Takes a shell_id parameter identifying the shell to kill"
- "Returns a success or failure status"

**Parameters:**
```typescript
interface KillShellTool {
  shell_id: string;       // ID of shell to kill (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["shell_id"],
  "additionalProperties": false,
  "properties": {
    "shell_id": {
      "type": "string",
      "description": "The ID of the background shell to kill"
    }
  }
}
```

---

## Agent Management

### Task Tool

**Purpose:** Launch autonomous sub-agents with specialized tool access.

**技术实现：**
- "Launch a new agent to handle complex, multi-step tasks **autonomously**"
- Available agent types and the tools they have access to:
  - **general-purpose**: "General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. **When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you**" (Tools: **\***)
  - **Explore**: "Fast agent specialized for exploring codebases. Use this when you need to quickly find files by patterns (eg. \"src/components/**/*.tsx\"), search code for keywords (eg. \"API endpoints\"), or answer questions about the codebase (eg. \"how do API endpoints work?\"). **When calling this agent, specify the desired thoroughness level: \"quick\" for basic searches, \"medium\" for moderate exploration, or \"very thorough\" for comprehensive analysis**" (Tools: **Glob, Grep, Read, Bash**)
  - **statusline-setup**: "Use this agent to configure the user's Claude Code status line setting" (Tools: **Read, Edit**)
  - **output-style-setup**: "Use this agent to create a Claude Code output style" (Tools: **Read, Write, Edit, Glob, Grep**)

**When NOT to use:**
- "If you want to read a specific file path, use the Read or Glob tool instead of the Agent tool, to find the match more quickly"
- "If you are searching for a specific class definition like \"class Foo\", use the Glob tool instead, to find the match more quickly"
- "If you are searching for code within a specific file or set of 2-3 files, use the Read tool instead of the Agent tool, to find the match more quickly"
- "Other tasks that are not related to the agent descriptions above"

**Agent Behavior:**
- "Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a **single message with multiple tool uses**"
- "When the agent is done, it will return a **single message** back to you. The result returned by the agent is **not visible to the user**"
- "For agents that run in the background, you will need to use AgentOutputTool to retrieve their results once they are done"
- "**Each agent invocation is stateless**. You will not be able to send additional messages to the agent, nor will the agent be able to communicate with you outside of its final report"
- "Your prompt should contain a **highly detailed task description** for the agent to perform autonomously and you should specify exactly what information the agent should return back to you in its final and only message to you"
- "The agent's outputs should generally be **trusted**"

**Parameters:**
```typescript
interface TaskTool {
  prompt: string;           // Detailed task description for agent (required)
  description: string;      // Short 3-5 word task summary (required)
  subagent_type: string;    // Type of specialized agent (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["description", "prompt", "subagent_type"],
  "additionalProperties": false,
  "properties": {
    "description": {
      "type": "string",
      "description": "A short (3-5 word) description of the task"
    },
    "prompt": {
      "type": "string",
      "description": "The task for the agent to perform"
    },
    "subagent_type": {
      "type": "string",
      "description": "The type of specialized agent to use for this task"
    }
  }
}
```

**Technical Tool Access:**
- general-purpose: ALL tools (*)
- Explore: Glob, Grep, Read, Bash
- statusline-setup: Read, Edit
- output-style-setup: Read, Write, Edit, Glob, Grep

**Thoroughness Levels (Explore Agent):**
- "quick" - basic searches
- "medium" - moderate exploration
- "very thorough" - comprehensive analysis

---

### Skill Tool

**Purpose:** Execute user-defined skills.

**技术实现：**
- "Execute a skill within the main conversation"
- "When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively"
- "Invoke skills using this tool with the **skill name only (no arguments)**"
- "When you invoke a skill, you will see <command-message>The \"{name}\" skill is loading</command-message>"
- "The skill's prompt will expand and provide detailed instructions on how to complete the task"
- "**Only use skills listed in <available_skills> below**"
- "**Do not invoke a skill that is already running**"
- "**Do not use this tool for built-in CLI commands (like /help, /clear, etc.)**"

**Parameters:**
```typescript
interface SkillTool {
  command: string;        // Skill name only, no arguments (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["command"],
  "additionalProperties": false,
  "properties": {
    "command": {
      "type": "string",
      "description": "The skill name (no arguments). E.g., \"pdf\" or \"xlsx\""
    }
  }
}
```

---

### SlashCommand Tool

**Purpose:** Execute custom slash commands from user configuration.

**技术实现：**
- "Execute a slash command within the main conversation"
- "**IMPORTANT - Intent Matching:** Before starting any task, CHECK if the user's request matches one of the slash commands listed below"
- "When you use this tool or when a user types a slash command, you will see <command-message>{name} is running…</command-message> **followed by the expanded prompt**"
- "For example, if .claude/commands/foo.md contains \"Print today's date\", then /foo expands to that prompt in the next message"
- "When a user requests multiple slash commands, execute **each one sequentially** and check for <command-message>{name} is running…</command-message> to verify each has been processed"
- "**Do not invoke a command that is already running**"
- "**Only use this tool for custom slash commands** that appear in the Available Commands list below. Do NOT use for: Built-in CLI commands, Commands not shown in the list, Commands you think might exist but aren't listed"

**Parameters:**
```typescript
interface SlashCommandTool {
  command: string;        // Slash command with arguments (e.g., "/review-pr 123") (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["command"],
  "additionalProperties": false,
  "properties": {
    "command": {
      "type": "string",
      "description": "The slash command to execute with its arguments, e.g., \"/review-pr 123\""
    }
  }
}
```

**Command Expansion:**
- Commands defined in `.claude/commands/*.md`
- Prompt text expands in next message
- Execute sequentially if multiple requested

---

## Planning & Tracking

### TodoWrite Tool

**Purpose:** Create and manage structured task lists for current session.

**技术实现：**
- "Use this tool to create and manage a **structured task list for your current coding session**"
- "This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user"
- "It also helps the user understand the progress of the task and overall progress of their requests"

**When to Use This Tool:**
1. "**Complex multi-step tasks** - When a task requires 3 or more distinct steps or actions"
2. "**Non-trivial and complex tasks** - Tasks that require careful planning or multiple operations"
3. "**User explicitly requests todo list** - When the user directly asks you to use the todo list"
4. "**User provides multiple tasks** - When users provide a list of things to be done (numbered or comma-separated)"
5. "**After receiving new instructions** - Immediately capture user requirements as todos"
6. "**When you start working on a task** - Mark it as in_progress BEFORE beginning work. **Ideally you should only have one todo as in_progress at a time**"
7. "**After completing a task** - Mark it as completed and add any new follow-up tasks discovered during implementation"

**When NOT to Use This Tool:**
- "There is only a single, straightforward task"
- "The task is trivial and tracking it provides no organizational benefit"
- "The task can be completed in less than 3 trivial steps"
- "The task is purely conversational or informational"
- "NOTE that you should **not use this tool if there is only one trivial task to do**. In this case you are better off just doing the task directly"

**Task Management:**
- "Update task status in real-time as you work"
- "Mark tasks complete **IMMEDIATELY** after finishing (**don't batch completions**)"
- "**Exactly ONE task must be in_progress at any time (not less, not more)**"
- "Complete current tasks before starting new ones"
- "Remove tasks that are no longer relevant from the list entirely"

**Task Completion Requirements:**
- "**ONLY** mark a task as completed when you have **FULLY** accomplished it"
- "If you encounter errors, blockers, or cannot finish, keep the task as in_progress"
- "When blocked, create a new task describing what needs to be resolved"
- "Never mark a task as completed if: Tests are failing, Implementation is partial, You encountered unresolved errors, You couldn't find necessary files or dependencies"

**Task Breakdown:**
- "Create specific, actionable items"
- "Break complex tasks into smaller, manageable steps"
- "Use clear, descriptive task names"
- "Always provide both forms: content: \"Fix authentication bug\", activeForm: \"Fixing authentication bug\""

**Parameters:**
```typescript
interface TodoWriteTool {
  todos: TodoItem[];      // Array of todo items (required)
}

interface TodoItem {
  content: string;          // Imperative form: what needs to be done (required, minLength: 1)
  status: 'pending' | 'in_progress' | 'completed';  // (required)
  activeForm: string;       // Present continuous: what's being done (required, minLength: 1)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["todos"],
  "additionalProperties": false,
  "properties": {
    "todos": {
      "type": "array",
      "description": "The updated todo list",
      "items": {
        "type": "object",
        "required": ["content", "status", "activeForm"],
        "additionalProperties": false,
        "properties": {
          "content": {
            "type": "string",
            "minLength": 1,
            "description": "Imperative form: what needs to be done"
          },
          "status": {
            "type": "string",
            "enum": ["pending", "in_progress", "completed"],
            "description": "Task status"
          },
          "activeForm": {
            "type": "string",
            "minLength": 1,
            "description": "Present continuous form: what's being done"
          }
        }
      }
    }
  }
}
```

**Critical Rule:**
- "It is critical that you mark todos as completed **as soon as you are done** with a task. **Do not batch up multiple tasks before marking them as completed**"

---

### ExitPlanMode Tool

**Purpose:** Exit planning mode after creating implementation plan.

**技术实现：**
- "Use this tool when you are in plan mode and have finished presenting your plan and are ready to code. This will prompt the user to exit plan mode"
- "**IMPORTANT: Only use this tool when the task requires planning the implementation steps of a task that requires writing code**"
- "**For research tasks where you're gathering information, searching files, reading files or in general trying to understand the codebase - do NOT use this tool**"

**Handling Ambiguity in Plans:**
- "Before using this tool, ensure your plan is clear and unambiguous. If there are multiple valid approaches or unclear requirements:"
  1. "Use the AskUserQuestion tool to clarify with the user"
  2. "Ask about specific implementation choices (e.g., architectural patterns, which library to use)"
  3. "Clarify any assumptions that could affect the implementation"
  4. "**Only proceed with ExitPlanMode after resolving ambiguities**"

**Parameters:**
```typescript
interface ExitPlanModeTool {
  plan: string;         // Implementation plan (supports markdown) (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["plan"],
  "additionalProperties": false,
  "properties": {
    "plan": {
      "type": "string",
      "description": "The plan you came up with, that you want to run by the user for approval. Supports markdown. The plan should be pretty concise."
    }
  }
}
```

**When to Use:**
- After detailed planning for implementation tasks
- Before starting to write code
- NOT for research/exploration tasks

---

## User Interaction

### AskUserQuestion Tool

**Purpose:** Ask user questions with structured multiple-choice options.

**技术实现：**
- "Use this tool when you need to ask the user questions during execution"
- "This allows you to: 1. Gather user preferences or requirements, 2. Clarify ambiguous instructions, 3. Get decisions on implementation choices as you work, 4. Offer choices to the user about what direction to take"
- "**Users will always be able to select \"Other\" to provide custom text input**"
- "Use **multiSelect: true** to allow multiple answers to be selected for a question"

**Parameters:**
```typescript
interface AskUserQuestionTool {
  questions: Question[];      // Questions to ask (1-4 questions) (required, minItems: 1, maxItems: 4)
  answers?: Record<string, string>;  // User answers collected
}

interface Question {
  question: string;           // Complete question (required)
  header: string;            // Very short label (max 12 chars) (required)
  multiSelect: boolean;      // Allow multiple selections (required)
  options: Option[];         // Available choices (2-4 options) (required, minItems: 2, maxItems: 4)
}

interface Option {
  label: string;             // Display text (1-5 words, concise) (required)
  description: string;       // Explanation of choice (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["questions"],
  "additionalProperties": false,
  "properties": {
    "questions": {
      "type": "array",
      "description": "Questions to ask the user (1-4 questions)",
      "minItems": 1,
      "maxItems": 4,
      "items": {
        "type": "object",
        "required": ["question", "header", "options", "multiSelect"],
        "additionalProperties": false,
        "properties": {
          "question": {
            "type": "string",
            "description": "The complete question to ask the user. Should be clear, specific, and end with a question mark. Example: \"Which library should we use for date formatting?\" If multiSelect is true, phrase it accordingly, e.g. \"Which features do you want to enable?\""
          },
          "header": {
            "type": "string",
            "description": "Very short label displayed as a chip/tag (max 12 chars). Examples: \"Auth method\", \"Library\", \"Approach\"."
          },
          "multiSelect": {
            "type": "boolean",
            "description": "Set to true to allow the user to select multiple options instead of just one. Use when choices are not mutually exclusive."
          },
          "options": {
            "type": "array",
            "description": "The available choices for this question. Must have 2-4 options. Each option should be a distinct, mutually exclusive choice (unless multiSelect is enabled). There should be no 'Other' option, that will be provided automatically.",
            "minItems": 2,
            "maxItems": 4,
            "items": {
              "type": "object",
              "required": ["label", "description"],
              "additionalProperties": false,
              "properties": {
                "label": {
                  "type": "string",
                  "description": "The display text for this option that the user will see and select. Should be concise (1-5 words) and clearly describe the choice."
                },
                "description": {
                  "type": "string",
                  "description": "Explanation of what this option means or what will happen if chosen. Useful for providing context about trade-offs or implications."
                }
              }
            }
          }
        }
      }
    },
    "answers": {
      "type": "object",
      "description": "User answers collected by the permission component",
      "additionalProperties": {
        "type": "string"
      }
    }
  }
}
```

**Technical Constraints:**
- 1-4 questions per call
- 2-4 options per question
- Header: max 12 characters
- Option label: 1-5 words
- "Other" option automatically added (don't include it)
- multiSelect must be specified (not optional)

---

## Web Operations

### WebFetch Tool

**Purpose:** Fetch and analyze web content using AI.

**技术实现：**
- "Fetches content from a specified URL and processes it using an AI model"
- "Takes a URL and a prompt as input"
- "Fetches the URL content, **converts HTML to markdown**"
- "Processes the content with the prompt using a **small, fast model**"
- "Returns the model's response about the content"
- "Includes a self-cleaning **15-minute cache** for faster responses when repeatedly accessing the same URL"
- "**IMPORTANT: If an MCP-provided web fetch tool is available, prefer using that tool instead of this one**, as it may have fewer restrictions. All MCP-provided tools start with \"mcp__\""
- "The URL must be a fully-formed valid URL"
- "**HTTP URLs will be automatically upgraded to HTTPS**"
- "Results may be summarized if the content is very large"
- "**When a URL redirects to a different host, the tool will inform you and provide the redirect URL in a special format. You should then make a new WebFetch request with the redirect URL** to fetch the content"

**Parameters:**
```typescript
interface WebFetchTool {
  url: string;            // Fully-formed valid URL (required, format: uri)
  prompt: string;         // Prompt to run on fetched content (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["url", "prompt"],
  "additionalProperties": false,
  "properties": {
    "url": {
      "type": "string",
      "format": "uri",
      "description": "The URL to fetch content from"
    },
    "prompt": {
      "type": "string",
      "description": "The prompt to run on the fetched content"
    }
  }
}
```

**Technical Behaviors:**
- HTTP→HTTPS automatic upgrade
- 15-minute self-cleaning cache
- HTML→Markdown conversion
- Small fast model for processing
- Redirect handling requires new request

---

### WebSearch Tool

**Purpose:** Search the web for current information.

**技术实现：**
- "Allows Claude to search the web and use the results to inform responses"
- "Provides up-to-date information for current events and recent data"
- "Returns search result information formatted as search result blocks"
- "Domain filtering is supported to include or block specific websites"
- "**Web search is only available in the US**"
- "**Account for \"Today's date\" in <env>. For example, if <env> says \"Today's date: 2025-07-01\", and the user wants the latest docs, do not use 2024 in the search query. Use 2025**"

**Parameters:**
```typescript
interface WebSearchTool {
  query: string;                  // Search query (min 2 chars) (required, minLength: 2)
  allowed_domains?: string[];     // Only include results from these domains
  blocked_domains?: string[];     // Never include results from these domains
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["query"],
  "additionalProperties": false,
  "properties": {
    "query": {
      "type": "string",
      "minLength": 2,
      "description": "The search query to use"
    },
    "allowed_domains": {
      "type": "array",
      "description": "Only include search results from these domains",
      "items": {
        "type": "string"
      }
    },
    "blocked_domains": {
      "type": "array",
      "description": "Never include search results from these domains",
      "items": {
        "type": "string"
      }
    }
  }
}
```

**Technical Limitations:**
- Minimum query length: 2 characters
- Only available in US
- Must account for current date in queries

---

## IDE Integration

### getDiagnostics Tool

**Purpose:** Get language diagnostics from VS Code.

**技术实现：**
- "Get language diagnostics from VS Code"

**Parameters:**
```typescript
interface GetDiagnosticsTool {
  uri?: string;         // Optional file URI to get diagnostics for
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "uri": {
      "type": "string",
      "description": "Optional file URI to get diagnostics for. If not provided, gets diagnostics for all files."
    }
  }
}
```

**Behavior:**
- Queries VS Code language server
- Returns errors, warnings, info messages
- Can filter by specific file or get all diagnostics

---

### executeCode Tool

**Purpose:** Execute Python code in Jupyter kernel.

**技术实现：**
- "Execute python code in the Jupyter kernel for the current notebook file"
- "**All code will be executed in the current Jupyter kernel**"
- "**Avoid declaring variables or modifying the state of the kernel unless the user explicitly asks for it**"
- "**Any code executed will persist across calls to this tool, unless the kernel has been restarted**"

**Parameters:**
```typescript
interface ExecuteCodeTool {
  code: string;         // Python code to be executed (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["code"],
  "additionalProperties": false,
  "properties": {
    "code": {
      "type": "string",
      "description": "The code to be executed on the kernel."
    }
  }
}
```

**Technical State Persistence:**
- Code executes in current Jupyter kernel
- State persists across calls (variables, imports, etc.)
- State cleared only on kernel restart
- Avoid modifying kernel state unless requested

---

## MCP Resources

### ListMcpResourcesTool

**Purpose:** List available resources from MCP servers.

**Parameters:**
```typescript
interface ListMcpResourcesTool {
  server?: string;      // Optional: filter by server name
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "server": {
      "type": "string",
      "description": "Optional: filter by server name"
    }
  }
}
```

---

### ReadMcpResourceTool

**Purpose:** Read specific resource from MCP server.

**Parameters:**
```typescript
interface ReadMcpResourceTool {
  server: string;       // MCP server name (required)
  uri: string;          // Resource URI (required)
}
```

**JSON Schema 细节：**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["server", "uri"],
  "additionalProperties": false,
  "properties": {
    "server": {
      "type": "string",
      "description": "MCP server name"
    },
    "uri": {
      "type": "string",
      "description": "Resource URI"
    }
  }
}
```

---

## Complete Implementation Summary

### Technical Specifications:

**Operational Limits:**
- Read: Default 2000 lines, 2000 char line truncation
- Bash: Default 120000ms (2 min), Max 600000ms (10 min), 30000 char output truncation
- WebFetch: 15-minute self-cleaning cache
- WebSearch: Minimum 2 char query, US only
- Glob: Sorted by modification time
- Grep: Default output_mode is "files_with_matches"

**Enforcement Mechanisms:**
- Write/Edit: MUST read file first (system enforced, will fail if not)
- Edit: MUST read at least once in conversation
- Edit: FAILS if old_string not unique (unless replace_all)
- TodoWrite: Exactly ONE task in_progress at a time
- TodoWrite: Both content and activeForm required
- NotebookEdit: 0-indexed cells
- BashOutput: Returns ONLY new output since last check

**Agent Tool Access Matrix:**
- general-purpose: * (ALL tools)
- Explore: Glob, Grep, Read, Bash
- statusline-setup: Read, Edit
- output-style-setup: Read, Write, Edit, Glob, Grep

**Technology Stack:**
- Grep: Powered by ripgrep (explicitly stated)
- WebFetch: Uses small fast model for processing
- WebFetch: Converts HTML to markdown
- executeCode: Executes in Jupyter kernel, state persists

**Behavioral Characteristics:**
- Read: Returns cat -n format (spaces + line number + tab + content)
- Read: Multimodal (images presented visually, PDFs page by page, notebooks with all cells)
- Read: Empty file triggers system reminder warning
- Bash: Persistent shell session, state maintained
- Bash: Never use run_in_background with sleep
- Bash: Prefer absolute paths over cd
- Task: Agents are stateless, return single final report
- Task: Launch multiple agents in single message for parallel execution
- TodoWrite: Mark completed IMMEDIATELY, don't batch
- WebFetch: HTTP auto-upgraded to HTTPS
- WebSearch: Must account for current date in env
- BashOutput: Filter permanently removes non-matching lines
- Explore agent: Has thoroughness levels (quick, medium, very thorough)

**Command Chaining Patterns:**
- Independent commands: Multiple Bash calls in single message (parallel)
- Dependent commands: Single Bash call with && (sequential with error propagation)
- Don't care about failure: Use ; (sequential without error propagation)
- Never use newlines to separate commands

**Operational Constraints:**
- Read: Cannot read directories (use Bash ls)
- Write: Never create docs unless requested
- Edit: Never include line number prefix in old_string/new_string
- Bash: Avoid find, grep, cat, head, tail, sed, awk, echo
- Bash: Never update git config, never skip hooks, never force push to main/master
- Skill: Do not invoke if already running
- SlashCommand: Only use custom commands in Available Commands list

### Implementation Details Not Exposed:

The following details are internal to Claude Code and not exposed through the tool interface:
- Specific npm packages or libraries used internally
- Internal implementation code and algorithms
- Storage mechanisms (in-memory vs file-based vs database)
- Internal class structures and architecture patterns
- Low-level system integration details

---

**Document Version:** 4.0 (Technical Reference for Users)
**Last Updated:** 2025-10-17
**Source:** Claude Code Internal Tool Definitions + Official Documentation
**Claude Code Version:** Sonnet 4.5 (claude-sonnet-4-5-20250929)
