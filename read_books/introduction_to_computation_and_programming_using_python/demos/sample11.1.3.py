# -*- coding: utf-8 -*-
#画图表2 曲线
import pylab

principal = 10000 
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
	values.append(principal)
	principal += principal*interestRate
# pylab.plot(values)
# pylab.plot(values, 'ro')
# pylab.plot(values, linewidth = 30)

pylab.rcParams['lines.linewidth'] = 6
pylab.rcParams['axes.titlesize'] = 20
pylab.rcParams['axes.labelsize'] = 18
pylab.rcParams['xtick.major.size'] = 5
pylab.rcParams['ytick.major.size'] = 5


pylab.plot(values)

pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of principal ($)')
pylab.show()