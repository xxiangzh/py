#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from openpyxl import Workbook


def getResult(sql):
    # 建立数据库连接
    dbc = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="xzh"
    )
    cursor = dbc.cursor()
    cursor.execute(sql)

    # 获取标题
    description = cursor.description
    title = []
    for x in description:
        title.append(x[0])
    title = tuple(title)
    # 获取结果集
    result = cursor.fetchall()
    # 将标题插入到第一列
    result.insert(0, tuple(title))

    # 关闭游标和连接
    cursor.close()
    dbc.close()
    return result


def write(result, path):
    # 创建excel文件对象
    wb = Workbook()
    # 获取第一个sheet
    sheet = wb.active
    for row in result:
        sheet.append(row)
    wb.save(path)


# 程序主入口
if __name__ == "__main__":
    sql = "SELECT * FROM t_user"
    path = "D:demo.xlsx"

    result = getResult(sql)
    write(result, path)
