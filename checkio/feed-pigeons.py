# -*- coding: utf-8 -*-
#一开始有1只例子 一分钟之后来两只， 再一分钟后来三只.......四只，
#一份食物够一只鸽子吃一分钟， 如果食物足，则先到先吃
#鸽子永远吃不饱
#鸽子最少吃到一份食物，最多能喂多少只鸽子

def checkio(number):
	p = 1
	t = 1
	tmp = 0
	while number > 0:
		
		t = t + 1
		p = getP(t)
		number = number - p
		#print t
		#print p
		#print '--------'
		if number <= 0:
			# print p + number
			if (p + number < getP(t-1)):
				return getP(t-1)
			else:
				return p + number
	return 0

def getP(t):
	p  = 0
	for x in range(0,t):
		p = p + x
	return p
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print checkio(1)
	print checkio(2)
	print checkio(3)
	print checkio(4)
	print checkio(5)
	print checkio(10)
	# for x in xrange(1,10):
		# print checkio(x)

