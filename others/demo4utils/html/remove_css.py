# -*- coding:utf-8 -*-
'''
Created on 2015-02-12

@author: lisong
'''
from HTMLParser import HTMLParser

def read_content_from_file(file_path):
    fh = open(file_path)
    
    content = fh.read()
    fh.close()
    return content

class MyHTMLParser(HTMLParser):
    content = ""
    items = dict()
    b_tag = False
    def handle_starttag(self, tag, attrs):
#         attrs.pop('style')
        self.content += '<%s' % (tag)
        for x in attrs:
            if x[0] != 'style':
                self.content += ' %s="%s" ' % x
        self.content += '>'
    def handle_endtag(self, tag):
        self.content += '</%s>' % (tag)
    def handle_data(self, data):
        self.content += data
        
if __name__ == '__main__':
    file_path = '/home/lisong/KuaiPan/share/bobom.html'
    content = read_content_from_file(file_path)
    pr = MyHTMLParser()
    pr.feed(content)
    res = pr.items
    print pr.content