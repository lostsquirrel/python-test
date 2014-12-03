# -*- coding: utf-8 -*-
'''
Created on Dec 3, 2014

@author: lisong
'''
xxx = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
def p2cor(p):
    x = xxx.index(p[0])
    y = int(p[1]) - 1
    return x,y 
def c2p(x, y):
    return "%s%d" % (xxx[x], y + 1)

def is_safe(position, pawns):
    x, y = p2cor(position)
    if y == 0:
        #已经在第一行
        return False
    else:
        left = False
        right = False
        x1 = x - 1
        y1 = y - 1
        
        if x1 >= 0:
            left = c2p(x1, y1) in pawns
        x2 = x + 1
        if x2 <= 7:
            right = c2p(x2, y1) in pawns
        return  left or right
     
def safe_pawns(pawns):
    res = 0
    for p in pawns:
        if is_safe(p, pawns):
            res += 1
    return res


'''
参考python3
def safe_pawns(pawns):
    answer = 0
    for pawn in pawns :
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
    return answer
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
