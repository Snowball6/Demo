# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/2/25 9:40

import subprocess
import os


def jdk_version():
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
            print("执行命令：rpm -e --nodeps %s" % format_name)
            subprocess.Popen("rpm -e --nodeps %s" % format_name)


def jdk_install():
    # 如果机器可连外网，可以直接通过外网下载安装
    # 判断安装路径是否存在，如果不存在则创建
    install_path = "/tmp/jdk"
    # if not os.path.exists(install_path):
    #     os.makedirs(install_path)
    # subprocess.Popen("wget -P %s (将此处替换为jdk下载链接)" % install_path)

    subprocess.Popen("cd %s" % install_path, shell=True)
    jdk_name = subprocess.Popen("ll" ,shell=True,stdout=subprocess.PIPE)
    jdk_code = jdk_name.wait()
    if jdk_code == 1:
        print("未找到jdk安装包")
    else:
        jdk_tar = jdk_name.stdout.readline()
        jdk_home_path = "/opt/payment/soft/"
        subprocess.Popen("tar -zcvf %s -C %s" %(jdk_tar, jdk_home_path), shell=True)
        subprocess.Popen("echo export JAVA_HOME=%s+%s >> /etc/profile" % (jdk_home_path,jdk_tar), shell=True)
        subprocess.Popen("echo export JRE_HOME=${JAVA_HOME}/jre >> /etc/profile", shell=True)
        subprocess.Popen("echo export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib >> /etc/profile", shell=True)
        subprocess.Popen("echo PATH=${JAVA_HOME}/bin:$PATH >> /etc/profile", shell=True)
        subprocess.Popen("source /etc/profile", shell=True)
        result = subprocess.Popen("java -version", shell=True, stdout=subprocess.PIPE)
        print(result.stdout.read())


if __name__ == "main":
    jdk_install()