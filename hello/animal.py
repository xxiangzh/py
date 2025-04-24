#!/usr/bin/python3

class Dog:

    # 类变量。全体实例共享
    name = "默认"
    high = "10cm"
    # 私有属性。私有属性在类外部无法直接进行访问
    __age = 0

    # 构造函数，初始化实例属性
    def __init__(self, name, color, age = 1):
        # 实例属性。每个实例独有。修改一个实例的变量不会影响其他实例
        self.name = name
        self.color = color
        self.__age = age

    # 普通函数
    def bark(self):
        print(f"{self.name} {self.color} {self.high} {self.__age} 在汪汪叫！")

