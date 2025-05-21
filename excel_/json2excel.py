import json
import os

import pandas as pd

# JSON字符串示例
json_str = '''
[
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30, "city": "上海"},
    {"name": "王五", "age": 28, "city": "广州"}
]
'''

# 解析JSON字符串
try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f"JSON解析失败：{e}")
    exit()

# 转换为DataFrame
df = pd.DataFrame(data)

# 输出路径
output_dir = r"D:\demo"
output_path = os.path.join(output_dir, "output.xlsx")

# 创建目录（如果不存在）
try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as e:
    print(f"创建目录失败：{e}")
    exit()

# 导出到Excel
try:
    df.to_excel(output_path, index=False)
    print(f"文件已成功导出到：{output_path}")
except Exception as e:
    print(f"导出Excel失败：{e}")
