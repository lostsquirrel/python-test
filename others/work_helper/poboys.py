# -*- coding: utf-8 -*-
import re
import os

def readfile(filename):
    fh = open(filename)
    content = fh.read()
    pattern = r"com.casino.util.TransactionUtils"
    items = re.compile(pattern).split(content)
    p = re.compile(r"\<a\:TransactionStatus\>500\<\/a\:TransactionStatus\>")
    res = ''
    for index in range(len(items)):
        # print item
        m = p.search(items[index])

        if m is not None:
            print(m.group())
            res += items[index - 1]
            res += items[index]
        print('-------------------------------------')
    # print(len(items))
    fh.close()
    return res
def read_dir(dir_name):
    res = ''
    for dir in os.listdir(dir_name):
        print(dir)
        res += readfile("%s\\%s" % (dir_name, dir))

    fh = open("%s\\%s" % (dir_name, "500.log"), 'w')
    fh.write(res)
    fh.flush()
    fh.close()
# print(re.escape("<a:TransactionStatus>500</a:TransactionStatus>"))
# x = re.search("\d+:\d+:\d+.\d+ \\[.*\\] INFO  com.casino.util.TransactionUtils \\- ", "01:34:55.714 [http-bio-8080-exec-13] INFO  com.casino.util.TransactionUtils - ")
# print(x.group(0))
# readfile("G:\\poboys\\magensa_pay.2018-11-02.log")
read_dir("G:\\poboys")