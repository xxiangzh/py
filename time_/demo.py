from datetime import datetime

# 获取当前时间并格式化为 yyyy-MM-dd HH:mm:ss
# 方法1
now_datetime1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now_datetime1)  # 输出示例：2023-10-05 15:30:45

# 方法2
now_datetime2 = datetime.now().isoformat(sep=" ", timespec="seconds")  # 替换 T 为空格
print(now_datetime2)  # 输出示例：2023-10-05 15:30:45
