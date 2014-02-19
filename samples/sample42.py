# -*-coding:utf-8 -*-
# 求一个数的平方根的方法,包含文档注释和测试
def findRoot(x, power, epsilon):
	"""
	x可以为整数或小数
	power 为整数且大于等于1
	epsilon 需大于0
	返回值y满足 y ** power - x < epsilon
	如果没有找到满足条件的值 则返回None
	"""
	if x < 0 and power % 2 == 0:
		return None
	low = min(-1.0, x)
	high = max(1.0, x)
	ans = (low + high) / 2.0
	while abs(ans ** power - x) >= epsilon:
		if ans ** power < x:
			low = ans
		else:
			high = ans
		ans = (low + high) / 2.0
	return ans

def testFindRoot():
	epsilon = 0.0001
	for x in (0.25, -0.25, 2, -2, 8, -8):
		for power in range(1,4):
			print 'Testing x = ' + str(x) + \
				' and power = ' + str(power)
			res = findRoot(x, power, epsilon)
			if res == None:
				print '  No root'
			else :
				print '  ' + str(res ** power) + '~=' + str(x)