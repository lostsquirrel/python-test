# -*- coding:utf-8 -*-
"""
get images in vps and transfer to aliyun registry
"""
import os
import sys
import logging

log = logging.getLogger(__name__)


aliyun_registry_url = 'registry.cn-hangzhou.aliyuncs.com'
aliyun_registry_namespace = '/lisong'
local_registry_url = 'registry.lisong.pub:5000'
local_registry_namespace = '/'


def transfer_single(action, image):
    transfer_actions = {
        0: transfer2aliyun,
        1: transfer2origin,
        2: transfer2local
    }
    transfer_actions[action](image)


def transfer_multiply(action):
    fh = open('images.txt')
    action %= 10
    log.info("action %s ", action)
    x = 0
    for image in fh:
        transfer_single(action, image.strip('\n'))
        x += 1
    log.info("%d images transfer" % x)


def transfer2origin(image):
    aliyun_image = pull_from_aliyun(image)
    tag_image(aliyun_image, image)


def transfer2local(image):
    aliyun_image = pull_from_aliyun(image)
    local_image = parse_image_name_to_local(image)
    tag_image(aliyun_image, local_image)


def pull_from_aliyun(image):
    aliyun_image = parse_image_name_to_aliyun(image)
    pull_image(aliyun_image)
    return aliyun_image


def pull_image(image):
    log.info("pull image %s" % image)
    os.system('docker pull %s' % image)


def push_image(image):
    log.info("push image %s" % image)
    os.system('docker push %s' % image)


def tag_image(source_image, target_image):
    log.info("tag image %s to %s" % (source_image, target_image))
    os.system('docker tag %s %s' % (source_image, target_image))


def transfer2aliyun(image):
    aliyun_image = parse_image_name_to_aliyun(image)
    pull_image(image)
    tag_image(image, aliyun_image)
    push_image(aliyun_image)


def parse_image_name_to_aliyun(image):
    return transfer_image_name(image, aliyun_registry_url, aliyun_registry_namespace)


def parse_image_name_to_local(image):
    return transfer_image_name(image, local_registry_url, local_registry_namespace)


def transfer_image_name(source_image, target_registry_url, target_registry_namespace):
    tagged_image_name = source_image.strip('\n')[source_image.rfind("/") + 1:]
    return '%s%s/%s' % (target_registry_url, target_registry_namespace, tagged_image_name)


if __name__ == '__main__':
    args = sys.argv
    # 0 single image pass by arg tag and push to aliyun
    # 1 single image pass by arg pull from aliyun and tag to origin
    # 2 single image pass by arg pull from aliyun and tag to local
    # 10 multiply images pass by images.txt tag and push to aliyun
    # 11 multiply images pass by images.txt  pull from aliyun and tag to origin
    # 12 multiply images pass by images.txt  pull from aliyun and tag to local
    action = int(args[1])
    if action < 10:
        transfer_single(action, args[2])
    else:
        transfer_multiply(action)


