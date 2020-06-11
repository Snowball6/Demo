#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2020/6/11 9:44
# @Author : Snowball
import subprocess


def apply_port():
    # process_name = "memcached"
    find_process = subprocess.Popen("ps -ef | grep %s | grep -v 'grep' | awk '{print $2}'" % process_name, shell=True,
                                    stdout=subprocess.PIPE)
    process_list = [i for i in find_process.stdout.read().strip().split("\n")]
    if process_list[0]:
        for port in process_list:
            process = subprocess.Popen("ps -ef | grep %s | grep -v 'grep'" % port, shell=True, stdout=subprocess.PIPE).stdout.read()
            find_port = subprocess.Popen("netstat -ntlp | grep %s | awk '{print $4}' | cut -d':' -f '4'" % port, shell=True,
                                         stdout=subprocess.PIPE).stdout.read().replace("\n", ",")
            print(process_name, process, find_port)
    else:
        print("%s进程不存在" % process_name)


if __name__ == "__main__":
    apply_port()