# -*- coding: utf-8 -*-
#文件读写

def testWrite():
	#新建一个文件，并要求写入两个名字，
	nameHandle = open('kids','w')

	for i in xrange(2):
		name = raw_input("请输入姓名： ")
		nameHandle.write(name + "\n")

	nameHandle.close()

def testRead():
	#迭代文件中的所有内容
	nameHandle = open('kids', 'r')
	for line in nameHandle:
		print line
	nameHandle.close()

def testRead2():
	#迭代文件中的所有内容，并在打印时移除行尾的换行
	nameHandle = open('kids', 'r')
	for line in nameHandle:
		print line[:-1]
	nameHandle.close()

def testAppending():
	nameHandle = open('kids', 'a')
	nameHandle.write('王五\n')
	nameHandle.write('赵六\n')
	nameHandle.close()
	testRead2()

def testAllReads():
	nameHandle = open('kids', 'r')
	print 'read()'
	print nameHandle.read()
	nameHandle.reload()
	print 'readline() 1'
	print nameHandle.readline()
	print 'readline() 2'
	print nameHandle.readline()
	nameHandle.reload()
	print 'readlines()'
	print nameHandle.readlines()
	nameHandle.close()

#testWrite()
#testRead()
#testRead2()
#testAppending()
testAllReads()