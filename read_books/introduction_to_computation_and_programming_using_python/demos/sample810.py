# -*- coding: utf-8 -*-
#面向对象示例
class intSet(object):
	"""docstring for intSet"""
	def __init__(self):
		self.vals = []

	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)

	def member(self, e):
		return e in self.vals

	def remove(self, e):
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + 'not found')

	def __str__(self):
		self.vals.sort()
		result = ''
		for e in self.vals:
			result += (str(e) + ',')
		return '{' + result[:-1] + '}'
