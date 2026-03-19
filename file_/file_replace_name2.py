import os

"""
将路径下的所有文件名称中的指定字段替换为新字段（处理所有子文件夹）
"""
# 在这里修改参数↓↓↓↓↓↓↓↓↓↓
target_dir = r"D:\test"  # 需要处理的文件夹路径
old_str = "test_"  # 要替换的旧字段
new_str = ""  # 替换为的新字段

# 验证文件夹是否存在
if not os.path.isdir(target_dir):
    print(f"错误：路径 '{target_dir}' 不存在或不是文件夹。")
    exit()

# 递归遍历所有文件夹和子文件夹
for root, dirs, files in os.walk(target_dir):
    # 遍历当前文件夹下的所有文件
    for filename in files:
        file_path = os.path.join(root, filename)

        # 替换文件名中的指定字段
        if old_str in filename:
            new_filename = filename.replace(old_str, new_str)
        else:
            continue

        new_file_path = os.path.join(root, new_filename)

        if os.path.exists(new_file_path):
            print(f"⚠️ 跳过 {file_path}，目标文件已存在")
            continue

        try:
            os.rename(file_path, new_file_path)
            # print(f"✅ 成功：{filename} -> {new_filename}")
        except Exception as e:
            print(f"❌ 失败：{file_path} 错误信息：{str(e)}")

print(f"✅ 完成")