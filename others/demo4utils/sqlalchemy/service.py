# -*- coding: utf-8-*-
'''
Created on 2014-5-23

@author: zhuhua
'''
from application import Session
from models import Job
from datetime import datetime

def create(name, url):
    '''新增'''
    job = Job()
    job.name = name
    job.url = url
    job.create_time = datetime.now()
    
    session = Session()
    session.add(job)
    session.commit()
    session.close()
    
def update(job_id, name, url):
    '''修改'''
    session = Session()
    job = session.query(Job).get(job_id)
    job.name = name
    job.url = url
    session.commit()
    session.close()
    
def delete(job_id):
    '''删除'''
    session = Session()
    session.query(Job).filter(Job.id == job_id).delete()
    session.commit()
    session.close()
    
def read(job_id):
    '''读取'''
    session = Session()
    job = session.query(Job).get(job_id)
    session.close()
    return job
    
def get_list():
    '''列表'''
    session = Session()
    jobs = session.query(Job).order_by(Job.create_time.desc()).all()
    session.close()
    return jobs