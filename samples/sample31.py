# -*- coding: utf-8 -*-
#寻找能开立方的数
x = int(raw_input("请输入一个整数： "))
ans = 0;
while ans ** 3 < abs(x):
	ans = ans + 1
if ans ** 3 == abs(x):
	if x < 0:
		ans = -ans
	print x,'的立方根为',ans	
else :
	print x, '的立方根为不是整数！'