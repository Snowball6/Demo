# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/2/20 17:15


class Demo(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if Demo.init_flag:
            return
        print("-" * 50)
        Demo.init_flag = True


s1 = Demo()
s2 = Demo()
print(s1)
print(s2)