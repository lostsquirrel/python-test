'''
Created on Dec 2, 2014

@author: lisong
'''

xxx = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
def p2cor(p):
    x = xxx.index(p[0])
    y = int(p[1]) - 1
    return x,y 
def c2p(x, y):
    return "%d%d" % (xxx[x], y + 1)

def is_safe(position, pawns):
    
    return False

xx = dict(a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7)

print xxx.index('a')

print xxx[0]
print xx.get('a')
