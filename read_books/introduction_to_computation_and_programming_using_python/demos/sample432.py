# -*- coding: utf-8 -*-
#判断字符串是否为回文（分治）divide-and-conquer
#字母回文，非单词回文
def isPalindrome(s):
	"""s 为字符串，会忽略标点，空格和大小写"""
	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in "abcdefghijklmnopqrstuvwxyz":
				ans += c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else :
			return s[0] == s[-1] and isPal(s[1:-1])
	return isPal(toChars(s))

print isPalindrome("Dollars make men covetous, then covetous men make dollars")
print isPalindrome("dsafl;jdsalkfjlsakdjflksd")
print isPalindrome("deed")
print isPalindrome("c")
print isPalindrome("")