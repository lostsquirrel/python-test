# -*- coding: utf-8 -*-
#面向对象示例 二

import datetime

class Person(object):
	def __init__(self, name):
		self.name = name
		try:
			lastBlank = name.rindex(' ')
			#print lastBlank
			self.lastName = name[lastBlank + 1:]
		except :
			self.lastName = name
		self.birthday = None

	def getLastName(self):
		return self.lastName

	def setBirthday(self, birthDate):
		self.birthday = birthDate

	def getAge(self):
		if self.birthday == None:
			raise ValueError
		return (datetime.date.today() - self.birthday).days

	def __lt__(self, other):
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName

	def __str__(self):
		return self.name

class MITPerson(Person):
	nextIdNum = 0	
	def __init__(self, name):
		Person.__init__(self, name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idNum

	def __lt__(self, other):
		return self.idNum < other.idNum
	def isStudent(self):
		return isinstance(self,Student)

class Student(MITPerson):
	pass

class UG(Student):
	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear
	
	def getClass(self):
		return self.year

class Grad(Student):
	pass
# mg = Person('Michael Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# print him.getLastName()
# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958,8, 16))
# print him.getAge()
# print her.getAge()


# pList = [mg, him, her]
# for x in pList:
# 	print x
# pList.sort()
# for x in pList:
# 	print x

######################################################
# p1 = MITPerson('Barbara Beaver')
# print p1,p1.getIdNum()
#########################################
p3 = MITPerson('Billy Bob Beaver')
p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
# print p5
# print type(p5)
# print type(p5) == Grad
# print type(p5) == UG
print p5.isStudent()
print p6.isStudent()
print p3.isStudent()