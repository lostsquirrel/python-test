'''
Created on Dec 4, 2014

@author: lisong
'''
'''
import sqlite3

def getData():
	fh = open('/home/lisong/size2.txt')
	rows = list()
	for l in fh:
		head = l[:9]
		if 'M' in head:
			s = l.index("M")
			x = float(l[:s])
			if x > 100:
				rows.append([x,l[s + 1:].strip()])
		if 'G' in head:
			s = l.index("G")
			x = float(l[:s]) * 1024
			rows.append([x,l[s+1:].strip()])
			
	return rows

def save(data):
	try:
		con = sqlite3.connect('size.db')
		cur = con.cursor()    
		cur.executemany("INSERT INTO folder_size(size, path) VALUES (?, ?)", data)
		con.commit()
	except Exception, e:
		print 'save Error' + e
	finally:
		con.close()
		
def find_all():
	try:
		con = sqlite3.connect('size.db')
		cur = con.cursor()    
		cur.execute("SELECT * FROM folder_size ORDER BY size DESC")
		return cur.fetchall()
	except Exception, e:
		print 'find Error' + e
	finally:
		con.close()

def clear_all():
	try:
		con = sqlite3.connect('size.db')
		cur = con.cursor()    
		cur.execute("DELETE FROM folder_size")
		con.commit()
	except Exception, e:
		print 'delete Error' + e
	finally:
		con.close()
		
def show(data):
	for x in data:
		size = x[1]
		path = x[2]
		if not '/data' in path:
			continue
		if size > 1024:
			size = "%s%s" % (size / 1024, 'G')
		else:
			size = "%s%s" % (size, 'M')
		print "%s\t%s" % (size, path)
		
def test():
	try:
		con = sqlite3.connect('size.db')
		cur = con.cursor()    
		cur.execute('SELECT SQLITE_VERSION()')
		data = cur.fetchone()

		print "SQLite version: %s" % data
	finally:
		con.close()
		
		
if __name__ == "__main__":
# 	clear_all()
# 	data = getData()
# 	save(data)
	d = find_all()
	show(d)
	test()
	'''