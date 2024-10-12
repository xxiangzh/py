#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hellocp


def hl(x):
    print("hello world", x)


# 程序主入口
if __name__ == "__main__":
    print("hello world")

    hl('张三')

    c = hellocp.Hlclass('李四', 3)
    c.hlh()