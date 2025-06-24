import os

"""
将路径下的所有文件名称中的指定字段替换为新字段（不处理子文件夹）
"""
# 在这里修改参数↓↓↓↓↓↓↓↓↓↓
target_dir = r"D:\test"  # 需要处理的文件夹路径
old_str = "test_"  # 要替换的旧字段
new_str = ""  # 替换为的新字段

# 验证文件夹是否存在
if not os.path.isdir(target_dir):
    print(f"错误：路径 '{target_dir}' 不存在或不是文件夹。")
    exit()

# 遍历目标文件夹
for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

    if os.path.isfile(file_path):
        # 替换文件名中的指定字段
        if old_str in filename:
            new_filename = filename.replace(old_str, new_str)
        else:
            print(f"⚠️ 跳过 {filename}，未找到要替换的字段 '{old_str}'")
            continue

        new_file_path = os.path.join(target_dir, new_filename)

        if os.path.exists(new_file_path):
            print(f"⚠️ 跳过 {filename}，目标文件 {new_filename} 已存在")
            continue

        try:
            os.rename(file_path, new_file_path)
            # print(f"✅ 成功：{filename} -> {new_filename}")
        except Exception as e:
            print(f"❌ 失败：{filename} 错误信息：{str(e)}")

print(f"✅ 完成")
