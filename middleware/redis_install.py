# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/2/28 14:16

import subprocess
import os


def redis_install():
    """
    需要修改的变量如下：
    1 、 install_path : 软件包（tar、rpm）包存放路径，请手动新建一个目录，并将tar包放到该路径下,一定要以 / 结尾
    2 、 redis_home_path :解压包后 redis的部署路径，一定要以  / 结尾
    3、  configuration_dir : redis.conf配置文件存放路径，建议在 部署路径中（即redis_home_path）后建立/etc文件存储 ,一定要以  / 结尾
    :return:
    """
    install_path = "/tmp/redis/"
    redis_dir = "/usr/local/redis/"
    configuration_dir = "/usr/local/redis/etc/"
    if not os.path.exists(redis_dir,):
        os.makedirs(redis_dir,)
    if not os.path.exists(configuration_dir):
        os.makedirs(configuration_dir)
    tar_name = subprocess.Popen("cd %s && ls" % install_path, shell=True, stdout=subprocess.PIPE).stdout.readline().strip().decode()
    subprocess.Popen("cd %s && tar -zxvf %s" % (install_path, tar_name), shell=True).wait()
    redis_name = subprocess.Popen("cd %s && ls" % install_path, shell=True, stdout=subprocess.PIPE).stdout.readline().strip().decode()
    subprocess.Popen("cd %s%s && make" % (install_path, redis_name), shell=True,).wait()
    subprocess.Popen("cd %s%s/src && make install PREFIX=%s" % (install_path, redis_name, redis_dir), shell=True,).wait()

    subprocess.Popen("cd %s%s && mv redis.conf %s" %(install_path, redis_name, configuration_dir), shell=True).wait()
    os.system("sed -i 's/daemonize no/daemonize yes/g' %sredis.conf" % configuration_dir)
    subprocess.Popen("echo %sbin/redis-server >> /etc/rc.local && echo %sredis.conf >> /etc/rc.local" % (redis_dir, configuration_dir), shell=True)
    subprocess.Popen("%sbin/redis-server %sredis.conf >> /etc/rc.local" % (redis_dir, configuration_dir), shell=True)


def main():
    redis_install()


if __name__ == '__main__':
    main()
