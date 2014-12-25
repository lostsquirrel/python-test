# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2014

@author: lisong
闭包
'''
'''
def outer():
    x = 1
    def inner():
        print x
    return inner

foo = outer()
foo() still working
print foo.func_closure # doctest: +ELLIPSIS
'''
def outer(x):
    
    def inner():
        print x
    return inner

print1 = outer(1)
print2 = outer(2)
print1()
print2()