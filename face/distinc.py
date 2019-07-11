#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2019/7/11 10:21
# @Author : Snowball

# 去重，保持原来的顺序
# data = [11, 2, 33, 7, 11, 8, 19, 1, 2]
# # data_dis = []
# # for item in data:
# #     if item not in data_dis:
# #         data_dis.append(item)
# # print(data_dis)
# data_dis = list(set(data))
# data_dis.sort(key=data.index)
# print(data_dis)

# 按照age从小到大排序
data = [
    {'name': 'chen1', 'age': 19},
    {'name': 'chen2', 'age': 23},
    {'name': 'chen3', 'age': 10},
    {'name': 'chen4', 'age': 29},
]
# 第一种方法：
data_dis = sorted(data, key=lambda k: k['age'])
print(data_dis)

# 第二种方法：
data.sort(key=lambda k: k['age'])
print(data)