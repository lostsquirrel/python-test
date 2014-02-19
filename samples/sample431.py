# -*- coding: utf-8 -*-
#Fibonacci sequence
def fib(n):
	"""n是大于零的整数"""
	if n == 0 or n == 1 :
		return 1
	return fib(n - 1) + fib(n - 2)

def testFub(n):
	for x in xrange(n + 1):
		print 'fib of ',x,'=',fib(x)

testFub(10)