# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2014

@author: lisong
局部变量
全局变量
'''
a_string = "This is a global variable"

def foo():
    print locals()
    
def bar():
    print globals()
    
foo()
bar()