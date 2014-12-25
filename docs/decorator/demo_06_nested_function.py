# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2014

@author: lisong

函数嵌套时， 内部函数可以使用外部函数的变量
'''
def outer():
    x = 1
    def inner():
        print x # 1
    inner() # 2
    
outer()