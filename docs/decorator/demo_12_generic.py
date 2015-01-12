'''
Created on Jan 12, 2015

@author: lisong
12. More generic decorators
'''
def logger(func):
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs) #2
    return inner

@logger
def foo1(x, y=1):
    return x * y

@logger
def foo2():
    return 2

print foo1(5, 4)
print foo1(x = 3, y = 4)

print foo1(1)


print foo2()
