# -*-coding:utf-8 -*-
# 变量的作用范围
def f():
	print x
def g():
	print x
	x = 1
x = 3
f()
g() #local variable 'x' referenced before assignment
'''
def  f(x):
	def g():
		x = 'abc'
		print 'x =', x
	def h():
		z = x
		print 'z =', z
	x = x + 1
	print 'x =', x
	h()
	g()
	print 'x =', x
	return g
x = 3
z = f(x)
print 'x =', x
print 'z = ', z
z()
'''
'''
def f(x):
	y = 1
	x = x + y
	print 'x = ' , x
	return x
x = 3
y = 2
z = f(x)
print 'z =', z
print 'y =', y
print 'x =', x
'''