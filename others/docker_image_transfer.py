# -*- coding:utf-8 -*-
"""
get images in vps and transfer to aliyun registry
"""
import os
import sys


aliyun_registry_url = 'registry.cn-hangzhou.aliyuncs.com'
aliyun_registry_namespace = 'lisong'


def transfer_single(action, image):
    if '0' == action:
        transfer2aliyun(args[2])
    if '1' == action:
        transfer2origin(args[2])


def transfer_multiply(action):
    fh = open('images.txt')
    for image in fh:
        transfer_single(action, image.strip('\n'))


def transfer2origin(image):
    aliyun_image = parse_image_name(image)

    os.system('docker pull %s' % aliyun_image)
    cmd = 'docker tag %s %s' % (aliyun_image, image)
    print cmd
    os.system(cmd)


def transfer2aliyun(image):

    aliyun_image = parse_image_name(image)

    os.system('docker pull %s' % image)
    cmd = 'docker tag %s %s' % (image, aliyun_image)
    print cmd
    os.system(cmd)
    os.system('docker push %s' % aliyun_image)


def parse_image_name(image):
    tagged_image_name = image.strip('\n')[image.rfind("/") + 1:]
    aliyun_image = '%s/%s/%s' % (aliyun_registry_url, aliyun_registry_namespace, tagged_image_name)
    return aliyun_image


if __name__ == '__main__':
    args = sys.argv
    # 0 single image pass by arg tag and push to aliyun
    # 1 single image pass by arg pull and tag to origin
    # 2 multiply images pass by images.txt tag and push to aliyun
    # 3 multiply images pass by images.txt  pull and tag to origin
    if int(args[1]) <= 1:
        transfer_single(args[1], args[2])
    else:
        transfer_multiply(args[1])


