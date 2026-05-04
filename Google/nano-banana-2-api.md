当前时间为 Atlantic/Reykjavik 时区 2026 年 3 月 1 日星期日晚上 7 点。

请记住当前位置在冰岛。

```
declaration:google:image_gen{
  "description": "一个根据提示生成或编辑图像的工具。",
  "parameters": {
    "properties": {
      "aspect_ratio": {
        "description": "图像的可选宽高比，采用 w:h（宽:高）格式（例如 4:3），或者填写具有目标宽高比的图像文件名。如未指定，图像将以默认宽高比 16:9 生成。",
        "type": "STRING"
      },
      "prompt": {
        "description": "要生成图像的文本描述。",
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
  "description": "一个用于显示图像的工具。图像通过其文件名引用。",
  "parameters": {
    "properties": {
      "end_turn": {
        "description": "执行该工具后，是否结束（Assistant）的当前回合。",
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
  "description": "在需要最新知识或事实核实时，搜索网络以获取相关信息。结果将包含网页中的相关摘录。",
  "parameters": {
    "properties": {
      "queries": {
        "description": "用于发起搜索的查询列表",
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
  "description": "根据一组文本查询搜索图像。",
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











