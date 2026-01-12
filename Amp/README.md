# Sourcegraph 公司 Amp AI 的系统提示词 @update:https://github.com/CreatorEdition/system-prompts-and-models-of-ai-tools-chinese/

# 如何获取 [Amp](https://ampcode.com) 的系统提示词（System Prompt）

1. 在 VS Code 中登录 Amp
2. 向 Amp 发送一个简短查询
3. 按住 Alt（Windows）或 Option（macOS），单击工作区按钮

![](./view-thread-yaml.png)

4. 点击 “View Thread YAML” 查看会话的 YAML

# 说明

Amp 使用针对 Sonnet 4.x 调优的系统提示词，并将其他 LLM 以工具（“the oracle”）的形式注册其中。若要获取针对 `GPT-5` 调优的系统提示词，请在 VS Code 用户设置中添加以下配置，然后重复以上步骤：

```json
{
  "amp.url": "https://ampcode.com/",
  "amp.gpt5": true
}
```
