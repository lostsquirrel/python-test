'''
Created on Jan 12, 2015

@author: lisong
11. *args and **kwargs
'''
def one(*args):
    print args
    
one()
one(1, 2, 3)    
def two(x, y, *args): # 2
        print x, y, args

two('a', 'b', 'c', 'd')      
two('a', 'b', 'c')
two('a', 'b')

def add(x, y):
    return x + y

lst = [1,2]
print add(*lst) # 2



def foo(**kwargs):
    print kwargs
    
foo(x=1, y=2)
# foo(1, y=2)  foo() takes exactly 0 arguments (2 given)
# foo(1, 2)

def bar(x, y):
    return x + y

dct = {'x': 1, 'y': 2}
print bar(**dct)
print add(**dct)