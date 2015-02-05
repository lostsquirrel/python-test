'''
Created on Feb 3, 2015

@author: lisong
'''
def foo(a = None):
    print a
    
def bar(b = None):
    foo(b)
if __name__ == '__main__':
    x = None
    y = 3
    bar(x)
    bar(y)
    bar()