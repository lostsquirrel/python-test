# -*- coding: utf-8 -*-
#求阶乘
import time
def factI(n):
	""" n须为大于0的整数"""
	res = 1
	while n > 1:
		res = res * n
		n -= 1
	return res

def factR(n):
	""" n须为大于0的整数"""
	if n == 1 :
		return 1
	return n * factR(n - 1)
num = 900

startI = time.time()
a = factI(num)
endI = time.time()
b = factR(num)
endR = time.time()
print 'time I:', endI - startI
print 'time R', endR - endI
print a
print b
