#-*- coding: utf-8 -*-
#用牛顿迭代法求一个数的平方根

y = 25
epsilon = 0.01
guess = y / 2.0
guessNum = 0
while abs(guess * guess - y ) >= epsilon:
	guess = guess - (guess * guess - y) / (2 * guess)
	print guess
	guessNum += 1
print guess, '近 似', y,' 的  平 方根'
print guessNum