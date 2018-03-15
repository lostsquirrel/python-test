#/usr/bin/python
# -*- coding:utf-8 -*-
"""
get images in vps and transfer to aliyun registry
"""
import os
import sys
import logging

log = logging.getLogger(__name__)


aliyun_registry_url = 'registry.cn-hangzhou.aliyuncs.com'
local_registry_url = 'registry.lisong.pub:5000'


class DockerImageTransfer:

    def __init__(self, image, aliyun_registry_namespace, direct):
        self.tagged_image_name = None
        self.registry_url = None
        self.registry_namespace = ''
        if not aliyun_registry_namespace.startswith("/"):
            aliyun_registry_namespace = "/%s" % aliyun_registry_namespace
        self.aliyun_registry_namespace = aliyun_registry_namespace
        self.image = image
        self.direct = direct
        self.parse_image()

    def transfer2aliyun(self):
        """
        在没有墙的环境下，下载镜像并打为 aliyun 的镜像，再推送
        """
        aliyun_image = self.get_aliyun_image()
        pull_image(self.image)
        tag_image(self.image, aliyun_image)
        push_image(aliyun_image)

    def transfer2origin(self):
        """
        在工作环境，从 aliyun 拉取对应的镜像，再打为原来的镜像名称
        """
        aliyun_image = self.get_aliyun_image()
        tag_image(aliyun_image, self.image)

    def transfer2local(self):
        remote_image = self.image
        if not self.direct:
            remote_image = self.get_aliyun_image()

        pull_image(remote_image)
        local_image = self.get_local_image()

        tag_image(remote_image, local_image)
        push_image(local_image)

    def get_aliyun_image(self):
        return '%s%s/%s%s' % (aliyun_registry_url, self.aliyun_registry_namespace, self.tagged_image_name, self.registry_namespace.replace("/", "-"))

    def get_local_image(self):
        return '%s%s/%s' % (local_registry_url, self.registry_namespace, self.tagged_image_name)

    def parse_image(self):
        c = self.image.count('/')

        if c > 1:
            name_space_start = self.image.find("/")
            name_space_end = self.image.rfind("/")
            self.tagged_image_name = self.image.strip('\n')[name_space_end + 1:]
            self.registry_namespace = self.image[name_space_start:name_space_end]
            self.registry_url = self.image[:name_space_start]

        elif c > 0:
            sep = self.image.rfind("/")
            self.tagged_image_name = self.image.strip('\n')[sep + 1:]
            self.registry_url = self.image[:sep]

        else:
            self.tagged_image_name = self.image

    def transfer_single(self, act):
        transfer_actions = {
            0: self.transfer2aliyun,
            1: self.transfer2origin,
            2: self.transfer2local
        }
        transfer_actions[act]()


def transfer_multiply(action, registry_namespace, isDirect):
    fh = open('images.txt')
    action %= 10
    log.info("action %s ", action)
    x = 0

    for image in fh:
        w = DockerImageTransfer(image.strip('\n'), registry_namespace, isDirect)
        w.transfer_single(action)
        x += 1
    log.info("%d images transfer" % x)


def pull_image(image):
    log.info("pull image %s" % image)
    os.system('docker pull %s' % image)


def push_image(image):
    log.info("push image %s" % image)
    os.system('docker push %s' % image)


def tag_image(source_image, target_image):
    log.info("tag image %s to %s" % (source_image, target_image))
    os.system('docker tag %s %s' % (source_image, target_image))


if __name__ == '__main__':
    args = sys.argv
    # 0 single image pass by arg tag and push to aliyun
    # 1 single image pass by arg pull from aliyun and tag to origin
    # 2 single image pass by arg pull from aliyun and tag to local
    # 10 multiply images pass by images.txt tag and push to aliyun
    # 11 multiply images pass by images.txt  pull from aliyun and tag to origin
    # 12 multiply images pass by images.txt  pull from aliyun and tag to local
    action = int(args[1])
    registry_namespace = "/lisong"
    isDirect = False
    if action < 10:
        if len(args) > 3:
            registry_namespace = args[3]
        if len(args) > 4:
            isDirect = True
        DockerImageTransfer(args[2].strip('\n'), registry_namespace, isDirect).transfer_single(action)
    else:
        if len(args) > 2:
            registry_namespace = args[2]
        if len(args) > 3:
            isDirect = True
        transfer_multiply(action, registry_namespace, isDirect)


