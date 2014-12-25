# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2014

@author: lisong

函数就是一个对象
'''
def foo():
    pass

print issubclass(foo.__class__, object)
print foo.__class__

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def applyx(func, x, y):
    return  func(x, y)

a = 2
b = 1

print applyx(add, a, b)
print applyx(sub, a, b)


def outer():
    def inner():
        print "Inside inner"
    return inner # 1

f = outer() #2
print f
f()