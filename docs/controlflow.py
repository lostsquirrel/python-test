
def demo_0():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break
        else:
            # loop fell through without finding a factor
            print n, 'is a prime number'
            

'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
'''
                   
def demo_1():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break
        print n, 'is a prime number'
    
# demo_1()

'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
4 is a prime number
5 is a prime number
6 equals 2 * 3
6 is a prime number
7 is a prime number
8 equals 2 * 4
8 is a prime number
9 equals 3 * 3
9 is a prime number
'''

def demo_2():
    x = 10
    while x > 0:
        x = x - 1
        if x % 2 == 0:
            pass
#             break
        print 'finish in this round with x = %s' % x
    else:
        print x
        
demo_2()
        