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

# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         print("%s 来了" % self.name)
#
#     def __del__(self):
#         print("%s 走了" % self.name)
#
#     def __str__(self):
#         return "我是小猫"
#
#
# tom = Cat("tom")
# print(tom)

# class Person:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def __str__(self):
#         return "我的名字叫%s, 我的身高是%s" % (self.name, self.height)
#
#     def run(self):
#         print("%s " % self.name)
#         self.height -= 0.5
#
#     def eat(self):
#         print("%s " % self.name)
#         self.height += 1
#
#
# people = Person("xiaoming", 180)
# people.run()
# print(people)


# class HouseItem(object):
#
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "add furniture %s, area is %.2f" % (self.name, self.area)
#
#
# bed = HouseItem("席梦思", 4)
# table = HouseItem("书桌", 3)
# chest = HouseItem("书柜", 1)
#
#
# class House(object):
#
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.total_area = area
#         # 剩余面积
#         self.free_area = area
#         # 家具列表
#         self.furniture_list = []
#
#     def add_item(self, item):
#         if item.area > self.total_area:
#             print("so big")
#             return
#         else:
#             self.free_area -= item.area
#             self.furniture_list.append(item.name)
#
#     def __str__(self):
#         return "房子的户型为%s,\n总面积：%.2f\n剩余面积：%.2f\n共有家具为%s" \
#                % (self.house_type, self.total_area, self.free_area, self.furniture_list)
#
#
# my_home = House("2居", 100)
# my_home.add_item(bed)
# my_home.add_item(table)
# my_home.add_item(chest)
# print(my_home)


# class Anmial(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def dark(self):
#         print("%s wangwang" % self.name)
#
# class Dog(Anmial):
#     def dark(self):
#         super().dark()
#         print("小王八")
#
# s1 = Dog("哮天犬")
# s1.dark()

# class Tools(object):
#
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Tools.count += 1
#
#     @classmethod
#     def count_example(cls):
#
# s1 = Tools("wang")
# s2 = Tools("li")
# print(Tools.count)


class Demo(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


s1 = Demo()
s2 = Demo()
print(s1)
print(s2)


