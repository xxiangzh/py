#!/usr/bin/python3

class Hlclass:
    # 定义基本属性
    name = ''
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __age = 0

    # 定义构造方法
    def __init__(self, n, a):
        self.name = n
        self.__age = a

    # 定义业务方法
    def hlh(self):
        print('hello world %s %d岁' % (self.name, self.__age))