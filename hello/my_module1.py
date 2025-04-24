#!/usr/bin/python3

# 如果模块是被直接运行，__name__ 的值为 __main__。
if __name__ == '__main__':
    # 命令 python using_name.py，直接运行此文件时，执行
    print('程序自身在运行')
else:
    # 命令 import my_module1，被引入时，执行
    print('我来自另一模块')
