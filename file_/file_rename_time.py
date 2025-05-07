import os
from datetime import datetime


def get_creation_time(path):
    """获取文件创建时间"""
    ctime = os.path.getctime(path)
    return datetime.fromtimestamp(ctime)


def safe_rename(src, dst):
    """处理文件名冲突的重命名"""
    if not os.path.exists(dst):
        # 更安全的跨盘符重命名
        os.replace(src, dst)
        return dst

    base, ext = os.path.splitext(dst)
    counter = 1
    while True:
        new_dst = f"{base}_{counter}{ext}"
        if not os.path.exists(new_dst):
            os.replace(src, new_dst)
            return new_dst
        counter += 1


def batch_rename(folder_path, dry_run=False):
    renamed = 0
    errors = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            src = os.path.join(root, file)

            try:
                # 获取文件信息
                ctime = get_creation_time(src)
                ext = os.path.splitext(file)[1]
                new_name = ctime.strftime("%Y_%m_%d_%H_%M_%S") + ext
                dst = os.path.join(root, new_name)

                # 显示操作预览
                if dry_run:
                    print(f"[预览] {file} -> {new_name}")
                    continue

                # 执行重命名
                final_path = safe_rename(src, dst)
                print(f"已重命名: {file} -> {os.path.basename(final_path)}")
                renamed += 1

            except PermissionError:
                print(f"权限不足: {file}")
                errors += 1
            except Exception as e:
                print(f"错误 {file}: {str(e)}")
                errors += 1

    print(f"\n操作结果: 成功 {renamed} 个, 失败 {errors} 个")


if __name__ == "__main__":
    # 使用前请修改路径
    target_folder = r"D:\a"

    # 试运行（不实际修改）
    batch_rename(target_folder, dry_run=True)

    # 确认无误后注释上行，取消注释下行执行实际操作
    # batch_rename(target_folder)
