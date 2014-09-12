# -*- coding: utf-8 -*-
#随机数
import random
def rollDie():
	return random.choice([1,2,3,4,5,6])

def rollN(n):
	result = ''
	for i in range(n):
		result += str(rollDie())

	print(result)

rollN(10)