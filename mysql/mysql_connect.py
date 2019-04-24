# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/10 8:36
# PyMySQL 下载地址：https://github.com/PyMySQL/PyMySQL && cd PyMySQL/ && python3 setup.py install 或直接使用pip下载
import pymysql
# 连接数据库，db为想要连接的库名
conn = pymysql.connect(host="localhost", user="root", password="root123!@#", db="manage_system", port=3306,)

# 创建一个游标对象
cur = conn.cursor()
sql = "select * from user_info"

# 使用execute方法来执行sql语句
cur.execute(sql)

# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。返回的数据类型为tuple
data = cur.fetchall()
print(data)
# 关闭连接
conn.close()


