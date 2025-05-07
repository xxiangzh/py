import os
import sys

def rename_files(target_dir, old_str, new_str):
    """
    在指定目录下执行批量文件重命名
    :param target_dir: 要处理的目录路径
    :param old_str: 要被替换的字符串
    :param new_str: 替换的新字符串
    """
    if not os.path.isdir(target_dir):
        print(f"错误：目录不存在 '{target_dir}'")
        return

    renamed_count = 0
    with os.scandir(target_dir) as entries:
        for entry in entries:
            if entry.is_file():
                original_name = entry.name
                new_name = original_name.replace(old_str, new_str)

                if new_name != original_name:
                    try:
                        os.rename(
                            entry.path,
                            os.path.join(target_dir, new_name)
                        )
                        print(f"成功：'{original_name}' → '{new_name}'")
                        renamed_count += 1
                    except FileExistsError:
                        print(f"跳过：'{new_name}' 已存在，未执行覆盖")
                    except Exception as e:
                        print(f"错误：重命名 '{original_name}' 失败 - {str(e)}")

    print(f"\n操作完成：共处理 {renamed_count} 个文件")

# 处理当前目录
# python file_rename_rep.py . "old" "new"
# 处理指定目录
# python file_rename_rep.py D:\bak "2023" "2024"
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("使用方法：python file_rename_rep.py <目标目录> <旧字符串> <新字符串>")
        print("示例：python file_rename_rep.py ./docs 'v1' 'v2'")
        sys.exit(1)

    directory = sys.argv[1]
    old_part = sys.argv[2]
    new_part = sys.argv[3]

    rename_files(
        target_dir=os.path.abspath(directory),
        old_str=old_part,
        new_str=new_part
    )
