# -*- coding: utf-8 -*-
#异常处理示例

def successFailureRatio(numSuccesses, numFailures):
	return numSuccesses / float(numFailures)

def successFailureRatio2(numSuccesses, numFailures):
	res = None
	try:
		res = numSuccesses / float(numFailures)
	except ZeroDivisionError:
		pass
	return res

print successFailureRatio2(0,100)
print successFailureRatio2(10,90)
print successFailureRatio2(60,40)
print successFailureRatio2(100,0)