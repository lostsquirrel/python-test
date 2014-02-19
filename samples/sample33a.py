# -*- coding: utf-8 -*-
#求一个数的平方根(二分查找)
x = 2
epsilon = 0.000001
numGuess = 0
low = 0.0
high = max(1.0, x)
ans = (low + high) / 2.0
while abs(ans * ans - x) > epsilon:
	numGuess += 1
	if ans ** 2 < x:
		low = ans
	else :
		high = ans
	ans = (low + high) / 2.0
print 'numGuess:', numGuess
print ans, '接近', x, '的平方根'