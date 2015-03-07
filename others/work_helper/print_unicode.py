'''
Created on Feb 8, 2015

@author: lisong
'''
def unicode2chines(source):
    print source.decode('unicode-escape')
    
if __name__ == '__main__':
    content = '\u624b\u673a\u53f7\u4e0d\u5b58\u5728'
    unicode2chines(content)