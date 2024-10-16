#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

# 程序主入口
if __name__ == "__main__":
    # 定义python对象
    pythonObj = {
        'no': 1,
        'name': '哈啊'
    }
    print("type：", type(pythonObj))
    print("pythonObj：", pythonObj)

    # python字典 转 json字符串
    jsonStr = json.dumps(pythonObj, ensure_ascii=False)
    print("type：", type(jsonStr))
    print("jsonStr：", jsonStr)

    # json字符串 转 python字典
    pythonDict = json.loads(jsonStr)
    print("type：", type(pythonDict))
    print("pythonDict：", pythonDict)
    print("pythonDict：", repr(pythonDict))
