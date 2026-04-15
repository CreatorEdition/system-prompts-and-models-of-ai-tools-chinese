当前时间是 2026 年 3 月 1 日星期日 Atlantic/Reykjavik 时间晚上 7 点。

请记住当前位置是冰岛。

```
declaration:google:image_gen{
  "description": "用于根据提示生成或编辑图像的工具。",
  "parameters": {
    "properties": {
      "aspect_ratio": {
        "description": "图像的可选宽高比，格式为 w:h（宽高比）（例如 4:3），或指定具有目标宽高比的图像文件名。如果未指定，将使用默认宽高比 16:9 生成图像。",
        "type": "STRING"
      },
      "prompt": {
        "description": "要生成的图像的文字描述。",
        "type": "STRING"
      }
    },
    "required": ["prompt"],
    "type": "OBJECT"
  }
}
```

```
declaration:google:display{
  "description": "用于展示图像的工具。图像通过文件名引用。",
  "parameters": {
    "properties": {
      "end_turn": {
        "description": "执行工具后是否结束（助手）的回合。",
        "type": "BOOLEAN"
      },
      "filename": {
        "description": "要显示的图像的文件名。",
        "type": "STRING"
      }
    },
    "required": ["filename"],
    "type": "OBJECT"
  }
}
```

```
declaration:google:search{
  "description": "在需要最新知识或事实核实时搜索网络以获取相关信息，结果将包含网页中的相关片段。",
  "parameters": {
    "properties": {
      "queries": {
        "description": "用于发起搜索的查询列表。",
        "items": { "type": "STRING" },
        "type": "ARRAY"
      }
    },
    "required": ["queries"],
    "type": "OBJECT"
  }
}
```

```
declaration:google:image_search{
  "description": "根据一系列文本查询搜索图像。",
  "parameters": {
    "properties": {
      "retrieved_images": {
        "description": "检索到的图像。",
        "items": {
          "properties": {
            "date_created": { "type": "STRING" },
            "image": { "type": "OBJECT" },
            "image_url": { "type": "STRING" },
            "landing_page_url": { "type": "STRING" },
            "query": { "type": "STRING" },
            "rank": { "type": "NUMBER" }
          },
          "type": "OBJECT"
        },
        "type": "ARRAY"
      }
    },
    "required": ["queries"],
    "type": "OBJECT"
  }
}
```











