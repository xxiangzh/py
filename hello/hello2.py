#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hello.animal import Dog

# 程序主入口
if __name__ == "__main__":
    dog1 = Dog("二哈", "白色", 100)
    dog2 = Dog("小狗", "黑色")
    dog1.bark()
    dog2.bark()

    print('---')
    dog3 = Dog("又一只", "彩色")
    Dog.name = "改名"
    Dog.high = "30cm"
    dog3.bark()

    # name没变，high变了，说明未赋值的才会全局共享，已赋值不变
    dog1.bark()
    dog2.bark()
