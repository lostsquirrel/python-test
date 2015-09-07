# -*- coding: utf-8-*-
'''
Created on 2014-5-23

@author: zhuhua
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, DateTime

Base = declarative_base()

class Job(Base):
    ''' JOB'''
    __tablename__ = 'job'
    
    id = Column(Integer, name='id', nullable=False, primary_key=True)
    name = Column(String(255), name='name', nullable=False)
    url = Column(String(255), name='url', nullable=False)
    create_time = Column(DateTime, name='create_time', nullable=False)
    
from application import engine
Base.metadata.create_all(engine)