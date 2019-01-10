# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/10 9:01

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="680034", db="test", port=3306)
cur = conn.cursor()
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cur.execute(sql)
conn.close()

