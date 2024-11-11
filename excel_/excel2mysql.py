#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from openpyxl import load_workbook


def save_result(sql, val):
    # 建立数据库连接
    dbc = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="xzh"
    )
    cursor = dbc.cursor()
    # 批量插入
    cursor.executemany(sql, val)
    # 提交事务
    dbc.commit()
    print('记录插入成功', cursor.rowcount, '条')

    # 关闭游标和连接
    cursor.close()
    dbc.close()


def read(path):
    # 读取excel文件数据
    wb = load_workbook(path, data_only=True)
    # 获取第一个sheet
    sheet = wb.active

    # 将每行数据放到列表
    row_list = []
    for row in sheet.rows:
        row_data = []
        for cell in row:
            row_data.append(cell.value)
        row_list.append(row_data)
    del row_list[0]
    return row_list


# 程序主入口
if __name__ == "__main__":
    sql = "INSERT INTO `t_user` (`id`, `name`) VALUES (%s, %s)"
    # val = [('3', '小明'), ('4', '小红')]
    path = "D:demo.xlsx"

    row_list = read(path)
    save_result(sql, row_list)
    print("完成")
