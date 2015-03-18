'''
Created on Feb 8, 2015

@author: lisong
'''
def unicode2chines(source):
    print source.decode('unicode-escape')
    
if __name__ == '__main__':
    content = open('unicode_content.txt', 'r').read()
    unicode2chines(content)