#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

# 程序主入口
if __name__ == "__main__":

    # 建立数据库连接
    dbc = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="xzh"
    )
    print(dbc)

    cursor = dbc.cursor()

    sql = "SELECT * FROM t_user WHERE id = 1"

    cursor.execute(sql)

    result = cursor.fetchall()

    for x in result:
        print(x)

    # 关闭游标和连接
    cursor.close()
    dbc.close()
