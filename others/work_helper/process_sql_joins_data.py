# -*- coding:utf-8 -*-
'''
Created on 2015-02-06

@author: lisong
'''

def camel2under_score(source):
    if 'ID' in source and source.index('ID') > 0:
        source = source.replace('ID', '_id')
    for i in range(len(source)):
        e = source[i]
        if i > 0 and e.isupper():
            source = source.replace(e, '_' + e.lower())
    return source.lower()

def bath_replace(content, process_fields):
    for f in process_fields:
        content = content.replace(f, camel2under_score(f))
    return content
   
def process(file_path, process_fields):
    fh = open(file_path)
    content = bath_replace(fh.read(), process_fields)
    
    for x in content.split('\n'):
        x = x.strip()
        if 'INSERT' in x:
            x = x[:-3] + x[-1:]
        print x
        
if __name__ == '__main__':
    file_path = "test_joins_0.data"
    process_fields = ('Employees', 'EmployeeID','LastName','FirstName','BirthDate','Photo','Notes')
    file_path = "test_joins_1.data"
    process_fields = ('OrderDetails', 'OrderDetailID', 'OrderID', 'ProductID', 'Quantity')
    file_path = "test_joins_2.data"
    process_fields = ('Orders', 'OrderID', 'CustomerID', 'EmployeeID', 'OrderDate', 'ShipperID')
    file_path = "test_joins_3.data"
    process_fields = ('Products' , 'ProductID', 'ProductName', 'SupplierID', 'CategoryID', 'Unit', 'Price')
    file_path = "test_joins_4.data"
    process_fields = ('Shippers', 'ShipperID', 'ShipperName', 'Phone')
    file_path = "test_joins_5.data"
    process_fields = ('Suppliers', 'SupplierID', 'SupplierName', 'contact_name', 'address', 'city', 'postal_code', 'country', 'Phone')
#     for f in process_fields:
#         print camel2under_score(f)
    process(file_path, process_fields)
#     print camel2under_score('EmployeeID')
