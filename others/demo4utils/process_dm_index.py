# -*- coding:utf-8 -*-
'''
Created on 2015-03-02

@author: lisong

not work properly
'''
import pysolr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    
    
    notify_connection_url = 'postgresql://soulagou_read:123456789@42.121.18.61:5432/soulagou_outlet_new'
    notify_engine = create_engine(notify_connection_url, echo=False)
    NotifySession = sessionmaker(bind=notify_engine)
    cursor_notify = NotifySession()
    all_results = list()
    try:
        for x in range(27):
            sql = "SELECT id FROM dm_commodity WHERE end_date > now() or is_valid = true LIMIT 1000 OFFSET :firstResults"
            params = dict(firstResults = x * 1000)
            rp = cursor_notify.execute(sql, params)
    #         print dir(cursor_notify)
    #         print sql
    #         print params
    #         return rp
            rs = rp.fetchall()
            if rs != None:
#                 print rs
                for itx in rs:
                    all_results.append(itx[0])
    finally:
        cursor_notify.close()
#     print 144764 in all_results
#     print all_results
    solr = pysolr.Solr('http://42.121.19.109:12102/solr/core2/', timeout=300)
    results = solr.search('*:*', rows=37614)
    print results.hits
    print len(results.docs)
    delete_docs = list()
    for doc in results.docs:
#         print doc
        if not (doc['id'] in all_results):
#             print doc['id']
#             solr.delete(id=doc['id'])
            delete_docs.append(doc['id'])
    while len(delete_docs) > 0:
        print len(delete_docs)
        page_size = 500
        if len(delete_docs) < 500:
            page_size = len(delete_docs)
        print page_size, ' '.join(map(str, delete_docs[:page_size]))
        solr.delete(q='id:(%s)' % ' '.join(map(str, delete_docs[:page_size])))
        delete_docs = delete_docs[page_size:]
#     solr.delete(q=' '.join(map(str, delete_docs)))
   