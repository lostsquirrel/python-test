# -*- coding: utf-8 -*-
# 选择最佳vpn服务器 仅 windows 中文件适用

from multiprocessing import Process
import subprocess
import re

ipList = [
# 'hnd-jp-ping.vultr.com',
# 'sgp-ping.vultr.com',
# 'syd-au-ping.vultr.com',
# 'fra-de-ping.vultr.com',
# 'ams-nl-ping.vultr.com',
# 'lon-gb-ping.vultr.com',
# 'par-fr-ping.vultr.com',
# 'wa-us-ping.vultr.com',
# 'sjo-ca-us-ping.vultr.com',
# 'lax-ca-us-ping.vultr.com',
# 'il-us-ping.vultr.com',
# 'tx-us-ping.vultr.com',
# 'nj-us-ping.vultr.com',
# 'ga-us-ping.vultr.com',
# 'fl-us-ping.vultr.com'
    '140.82.17.199'
]
# print check_output("ping", "127.0.0.1")
# call(["ls", "-l"])
result = []


# msg = '64 bytes from 220.181.111.86: icmp_seq=1 ttl=54 time=39.3 ms'
def parseMsg(contents):
    try:
        data = dict()
        lose = contents[-3]
        data['lost'] = int(re.split(r"\(|%", lose)[1])
        spent = contents[-1]
        ss = re.split(r"=|ms", spent)
        data['delay']=[int(ss[1]), int(ss[3]), int(ss[5])]
        # print_gbk(spent)
        return data
    except:
        print "Parser message %s Error" % contents


def doPing(ip, result):
    p = subprocess.Popen('ping -n 50 -w 3 %s' % ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = parseMsg(p.stdout.readlines())
    if data is not None:
        data['ip'] = ip
        print data
        result.append(data)


def print_gbk(msg):
    print msg.decode('gbk')


if __name__ == "__main__":
    plist = list()
    for ip in ipList:
        # doPing(ip)
        p = Process(target=doPing, args=(ip,result))
        p.start()
        plist.append(p)
    for p in plist:
        p.join()
    sorted(result, cmp=lambda x, y: x.lost > y.lost)
    for item in result:
        print item
    #     ip = ip[0]
    # data = getPingbyIp(ip)
#         print data
#         x[ip] = getAverate(data)
