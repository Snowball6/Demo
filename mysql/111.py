#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/9 12:59
# @Author : Snowball



from datetime import datetime
#构造一个将来的时间
def test(h):
    h = "2019-08-08"
    future = datetime.strptime('%s 08:00:00'% h, '%Y-%m-%d %H:%M:%S')
    #当前时间
    now = datetime.now()
    #求时间差
    delta = future - now
    hour = delta.seconds/60/60
    minute = (delta.seconds - hour*60*60)/60
    seconds = delta.seconds - hour*60*60 - minute*60
    print_now=now.strftime('%Y-%m-%d %H:%M:%S')
    print("今天是：",print_now)
    print("距离 2019-02-01 \"work\" 还剩下：%d天" % delta.days)
    print(delta.days,hour, minute, seconds)


if __name__ == '__main__':
    h = "2019-01-01"
    test(h)