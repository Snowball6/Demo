# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/2/25 9:40

import subprocess


def java_version():
    """
    判断 原有机器上是否安装jdk，如果有，则卸载后安装。
    :return:
    """
    java_install = subprocess.Popen("rpm -qa | grep java", shell=True, stdout=subprocess.PIPE)
    return_code = java_install.wait()
    if return_code == 1:
        print("该机器上未安装jdk")
    else:
        for java_exist_name in java_install.stdout.readlines():
            format_name = java_exist_name.strip().decode()
            subprocess.Popen("rpm -e --nodeps %s" % format_name)


if __name__ == "main":
    java_version()