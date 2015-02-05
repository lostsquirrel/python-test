# -*- coding: utf-8 -*-
#解析green vpn服务器列表
from db_conn import serverBatchInsert
import time

def read():
    f = open('greenvpn.txt')
    data = list()
    key = list()
    for line in f:
        if line.endswith("\n"):
            line = line[:-1]
        if line.endswith('正常'):
#             print line
            line = '0'
#         line = line.decode(encoding='UTF-8',errors='strict')
        line = line.decode('UTF-8')
        print line
        if line.isdigit():
            line = int(line)
        key.append(line)
        
        if len(key) == 5:
            key.append(time.time())
            data.append(key)
            key = list()
#         print key
    return data

def buildData(data):
    for index in range(1, len(data)):
        for x in data[index]:
            print x
        
if __name__ == "__main__":
    data = read()
    data = data[1:]
    print data
    serverBatchInsert(data)
