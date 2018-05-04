# -*- coding: utf-8 -*-
# 拆分 sha256sum 文件

def read(file):
    fh = open(file)
    for line in fh:
        name = line.split(" ")[-1].strip()
        fhl = open("%s.sha256" % name, 'w')
        fhl.write(line)
        fhl.flush()
        fhl.close()
    fh.close()

if __name__ == '__main__':
    f = "C:\\Users\\lisong\\Downloads\\sha256sum.txt"
    read(f)
