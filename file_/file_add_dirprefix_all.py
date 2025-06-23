import os

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

    # 按文件名排序，确保序号顺序一致
    filenames_sorted = sorted(filenames)

    # 为当前文件夹中的文件添加序号
    for index, filename in enumerate(filenames_sorted, start=1):
        old_path = os.path.join(foldername, filename)
        # 提取文件扩展名
        file_base, file_ext = os.path.splitext(filename)

        # 构建新文件名：文件夹名_序号_原文件名
        new_filename = f"{folder_name}_{index}_{file_base}{file_ext}"
        new_path = os.path.join(foldername, new_filename)

        # 跳过已存在同名文件的情况
        if os.path.exists(new_path):
            print(f"⚠️ 跳过 {old_path}，目标文件已存在")
            continue

        try:
            os.rename(old_path, new_path)
            rel_path = os.path.relpath(old_path, target_dir)
            print(f"✅ 成功：{rel_path} -> {new_filename}")
        except Exception as e:
            rel_path = os.path.relpath(old_path, target_dir)
            print(f"❌ 失败：{rel_path} 错误信息：{str(e)}")