# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2014

@author: lisong
查找一个变量先从局部变量找，没找到再从全局变量中找
'''
a_string = "This is a global variable"
def foo():
     
    print a_string 
    #Python looks for a local variable in our function and
    # not finding one, looks for a global variable[2] of the same name.
    
foo()

def bar():
    a_string = "test"
    print locals()
    
bar()
print a_string