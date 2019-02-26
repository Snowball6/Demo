# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/2/25 9:40

import subprocess
import os


def jdk_version():
    """
    判断 原有机器上是否安装jdk，如果有，则卸载后安装,新建的虚拟机 无需执行此函数，如需则在main函数中调用此方法
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
    """
    脚本需要修改的变量：
    1 、 install_path : 软件包（tar、rpm）包存放路径，请手动新建一个目录，并将tar包放到该路径下,一定要以 / 结尾
    2 、 jdk_home_path :解压包后 jdk的部署路径，一定要以  / 结尾
    """
    # 如果机器可连外网，可以直接通过外网下载安装
    install_path = "/tmp/jdk/"
    if not os.path.exists(install_path):
        os.makedirs(install_path)
    # subprocess.Popen("wget -P %s (将此处替换为jdk下载链接)" % install_path)   # 如果机器可通外网，可通过此方式直接下载

    jdk_name = subprocess.Popen("cd %s && ls" % install_path, shell=True, stdout=subprocess.PIPE)
    jdk_code = jdk_name.wait()
    if jdk_code == 1:
        print("未找到jdk安装包")
    else:
        jdk_tar = jdk_name.stdout.readline().strip().decode()
        jdk_home_path = "/opt/payment/soft/"
        if not os.path.exists(jdk_home_path):
            os.makedirs(jdk_home_path)
        # 解压 安装包
        subprocess.Popen("cd %s && tar -zxvf %s" % (install_path, jdk_tar), shell=True).wait()
        # 获取 解压后的jdk文件夹名称 并移动到指定部署路径下
        global_jdk_path = subprocess.Popen("ls %s" % install_path, shell=True, stdout=subprocess.PIPE).stdout.readline().strip().decode()
        subprocess.Popen("mv %s%s %s" % (install_path, global_jdk_path, jdk_home_path), shell=True)

        subprocess.Popen("echo export JAVA_HOME=%s%s >> /etc/profile" % (jdk_home_path, global_jdk_path ), shell=True)
        subprocess.Popen("echo export CLASSPATH=.:'$JAVA_HOME'/lib/dt.jar:'$JAVA_HOME'/lib/tools.jar >> /etc/profile", shell=True)
        subprocess.Popen("echo export PATH='$JAVA_HOME'/bin:'$PATH' >> /etc/profile", shell=True)
        subprocess.Popen("source /etc/profile", shell=True)
        result = subprocess.Popen("java -version", shell=True, stdout=subprocess.PIPE)
        result_code = result.wait()
        if result_code == 1:
            print("%s 安装失败" % jdk_home_path)
        else:
            print("%s 安装成功" % jdk_home_path)
            print(result.stdout.read())


def main():
    jdk_install()


if __name__ == "__main__":
    main()
