# -*- coding: utf-8 -*-
#选择最佳vpn服务器

from subprocess import call
from subprocess import check_output
import subprocess
from db_conn import getIps
from db_conn import pingInsert
from db_conn import getPingbyIp
import time
import operator

ipList = getIps()
# print check_output("ping", "127.0.0.1")
# call(["ls", "-l"])


# msg = '64 bytes from 220.181.111.86: icmp_seq=1 ttl=54 time=39.3 ms'
def parseMsg(msg):
    try :
        data = dict()
        # print msg.index('from')
        # print msg.index(':')
        data['ip']=msg[msg.index('from') + 5 : msg.index(':',msg.index('from'))]
        # print msg.index('ttl')
        data['ttl']=msg[msg.index('ttl') + 4 : msg.index(' ',msg.index('ttl'))]
        # print msg.index('time')
        data['time']=msg[msg.index('time') + 5 : msg.index(' ',msg.index('time'))]
        # print msg.index('ms')
        return data
    except :
        print "Parser message %s Error" % msg
        
def doPing(ip):
    p = subprocess.Popen('ping -w 3 %s' % ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for msg in p.stdout.readlines():
        print msg
        if (msg.endswith(' ms\n')):
            data = parseMsg(msg)
            if not data == None:
                data = (data['ip'], data['ttl'], data['time'], time.time())
                pingInsert(data)
                
def getAverate(data): 
    count = 0
    sum = 0
    for i in data:
        count += 1
        sum += i[0]
    if (count == 0):
        return -1
    
    return sum / count
                
if __name__ == "__main__":
    x = dict()
    for ip in ipList:
        ip = ip[0]
        data = getPingbyIp(ip)
#         print data
        x[ip] = getAverate(data)
        
sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
print sorted_x