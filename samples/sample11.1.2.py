# -*- coding: utf-8 -*-
#画图表2 保存文件
import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,2,3,4])
pylab.figure(2)
pylab.plot([1,2,3,4],[5,6,7,8])
pylab.savefig('Figure-Addie')
pylab.figure(1)
pylab.plot([5,6,10,3]) #x : range(len(y-values))
pylab.savefig('Figure-Jane')