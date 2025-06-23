import os
import random
import string

"""
给路径下的所有文件添加前缀（使用文件所在文件夹名作为前缀，包括子文件夹）
"""
# 在这里修改参数↓↓↓↓↓↓↓↓↓↓
target_dir = r"D:\test"  # 需要处理的文件夹路径

# 验证文件夹是否存在
if not os.path.isdir(target_dir):
    print(f"错误：路径 '{target_dir}' 不存在或不是文件夹。")
    exit()

# 递归遍历目标文件夹及其子文件夹
for foldername, subfolders, filenames in os.walk(target_dir):
    # 获取当前文件夹名称
    folder_name = os.path.basename(foldername)
    # 生成两位随机字母（可能重复，包含大小写）
    random_letters = ''.join(random.choices(string.ascii_letters, k=2))
    prefix = f"{folder_name}_" + random_letters

    # 处理当前文件夹中的所有文件
    for filename in filenames:
        old_path = os.path.join(foldername, filename)
        new_filename = prefix + filename
        new_path = os.path.join(foldername, new_filename)

        # 跳过已存在同名文件的情况
        if os.path.exists(new_path):
            print(f"⚠️ 跳过 {old_path}，目标文件已存在")
            continue

        try:
            os.rename(old_path, new_path)
            print(f"✅ 成功：{os.path.relpath(old_path, target_dir)} -> {new_filename}")
        except Exception as e:
            print(f"❌ 失败：{os.path.relpath(old_path, target_dir)} 错误信息：{str(e)}")
