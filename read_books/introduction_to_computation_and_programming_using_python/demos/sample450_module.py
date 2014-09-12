# -*- coding: utf-8 -*-
#模块与引入，模块部分
pi = 3.14159

def area(radius):
	"""radius 半径，返回圆面积"""
	return pi * (radius * radius)

def circumference(radius):
	"""radius 半径，返回圆周长"""
	return 2 * pi * radius

def sphereSurface(radius):
	"""radius 半径，返回圆球体表面积"""
	return 4.0 * area(radius)
	
def sphereVolume(radius):
	"""radius 半径，返回圆球体体积"""
	return (4.0 / 3.0) * pi *(radius ** 3)

