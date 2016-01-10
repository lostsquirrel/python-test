# -*- encoding: utf-8 -*-
'''
Created on 2015-05-12

@author: lisong
'''
from math import sqrt
import __main__

def test_14():
    number = input("Enter an integer: ")
    maz = number
    while number != 0:
        number = input("Enter an integer: ")
        print "number", number, type(number), maz, type(maz)
        if number > maz:
            maz = number
    print "number", number
    
def test_16():
    print sqrt(3)*sqrt(3) == 3
    
def test_18():
    k=1000  
    while k>1:   
        print k
        k = k/2
        
def test_25():
    dict1 = {} 
    dict2 = { 3 : 5 } 
    dict4 = {(1,2,3): 'uestc'} 
    dict3 = {[1,2,3]: 'uestc'} #TypeError: unhashable type: 'list'
    
def test_29():
    x = 7.0
    y = 5
    print x % y
    
def test_31():
    a,b=1,2
    x = a if a>b else b
    print x
    
def test_33():
    test = 1
    def set_test_value_one():
        test = 5
        test = test + 1
    def set_test_value_two():
        global test
        test = 10
    set_test_value_one()
    print test
    set_test_value_two()
    print test
    
def test_34():
    def fib(n):
        f1, f2 = 0, 1
        while f2 < n:
            print f2,
            f1, f2 = f2, f1 + f2
    fib(10)
if __name__ == '__main__':
    test_34()