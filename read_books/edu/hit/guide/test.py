'''
Created on May 12, 2015

@author: lisong
'''
def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        r = m % n
    return gcd(n, r)
print gcd(384, 84)
if __name__ == '__main__':
    pass