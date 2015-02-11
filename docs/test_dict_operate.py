# -*- coding:utf-8 -*-
'''
Created on 2015-02-11

@author: lisong
'''

if __name__ == '__main__':
    d1 = dict(a = 1, b = 2, c = 3)
    d2 = dict(c = 33, d = 5, e = 6)
#     d1.update(d2)
    print d1
    d2.update(d1)
    print d2