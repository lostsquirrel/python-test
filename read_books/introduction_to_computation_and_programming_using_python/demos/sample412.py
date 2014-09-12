# -*-coding:utf-8 -*-
# 参数默认值
def printName(firstName, lastName, reverse=False):
	if reverse:
		print lastName + ' , ' + firstName
	else :
		print firstName, lastName
