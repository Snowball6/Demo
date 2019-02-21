# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/10 9:15

# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
#
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="680034", db="test", port=3306)
cur = conn.cursor()
sql = "select * from employee"
try:
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        print(row)
        first_name = row[0]
        last_name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print(first_name, last_name, age, sex, income)
except:
    print("Error")
conn.close()