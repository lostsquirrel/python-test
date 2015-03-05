# -*- coding:utf-8 -*-
'''
Created on Jan 12, 2015

@author: lisong
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

notify_connection_url = 'postgresql://postgres:sale114@db0.soulagou.com:5433/soulagou_notify'
notify_engine = create_engine(notify_connection_url, echo=False)
NotifySession = sessionmaker(bind=notify_engine)

def get_pages(total, size):
    '''
    @param:total 记录总条数，
    @param:size 每页条数
    '''
    xx = total % size
    if xx == 0:
        return total / size
    else :
        return total / size + 1
    
def find_notice(user_id, firstResult, maxResults, is_read = None):
    '''
        商家用户ID
        is_read 通知状态 None 所有状态
    '''
    cursor_notify = NotifySession()
    try:
        if is_read == None:
            sql = "SELECT * FROM notice WHERE user_id = :user_id LIMIT :maxResult OFFSET :firstResult"
            params = dict(user_id=user_id, firstResult=firstResult, maxResult=maxResults)
        else :
            sql = "SELECT * FROM notice WHERE user_id = :user_id AND is_read = :is_read limit :maxResult offset :firstResult"
            params = dict(user_id = user_id, is_read = is_read, firstResult=firstResult, maxResult=maxResults)
        rp = cursor_notify.execute(sql, params)
#         print dir(cursor_notify)sessionmaker
#         print sql
#         print params
#         return rp
        rs = rp.fetchall()
        if rs != None:
            return rs
    finally:
        cursor_notify.close()
        
def count_notice(user_id, is_read = None):
    '''
        商家用户ID
        is_read 通知状态 None 所有状态
    '''
    cursor_notify = NotifySession()
    try:
        if is_read == None:
            sql = "SELECT COUNT(id)  FROM notice WHERE user_id = :user_id"
            params = dict(user_id=user_id)
        else :
            sql = "SELECT COUNT(id)  FROM notice WHERE user_id = :user_id AND is_read = :is_read"
            params = dict(user_id = user_id, is_read = is_read)
        rp = cursor_notify.execute(sql, params)
        rs = rp.fetchone()
        return rs[0]
    finally:
        cursor_notify.close()
        
def get_notieces(user_id, page, size):
    firstResult = (page - 1) * size
    maxResults = size
    
    total = count_notice(user_id)
    
    dataList = find_notice(user_id, firstResult, maxResults)
    if dataList == None:
        return list()
    
    feilds = ('id', 'user_id', 'content', 'create_time', 'read_time', 'is_valid', 'is_read', 'typex', 'source')
    orm = dict(id = 'id', 
               user_id = 'userId', 
               content = 'content', 
               create_time = 'createTime', 
               read_time = 'readTime', 
               is_valid = 'isValid', 
               is_read = 'isRead',
               typex = 'type',
               source = 'source'
    )
    
    rList = list()
#     print type(dataList)
    for i in dataList:
        item = dict()
        print len(i)
        for x in range(len(i)):
            item[orm[feilds[x]]] = i[x]
        rList.append(item)
    
    pages = get_pages(total, size)
    da = dict(
              data = rList,
              total = total,
              size = size,
              page = page,
              pages = pages)
    jre = dict(status=True, data = da, messages = "")
    
    return jre

def test():
    cursor_notify = NotifySession()
    try:
        sql = "SELECT (id, is_valid) FROM notice WHERE user_id = :user_id LIMIT :maxResult OFFSET :firstResult"
        params = dict(user_id='88e3f40f78944dac9755948f215faa48', firstResult=0, maxResult=10)
        rp = cursor_notify.execute(sql, params)
        rs = rp.fetchall()
        print type(rp)
        print type(rs)
        print rs
       
#         if rs != None:
#             return rs
    finally:
        cursor_notify.close()
if __name__ == '__main__':
    user_id = '88e3f40f78944dac9755948f215faa48'
    print get_notieces(user_id, 1, 11)
#     test()
#     print count_notice(user_id)
#     print find_notice(user_id, 0, 10)