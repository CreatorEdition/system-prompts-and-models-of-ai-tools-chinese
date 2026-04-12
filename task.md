# 当前任务

> 更新时间：2026-04-12

## 状态

- [x] 阅读 `README.md`、`task.md` 与 `.teamwork/` 目录
- [x] 审计 git 历史、工作区状态与目录结构
- [x] 识别高优先级问题：状态文档失真、异常目录名、Qoder 半迁移
- [x] 更新 `README.md` 反映当前目录结构与整理状态
- [x] 更新 `task.md` 反映真实进度与待收口事项
- [x] 建立 `.teamwork` 任务与进度记录
- [x] 规范化 `Bolt.new` 目录命名，移除隐藏字符影响
- [x] 确认 `阿里 Qoder/` 以子目录结构纳入版本管理
- [x] 翻译 Anthropic 首批英文资料（搜索指令 / 记忆系统 / XLSX 工具）
- [ ] 审阅其余未跟踪资料（Anthropic / OpenAI / Moonshot AI 等）
- [ ] 继续清理未提交文档并按主题分批提交

## 本次处理范围

- 修复 `README.md` 的更新时间与目录结构失真
- 修复 `task.md` 与实际仓库状态脱节的问题
- 补充 `.teamwork/tasks/` 与 `.teamwork/progress/` 记录，恢复协作上下文
- 将异常命名目录 `‎Bolt.new` 规范化为 `Bolt.new`
- 接受 `阿里 Qoder/` 从平铺文件向 `Qoder/` 子目录迁移的结构调整
- 完成 Anthropic 首批英文资料的高确定性翻译
- 不主动并入未审阅的新文档内容，避免把不同主题的整理混在同一提交中

## 待处理

- 继续处理 `Anthropic/` 下剩余英文资料（如 Browser Extensions、Core Models）
- 审核 `Anthropic/` 下新增提示词与工具文档的归档边界
- 审核 `OpenAI/` 下新增模型资料与 `Old/` 历史文件的保留策略
- 审核 `月之暗面（Moonshot AI）/Kimi K2.5.txt` 等新增资料是否满足收录标准
- 评估是否增加目录校验脚本，自动发现隐藏字符目录、占位符与重复路径
- 已补充仓库级 `.gitignore`，仅忽略系统与临时文件；当前未跟踪的正文资料不应通过忽略规则掩盖