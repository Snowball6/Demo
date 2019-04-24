# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/10 9:15

# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
#
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
import pymysql
conn = pymysql.connect(host="192.168.35.9", user="root", password="root123!@#", db="test_utl", port=3306)
cur = conn.cursor()
sql = "select * from alone_app "

cur.execute(sql)
data = cur.fetchall()
print(data)
conn.close()