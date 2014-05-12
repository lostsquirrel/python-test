# -*- coding: utf-8 -*-
#面向对象示例 三 封装
from sample811 import Student
from sample811 import UG
from sample811 import Grad
class Grades(object):

	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True

	def addStudent(self, student):
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False

	def addGrade(self, student, grade):
		try:
			self.grades[student.getIdNum()].append(grade)
		except :
			raise ValueError('Student not in Mapping ')

	def getGrades(self, student):
		try:
			return self.grades[student.getIdNum()][:]
		except :
			raise ValueError('Student not in Mapping ')

	def allStudents(self):
		if not self.isSorted:
			self.students.sort()
		for s in self.students:
			yield s
	def gradeReport(course):
		report = ''
		for s in course.allStudents():
			tot = 0.0
			numGrades = 0
			for g in course.getGrades(s):
				toto += g
				numGrades += 1
			try:
				average = tot / numGrades
				report = report +'\n' + str(s) + ':' + str(average) 
			except ZeroDivisionError:
				report = report + '\n' + str(s) + 'has no grades'
		return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Buckner F. Dent')

sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
# for s in sixHundred.allStudents():
# 	sixHundred.addGrade(s, 75)

# sixHundred.addGrade(g1, 25)
# sixHundred.addGrade(g2, 100)
# sixHundred.addStudent(ug3)
# print gradeReport(sixHundred)

gen = sixHundred.allStudents()
print gen
print gen.next()
print gen.next()
print gen.next()