# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/14 9:43


# def measure():
#     temp = 30
#     wetness = 50
#     return temp, wetness
#
#
# result = measure()
# # 需要单独处理返回值的其中某个值，使用索引的方式 是不方便的。
# print(result[0])
# print(result[1])
# # 使用简单的方法，单独处理元组中的元素，可以使用多个变量一次接受函数的返回结果
# gl_temp, gl_wetness = measure()
# print(gl_temp)
# print(gl_wetness)


# 交换两个变量的值
# a = 100
# b = 6
# a, b = b, a
# print(a, b)

# def sum_numbers(*args):
#     result = 0
#     for n in args:
#         result += n
#     return result
#
#
# num_result = sum_numbers(1, 2, 4)
# print(num_result)

#
# def sum_numbers(num):
#     # 出口
#     if num == 1:
#         return 1
#     temp = sum_numbers(num - 1)
#     return num + temp
#
#
# result = sum_numbers(2)
# print(result)


class Cat(object):
    def eat(self):
        print("111")













