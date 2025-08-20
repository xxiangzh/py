import os
import shutil
from typing import Set


def generate_unique_filename(dst_folder: str, filename: str) -> str:
    """
    生成带序号的不重复文件名
    示例：file.txt → file_1.txt (如果已存在)
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(dst_folder, new_name)):
        new_name = f"{base}_{counter}{ext}"
        counter += 1

    return new_name


def flat_copy_with_filter(
        src_root: str,
        dst_folder: str,
        exclude_exts: Set[str],
        overwrite: bool = False,
        verbose: bool = True
) -> dict:
    """
    扁平化复制文件到单个文件夹

    :param src_root: 源文件夹路径
    :param dst_folder: 目标文件夹路径
    :param exclude_exts: 排除的扩展名集合（小写，如 {'.tmp', '.bak'}）
    :param overwrite: 是否覆盖已存在文件
    :param verbose: 是否显示详细信息
    :return: 包含统计信息的字典
    """
    stats = {
        'total': 0,
        'copied': 0,
        'skipped': 0,
        'failed': 0,
        'duplicates': 0
    }

    try:
        os.makedirs(dst_folder, exist_ok=True)
        if verbose:
            print(f"目标目录已就绪: {dst_folder}")
    except Exception as e:
        print(f"创建目标目录失败: {str(e)}")
        stats['failed'] += 1
        return stats

    for root, _, files in os.walk(src_root):
        for file in files:
            src_file = os.path.join(root, file)
            stats['total'] += 1

            # 检查扩展名过滤
            _, ext = os.path.splitext(file)
            if ext.lower() in exclude_exts:
                stats['skipped'] += 1
                if verbose:
                    print(f"跳过排除文件: {file}")
                continue

            # 处理目标文件名
            dst_file = os.path.join(dst_folder, file)

            # 处理文件重名
            if os.path.exists(dst_file):
                if overwrite:
                    try:
                        os.remove(dst_file)
                    except Exception as e:
                        print(f"无法覆盖文件 {file}: {str(e)}")
                        stats['failed'] += 1
                        continue
                else:
                    new_name = generate_unique_filename(dst_folder, file)
                    dst_file = os.path.join(dst_folder, new_name)
                    stats['duplicates'] += 1
                    if verbose:
                        print(f"检测到重名: {file} → {new_name}")

            # 执行复制
            try:
                shutil.copy2(src_file, dst_file)
                stats['copied'] += 1
                if verbose:
                    print(f"复制成功: {file}")
            except PermissionError:
                print(f"权限不足: {file}")
                stats['failed'] += 1
            except Exception as e:
                print(f"复制失败 {file}: {str(e)}")
                stats['failed'] += 1

    return stats


if __name__ == "__main__":
    # 配置参数
    SOURCE_FOLDER = r"D:\Zzz\a"  # 源路径
    TARGET_FOLDER = r"D:\Zzz\b"  # 目标路径
    EXCLUDE_EXTENSIONS = {'.jpg', '.zip', '.torrent', '.js'}  # 排除的扩展名

    # 执行复制
    result = flat_copy_with_filter(
        src_root=SOURCE_FOLDER,
        dst_folder=TARGET_FOLDER,
        exclude_exts=EXCLUDE_EXTENSIONS,
        overwrite=False,
        verbose=True
    )

    # 输出统计
    print("\n=== 操作统计 ===")
    print(f"扫描文件总数: {result['total']}")
    print(f"成功复制: {result['copied']}")
    print(f"跳过排除文件: {result['skipped']}")
    print(f"重名处理: {result['duplicates']}")
    print(f"失败操作: {result['failed']}")
