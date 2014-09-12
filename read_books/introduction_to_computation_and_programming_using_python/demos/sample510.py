# -*- coding: utf-8 -*-
#找两个数的最大公约数和最小公约数
def findExtremeDivisors(n1, n2):
	"""n1,n2 正整数;返回大于1的公约数"""
	minVal, maxVal = None, None
	for i in xrange(2, min(n1, n2) + 1):
		if n1 % i == 0 and n2 % i == 0:
			if minVal == None or i < minVal:
				minVal = i
			if maxVal == None or i > maxVal:
				maxVal = i 
	return (minVal, maxVal)
