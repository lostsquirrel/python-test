# -*- coding: utf-8 -*-
#检查一个字符串是否包含另一个
def  isIn(str1, str2):
	if str1 in str2:
		return True
	elif str2 in str1:
		return True
	else :
		return False