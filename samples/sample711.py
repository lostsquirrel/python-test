# -*- coding: utf-8 -*-
#异常处理示例2: 打印输入整数的平方

flag = None
while flag != 'quit':
	val = raw_input("请输入一个整数： ")
	flag = val
	try:
		val = int(val)
		print val,'的平方是', val**2
	except ValueError:
		print val, '不是整数'