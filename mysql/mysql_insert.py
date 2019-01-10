# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/10 9:06

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="680034", db="test", port=3306)
cur = conn.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cur.execute(sql)
    conn.commit()  # 提交到数据库执行
except:
    conn.rollback()  # 如果发生错误回滚

conn.close()