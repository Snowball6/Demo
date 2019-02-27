# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/2/27 8:57

import subprocess
import os


def tomcat_install():
    """
     注意： 安装tomcat 前 必须确保机器上已部署好jdk环境
     需要按需求修改的变量：
    1 、 install_path：软件包（tar、rpm）包存放路径，请手动新建一个目录，并将tar包放到该路径下,一定要以 / 结尾
    2 、 tomcat_home_path ：解压包后 tomcat 的部署路径，一定要以  / 结尾
    :return:
    """
    install_path = "/tmp/tomcat/"
    tomcat_home_path = "/opt/payment/soft/"
    tomcat_dir = "/bin"   # 启动路径
    if not os.path.exists(tomcat_home_path):
        os.makedirs(tomcat_home_path)
    tar_name = subprocess.Popen("cd %s && ls " % install_path, shell=True, stdout=subprocess.PIPE).stdout.readline().\
        strip().decode()
    subprocess.Popen("cd %s && tar -zxvf %s " % (install_path, tar_name), shell=True).wait()
    tomcat_name = subprocess.Popen("cd %s && ls" % install_path, shell=True, stdout=subprocess.PIPE).stdout.readline().strip().decode()
    subprocess.Popen("cd %s && mv %s %s" % (install_path, tomcat_name, tomcat_home_path), shell=True).wait()
    subprocess.Popen("cd %s%s%s && ./startup.sh" % (tomcat_home_path, tomcat_name, tomcat_dir), shell=True)


def main():
    tomcat_install()


if __name__ == "__main__":
    main()