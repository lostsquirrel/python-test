# -*- coding:utf-8 -*-
'''
Created on 2015-02-04

@author: lisong
'''
order_no = '123'
print type(order_no)
message = "订单不存在(order_no:%s)" % (order_no)
print message
order_no = ''
message = '''订单不存在(order_no:%s)''' % (order_no)
print message