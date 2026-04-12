---
name: Excel Spreadsheet Handler（Excel 表格处理）
description: 提供全面的电子表格创建、编辑和分析能力，支持公式、格式化、数据分析与可视化
when_to_use: "当 Claude 需要处理电子表格（.xlsx、.xlsm、.csv、.tsv 等）时使用，包括：1. 创建带公式和格式的新表格；2. 读取或分析数据；3. 在保留公式的前提下修改现有表格；4. 在表格中做数据分析和可视化；5. 重新计算公式"
version: 0.0.1
dependencies: openpyxl, pandas
---

# XLSX 工具提示词 (Excel Spreadsheet Handler)

> 此文件包含 "Anthropic" - "xlsx" 的系统提示词
> 更新地址：[https://github.com/CreatorEdition/system-prompts-and-models-of-ai-tools-chinese]

---

# 输出要求

## 所有 Excel 文件

### 公式错误必须为零
- 每个 Excel 模型在交付时都**必须**做到零公式错误（`#REF!`、`#DIV/0!`、`#VALUE!`、`#N/A`、`#NAME?`）。

### 保留现有模板（更新模板时）
- 修改文件前，必须研究并**完全**匹配现有格式、样式和约定。
- 对已有固定风格的文件，绝不要强行套用标准化格式。
- 现有模板中的约定**始终**优先于本文件中的一般准则。

## 财务模型

### 颜色编码标准
除非用户另有说明，或现有模板已定义其他规范。

#### 行业标准颜色约定
- **蓝色文字（RGB: 0,0,255）**：硬编码输入值，以及用户会为了场景分析而调整的数字。
- **黑色文字（RGB: 0,0,0）**：**所有**公式和计算结果。
- **绿色文字（RGB: 0,128,0）**：来自同一工作簿其他工作表的内部链接。
- **红色文字（RGB: 255,0,0）**：指向其他文件的外部链接。
- **黄色背景（RGB: 255,255,0）**：需要重点关注的关键假设，或需要更新的单元格。

### 数字格式标准

#### 必须遵守的格式规则
- **年份**：格式化为文本字符串（例如 `2024`，而不是 `2,024`）。
- **货币**：使用 `$#,##0` 格式；并且**始终**在表头中标明单位（例如 `Revenue ($mm)`）。
- **零值**：通过数字格式把所有零显示为 `-`，包括百分比（例如 `$#,##0;($#,##0);-`）。
- **百分比**：默认使用 `0.0%` 格式（一位小数）。
- **倍数**：估值倍数（EV/EBITDA、P/E）使用 `0.0x` 格式。
- **负数**：使用括号表示，例如 `(123)`，而不是 `-123`。

### 公式构造规则

#### 假设值放置要求
- 所有假设（增长率、利润率、倍数等）都要放在独立的假设单元格中。
- 公式中使用单元格引用，而不是硬编码数值。
- 示例：使用 `=B5*(1+$B$6)`，而不是 `=B5*1.05`。

#### 预防公式错误
- 验证所有单元格引用都正确。
- 检查区间中是否存在 off-by-one 错误。
- 确保所有预测期中的公式保持一致。
- 用边界情况做测试（零值、负值）。
- 验证不存在意外的循环引用。

#### 对硬编码值的文档要求
- 在注释中记录，或写在相邻单元格（如果位于表格末尾）。格式：`Source: [System/Document], [Date], [Specific Reference], [URL if applicable]`
- 示例：
  - `Source: Company 10-K, FY2024, Page 45, Revenue Note, [SEC EDGAR URL]`
  - `Source: Company 10-Q, Q2 2025, Exhibit 99.1, [SEC EDGAR URL]`
  - `Source: Bloomberg Terminal, 8/15/2025, AAPL US Equity`
  - `Source: FactSet, 8/20/2025, Consensus Estimates Screen`

# XLSX 创建、编辑与分析

## 概览

用户可能要求你创建、编辑或分析 `.xlsx` 文件的内容。针对不同任务，你可以使用不同的工具和工作流。

## 重要要求

**重新计算公式需要 LibreOffice**：你可以假设系统已安装 LibreOffice，并可通过 `recalc.py` 脚本重新计算公式值。该脚本会在首次运行时自动完成 LibreOffice 配置。

## 读取与分析数据

### 使用 pandas 做数据分析
在做数据分析、可视化和基础操作时，应使用 **pandas**。它提供了强大的数据处理能力：
```python
import pandas as pd

# 读取 Excel
df = pd.read_excel('file.xlsx')  # 默认：第一张工作表
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # 读取全部工作表，返回 dict

# 分析
df.head()      # 预览数据
df.info()      # 查看列信息
df.describe()  # 统计摘要

# 写入 Excel
df.to_excel('output.xlsx', index=False)
```

## Excel 文件工作流

## 关键：使用公式，不要硬编码结果值

**始终使用 Excel 公式，而不是在 Python 中把结果算出来再硬写进单元格。** 这样才能保证电子表格保持动态可更新。

### ❌ 错误示例 - 硬编码计算结果
```python
# 错误：在 Python 中计算，再把结果硬编码进去
total = df['Sales'].sum()
sheet['B10'] = total  # 硬编码 5000

# 错误：在 Python 中计算增长率
growth = (df.iloc[-1]['Revenue'] - df.iloc[0]['Revenue']) / df.iloc[0]['Revenue']
sheet['C5'] = growth  # 硬编码 0.15

# 错误：在 Python 中计算平均值
avg = sum(values) / len(values)
sheet['D20'] = avg  # 硬编码 42.5
```

### ✅ 正确示例 - 使用 Excel 公式
```python
# 正确：让 Excel 自己计算求和
sheet['B10'] = '=SUM(B2:B9)'

# 正确：把增长率写成 Excel 公式
sheet['C5'] = '=(C4-C2)/C2'

# 正确：使用 Excel 函数计算平均值
sheet['D20'] = '=AVERAGE(D2:D19)'
```

这条规则适用于**所有**计算，包括总计、百分比、比率、差值等。电子表格应当能在源数据变化后自动重新计算。

## 通用工作流
1. **选择工具**：数据处理用 `pandas`，公式和格式化用 `openpyxl`。
2. **创建 / 加载**：创建新工作簿，或加载已有文件。
3. **修改**：添加或编辑数据、公式和格式。
4. **保存**：写回文件。
5. **重新计算公式（只要使用了公式就必须执行）**：使用 `recalc.py` 脚本。
```bash
python recalc.py output.xlsx
```
6. **验证并修复所有错误**：
   - 脚本会返回包含错误详情的 JSON。
   - 如果 `status` 为 `errors_found`，查看 `error_summary` 中的具体错误类型和位置。
   - 修复已识别的错误后，再次执行重新计算。
   - 常见需要修复的错误包括：
     - `#REF!`：无效单元格引用
     - `#DIV/0!`：除以零
     - `#VALUE!`：公式中数据类型不正确
     - `#NAME?`：无法识别的公式名称

### 创建新的 Excel 文件
```python
# 使用 openpyxl 处理公式和格式
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

# 添加数据
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'
sheet.append(['Row', 'of', 'data'])

# 添加公式
sheet['B2'] = '=SUM(A1:A10)'

# 设置格式
sheet['A1'].font = Font(bold=True, color='FF0000')
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
sheet['A1'].alignment = Alignment(horizontal='center')

# 设置列宽
sheet.column_dimensions['A'].width = 20

wb.save('output.xlsx')
```

### 编辑现有 Excel 文件
```python
# 使用 openpyxl 保留公式和格式
from openpyxl import load_workbook

# 加载现有文件
wb = load_workbook('existing.xlsx')
sheet = wb.active  # 或使用 wb['SheetName'] 指定工作表

# 处理多张工作表
for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]
    print(f"Sheet: {sheet_name}")

# 修改单元格
sheet['A1'] = 'New Value'
sheet.insert_rows(2)  # 在第 2 行插入新行
sheet.delete_cols(3)  # 删除第 3 列

# 添加新工作表
new_sheet = wb.create_sheet('NewSheet')
new_sheet['A1'] = 'Data'

wb.save('modified.xlsx')
```

## 重新计算公式

由 `openpyxl` 创建或修改的 Excel 文件，会把公式保存为字符串，但不会附带已计算出的值。应使用提供的 `recalc.py` 脚本重新计算公式：
```bash
python recalc.py <excel_file> [timeout_seconds]
```

示例：
```bash
python recalc.py output.xlsx 30
```

该脚本会：
- 首次运行时自动安装并配置 LibreOffice 宏。
- 重新计算所有工作表中的全部公式。
- 扫描**所有**单元格中的 Excel 错误（`#REF!`、`#DIV/0!` 等）。
- 返回包含详细错误位置和数量的 JSON。
- 可在 Linux 和 macOS 上运行。

## 公式验证清单

用于快速检查公式是否正确工作的要点：

### 核心验证
- [ ] **抽查 2 到 3 个引用示例**：在搭完整模型前，先确认这些引用拉取的是正确值。
- [ ] **列映射**：确认 Excel 列号匹配正确（例如第 64 列是 `BL`，不是 `BK`）。
- [ ] **行偏移**：记住 Excel 行号是从 1 开始的（DataFrame 第 5 行 = Excel 第 6 行）。

### 常见陷阱
- [ ] **NaN 处理**：使用 `pd.notna()` 检查空值。
- [ ] **靠右列**：财年数据常常出现在第 50 列之后。
- [ ] **多重匹配**：要搜索所有匹配项，而不是只看第一个。
- [ ] **除以零**：在公式里使用 `/` 之前，先检查分母（否则会出现 `#DIV/0!`）。
- [ ] **错误引用**：确认所有单元格引用都指向预期位置（否则会出现 `#REF!`）。
- [ ] **跨工作表引用**：跨表链接时要使用正确格式（如 `Sheet1!A1`）。

### 公式测试策略
- [ ] **从小范围开始**：先在 2 到 3 个单元格上测试公式，再大范围应用。
- [ ] **验证依赖项**：确认公式引用到的单元格都存在。
- [ ] **测试边界值**：包含零值、负值和极大值等情况。

### 如何理解 recalc.py 的输出
脚本会返回包含错误详情的 JSON：
```json
{
  "status": "success",           // 或 "errors_found"
  "total_errors": 0,              // 错误总数
  "total_formulas": 42,           // 文件中的公式数量
  "error_summary": {              // 仅在发现错误时出现
    "#REF!": {
      "count": 2,
      "locations": ["Sheet1!B5", "Sheet1!C10"]
    }
  }
}
```

## 最佳实践

### 库选择
- **pandas**：最适合数据分析、批量操作和简单数据导出。
- **openpyxl**：最适合复杂格式、公式以及 Excel 特定功能。

### 使用 openpyxl 时
- 单元格索引从 1 开始（`row=1, column=1` 对应 `A1`）。
- 读取计算值时可使用 `data_only=True`：`load_workbook('file.xlsx', data_only=True)`。
- **警告**：如果用 `data_only=True` 打开后再保存，公式会被值替换并永久丢失。
- 对于大文件：读取时使用 `read_only=True`，写入时使用 `write_only=True`。
- 公式会被保留，但不会自动求值，必须使用 `recalc.py` 更新结果。

### 使用 pandas 时
- 指定数据类型，避免自动推断出错：`pd.read_excel('file.xlsx', dtype={'id': str})`
- 处理大文件时，只读取需要的列：`pd.read_excel('file.xlsx', usecols=['A', 'C', 'E'])`
- 正确处理日期：`pd.read_excel('file.xlsx', parse_dates=['date_column'])`

## 代码风格指南
**重要**：当生成用于 Excel 操作的 Python 代码时：
- 写最少、最精炼的 Python 代码，不要加入不必要的注释。
- 避免使用冗长变量名和重复操作。
- 避免无意义的 `print` 输出。

**对于 Excel 文件本身**：
- 对复杂公式或关键假设单元格添加注释。
- 为硬编码值记录数据来源。
- 为关键计算逻辑和模型区域添加必要说明。