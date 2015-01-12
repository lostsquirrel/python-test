'''
Created on Jan 12, 2015

@author: lisong
'''
def outer(some_func):
    def inner():
            print "before some_func"
            ret = some_func() # 1
            return ret + 1
    return inner

def foo():
    return 1

# decorated = outer(foo) # 2
# print decorated()
#############################
# foo =  outer(foo)
# 
# print foo()
###############################
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y =  y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)
    
def add(a, b):
        return Coordinate(a.x + b.x, a.y + b.y)
    
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)
 
print add(one, two)


# Coord: {'y': 400, 'x': 400}
# Coord: {'y': 0, 'x': -200}
# Coord: {'y': 100, 'x': 0}
#  Perhaps you can only sum or subtract based on positive coordinates and any result should be limited to positive coordinates as well. 

def wrapper(func):
    def checker(a, b): # 1
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

add = wrapper(add)
sub = wrapper(sub)

three = Coordinate(-100, -100)
print  sub(one, two)
print add(one, three)
# Coord: {'y': 400, 'x': 400}
# Coord: {'y': 0, 'x': 0}
# Coord: {'y': 200, 'x': 100}