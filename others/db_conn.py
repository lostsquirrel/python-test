#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import time

pingResultQl = "INSERT INTO ping_result(ip, ttl, time, create_time) VALUES (?, ?, ?, ?)"
serverInsertQl = "INSERT INTO server_list(area, name, ip, protocol, status, create_time) VALUES (?, ?, ?, ?, ?, ?)"
db = 'test.db'

def printVersion2():
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        
        data = cur.fetchone()
        
        print "SQLite version: %s" % data
        
def printVersion():
    con = None
    try:
        con = lite.connect('test.db')
        
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        
        data = cur.fetchone()
        
        print "SQLite version: %s" % data                
        
    except lite.Error, e:
        
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:
    
        
        if con:
            con.close()
def crateTable(db,qlString):     
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute(qlString)

        
def insert(db, qlString, data):
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute(qlString, data)

def batchInsert(db, qlString, data):
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.executemany(qlString, data)

def pingInsert(data):
    insert(db, pingResultQl, data)
    
def serverBatchInsert(data):
    batchInsert(db, serverInsertQl, data)
    
def getIps():
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("SELECT ip FROM server_list")
        return cur.fetchall()
    
def getPingbyIp(ip):
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("SELECT time FROM ping_result where ip = ? and create_time > ?", (ip, time.time() - 60 * 24 * 1000))
        return cur.fetchall()
    


if __name__ == "__main__":
    pass
#     qlString = "CREATE TABLE server_list(id INTEGER PRIMARY KEY AUTOINCREMENT, area TEXT, name TEXT, ip TEXT, protocol TEXT, create_time REAL, status INT)"
#     crateTable(db, qlString)
#     insert('220.181.111.86', 54, 39.3, time.time())    
#     print time.time()