# -*- coding: utf-8 -*-
#求一个数的平方根
x = int(raw_input("请输入一个大于0的数： "))
epsilon = 0.01
step = epsilon ** 2
numGuess = 0
ans= 0.0
while abs(ans ** 2 - x) >= epsilon and ans ** 2 <= x:
	ans += step
	numGuess += 1
print 'numGuess:', numGuess
if abs(ans ** 2 - x) > epsilon:
	print '没有成功找到',x,'的平方根'
else :
	print ans, '接近', x, '的平方根'