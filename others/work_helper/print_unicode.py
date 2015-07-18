'''
Created on Feb 8, 2015

@author: lisong
'''
def unicode2chines(source):
    print source.decode('unicode-escape')
    
if __name__ == '__main__':
    content = '''
    \u8ba2\u5355\u4e0d\u5b58\u5728(trade_no:1431525873385488)
    '''
    unicode2chines(content)