# -*- coding: utf-8 -*-
#输入一个整数x，列出所有 满足 root ** pwr = x 的 root,pwr  0 < pwr < 6 
x = int(raw_input("请输入一个整数： "))

root = 2
while root <= x:	
	pwr = 1
	while pwr < 6:
		#print 	root ** pwr, x
		if (root ** pwr) == x:
			print 'root:',root, ' pwr:',pwr
		#print root, pwr, 'inner'
		pwr = pwr + 1
	root = root + 1
	#print root,pwr, 'outer'
print 'check finished!'