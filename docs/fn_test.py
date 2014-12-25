'''
Created on Sep 19, 2014

@author: lisong
'''
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

def f_v1(a, L=[]):
    L.append(a)
    return L

def f_v2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

if __name__ == '__main__':
    pass
#     fib(2000)
#     print  ask_ok('Are you ok?')
    print f_v1(1)
    print f_v1(2)
    print f_v1(3)
    print f_v2(1)
    print f_v2(2)
    print f_v2(3)
