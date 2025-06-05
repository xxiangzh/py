import os

"""
给路径下的所有文件添加前缀（不处理子文件夹）
"""
# 在这里修改参数↓↓↓↓↓↓↓↓↓↓
target_dir = r"D:\test"  # 需要处理的文件夹路径
prefix = "new_"  # 要添加的前缀

# 验证文件夹是否存在
if not os.path.isdir(target_dir):
    print(f"错误：路径 '{target_dir}' 不存在或不是文件夹。")
    exit()

# 遍历目标文件夹
for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

    if os.path.isfile(file_path):
        new_filename = prefix + filename
        new_file_path = os.path.join(target_dir, new_filename)

        if os.path.exists(new_file_path):
            print(f"⚠️ 跳过 {filename}，目标文件已存在")
            continue

        try:
            os.rename(file_path, new_file_path)
            print(f"✅ 成功：{filename} -> {new_filename}")
        except Exception as e:
            print(f"❌ 失败：{filename} 错误信息：{str(e)}")
