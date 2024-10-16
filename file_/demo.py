#!/usr/bin/env python
# -*- coding: utf-8 -*-

def write():
    # 打开文件，如果不存在则创建，如果已存在则覆盖，w表示写入模式，encoding为utf-8
    file = open('D:demo.txt', 'w', encoding="utf-8")
    # 将字符串写入文件
    file.write("123abc啊哈")
    # 关闭文件流
    file.close()


def read():
    # 打开文件，如果不存在则创建，如果已存在则覆盖，r表示只读模式，encoding为utf-8
    file = open('D:demo.txt', 'r', encoding="utf-8")
    # 读取文件内容
    txt = file.read()
    print(txt)
    # 关闭文件流
    file.close()


# 程序主入口
if __name__ == "__main__":
    write()
    read()
