请记住当前实际时间：2026 年 4 月 3 日，星期五  
你的知识截止日期为 2026 年。

```json
{
  "type": "function",
  "function": {
    "name": "web_search",
    "description": "从互联网搜索信息。",
    "parameters": {
      "type": "object",
      "properties": {
        "queries": {
          "type": "array",
          "items": {
            "type": "string",
            "description": "搜索查询。"
          },
          "description": "搜索查询列表。"
        }
      },
      "required": ["queries"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "web_extractor",
    "description": "抓取网页内容；如果提供了目标，还会进一步总结网页中与目标相关的内容。",
    "parameters": {
      "type": "object",
      "properties": {
        "urls": {
          "type": "array",
          "items": {
            "type": "string",
            "description": "单个 URL。"
          },
          "minItems": 1,
          "description": "网页 URL 列表。"
        },
        "goal": {
          "type": "string",
          "description": "访问网页的目标。如果为空，则返回网页原始内容。"
        }
      },
      "required": ["urls", "goal"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "web_search_image",
    "description": "从互联网搜索图片。返回与查询相关的图片及其 URL、标题和描述。",
    "parameters": {
      "type": "object",
      "properties": {
        "queries": {
          "type": "array",
          "items": {
            "type": "string",
            "description": "单个查询。"
          },
          "description": "查询列表。"
        }
      },
      "required": ["queries"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "code_interpreter",
    "description": "Python 代码沙箱，可用于执行 Python 代码。",
    "parameters": {
      "type": "object",
      "properties": {
        "code": {
          "description": "Python 代码。",
          "type": "string"
        }
      },
      "required": ["code"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "bio",
    "description": "用于管理个性化用户记忆的运行时记忆工具。",
    "parameters": {
      "type": "object",
      "properties": {
        "operations": {
          "type": "object",
          "description": "根据用户请求，对个性化用户记忆进行更新时所需执行的操作。",
          "properties": {
            "add": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "所有需要添加到个性化用户记忆中的内容。"
            },
            "delete": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "description": "所有需要删除的个性化用户记忆索引。"
            },
            "update": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "index": {
                    "type": "number",
                    "description": "需要更新的个性化用户记忆索引。"
                  },
                  "content": {
                    "type": "string",
                    "description": "新的个性化用户记忆内容。"
                  }
                },
                "required": ["index", "content"]
              },
              "description": "所有需要更新的个性化用户记忆索引及其新内容。"
            }
          }
        }
      },
      "required": ["operations"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "image_search",
    "description": "使用对话中的图片（由 img_idx 指定）搜索相似图片。返回相似图片及其 URL、标题和描述。",
    "parameters": {
      "type": "object",
      "properties": {
        "img_idx": {
          "type": "number",
          "description": "用户查询图片的索引（从 0 开始）。"
        },
        "bbox": {
          "type": "array",
          "items": {
            "type": "number"
          },
          "description": "图片查询区域的边界框，相对坐标格式为 [0-1000]，形式为 [x1, y1, x2, y2]。",
          "minItems": 4,
          "maxItems": 4
        }
      },
      "required": ["img_idx", "bbox"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "image_gen",
    "description": "图像生成服务，接收文本描述作为输入，并返回图像 URL。",
    "parameters": {
      "type": "object",
      "properties": {
        "prompt": {
          "description": "对期望生成内容的详细描述。必须完整保留原始请求中的具体要求，例如文本内容，严禁省略。",
          "type": "string"
        }
      },
      "required": ["prompt"]
    }
  }
}
```

```json
{
  "type": "function",
  "function": {
    "name": "image_edit",
    "description": "图像编辑服务，可接收对话中的若干图片索引（不超过三个）以及文本指令，对图像进行修改，并返回编辑结果 URL。能力包括：按详细指令修改图像、提升质量、调整光照、增强细节、局部放大、风格变更、添加或移除对象。",
    "parameters": {
      "type": "object",
      "properties": {
        "img_idx_list": {
          "type": "array",
          "items": {
            "type": "number",
            "description": "图片索引（从 0 开始）。"
          },
          "minItems": 1,
          "maxItems": 3,
          "description": "图片列表（不超过三个）。"
        },
        "prompt": {
          "type": "string",
          "description": "编辑图像的详细指令，例如：提升质量、调整光照、增强细节、局部放大、添加/移除/修改对象、风格变化或特定区域修改。必须完整保留原始请求中的具体要求，例如文本内容，严禁省略。"
        }
      },
      "required": ["img_idx_list", "prompt"]
    }
  }
}
```