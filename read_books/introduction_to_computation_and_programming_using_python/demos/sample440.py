# -*- coding: utf-8 -*-
#Fibonacci sequence
#使用全局变量统计方法被调用的次数
def fib(n):
	"""n是大于零的整数"""
	global numCalls
	numCalls += 1
	if n == 0 or n == 1 :
		return 1
	return fib(n - 1) + fib(n - 2)

def testFub(n):
	for x in xrange(n + 1):
		global numCalls
		numCalls = 0
		print 'fib of ',x,'=',fib(x)
		print 'numCalls =', numCalls
		print '-----------'

testFub(10)