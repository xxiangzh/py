import os
from datetime import datetime

"""
给路径下的所有文件重命名为文件创建时间（格式：年_月_日_时_分_秒）
如果出现冲突则添加序号（1,2,3...）
"""
# 在这里修改参数↓↓↓↓↓↓↓↓↓↓
target_dir = r"D:\test"  # 需要处理的文件夹路径

# 验证文件夹是否存在
if not os.path.isdir(target_dir):
    print(f"错误：路径 '{target_dir}' 不存在或不是文件夹。")
    exit()

# 用于跟踪时间戳出现次数的字典
timestamp_counter = {}

# 遍历目标文件夹
for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

    if os.path.isfile(file_path):
        # 获取文件创建时间并格式化
        ctime = os.path.getctime(file_path)
        formatted_time = datetime.fromtimestamp(ctime).strftime("%Y_%m_%d_%H_%M_%S")

        # 分离文件名和扩展名
        base_name, extension = os.path.splitext(filename)

        # 初始化新文件名（无序号版本）
        new_filename = f"{formatted_time}{extension}"
        new_file_path = os.path.join(target_dir, new_filename)

        # 处理文件名冲突
        if new_filename in timestamp_counter:
            timestamp_counter[new_filename] += 1
            counter = timestamp_counter[new_filename]
            new_filename = f"{formatted_time}_{counter}{extension}"
            new_file_path = os.path.join(target_dir, new_filename)
        else:
            timestamp_counter[new_filename] = 0  # 初始化计数器

        # 检查文件是否存在（处理跨文件冲突）
        attempt_count = 1
        while os.path.exists(new_file_path):
            attempt_count += 1
            new_filename = f"{formatted_time}_{attempt_count}{extension}"
            new_file_path = os.path.join(target_dir, new_filename)
            timestamp_counter[new_filename] = attempt_count

        # 重命名文件
        try:
            os.rename(file_path, new_file_path)
            # print(f"✅ 成功: {filename} -> {new_filename}")
        except Exception as e:
            print(f"❌ 失败: {filename} 错误信息: {str(e)}")

print(f"✅ 完成")
