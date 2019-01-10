# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/10 9:15

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