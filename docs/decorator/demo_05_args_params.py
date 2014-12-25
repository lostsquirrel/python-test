# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2014

@author: lisong
一个函数可有默认参数
'''
def foo(x):
    print locals()
    
foo(1)

def bar(x, y = 0):
    return x - y

print bar(3, 1)
print bar(3)
print bar(y = 1, x = 3)
# bar() #TypeError: bar() takes at least 1 argument (0 given