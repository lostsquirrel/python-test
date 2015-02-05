#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 23, 2014

@author: lisong


'''
from HTMLParser import HTMLParser
import requests;


ext_tag = ["style", "script","meta", "link", "br"]
ext_attr =["style", "class", "id"]
class ItemHTMLParser(HTMLParser):
    content = ""
    data_tag = False
    tag_stack = list()
    start = False
    finish = False
    def handle_starttag(self, tag, attrs):
#         print "Start tag:", tag
        href = ''
        for attr in attrs:
            if 'div' == tag and attr[0] == 'id' and attr[1].startswith('post-'):
                self.start = True
            if 'href' == attr[0]:
                href = attr[1]
        if (not (tag in ext_tag)) and self.start and (not self.finish):
            if 'a' ==  tag:
                
                self.content += "<%s href='%s'>" % (tag, href)
            else:
                self.content += "<%s>" % tag
            self.data_tag = True
            self.tag_stack.append(tag)
        else:
            self.data_tag = False
            
    def handle_endtag(self, tag):
#         print "End tag  :", tag
#         print self.getpos()
        if len(self.tag_stack) == 0 and self.start == True and (not self.finish):
            self.finish = True
#         print self.tag_stack
        if (not (tag in ext_tag)) and self.start and (not self.finish):
            self.content += "</%s>" % tag
            self.tag_stack.pop()
    def handle_data(self, data):
#         print "Data     :", data
        if self.data_tag and self.start and (not self.finish):
            self.content += data
class ChannelHTMLParser(HTMLParser):
    items = dict()
    b_tag = False
    def handle_starttag(self, tag, attrs):
        if 'a' == tag:
            for attr in attrs:
                if 'href' == attr[0]:
                    href = attr[1]
                    if not self.b_tag and '#' == href:
                        self.b_tag = True
                    if self.b_tag:
                        k = href[31:-1]
                        self.items[k] = href
#         print "Decl     :", data
def clip(page):
    '''
    截取博客正文
    @param page: 网页文本
    @return: 截取的正文内容
    '''
    parser = ItemHTMLParser()
    parser.feed(page)
    return parser.content

if __name__ == '__main__':
    
    root = 'http://mindhacks.cn/archives/'
    r = requests.get(root)
    content = clip(r.content)
    pr = ChannelHTMLParser()
    pr.feed(content)
    res = pr.items
    res.pop('')
    print res
    for k in res:
        u = res.get(k)
        r = requests.get(u)
#     print r.status_code
    
        content = clip(r.content)
        
        f = open('/home/lisong/aptana_work/blog_save/mindhacks/%s.html' % k, 'w')
        f.write(content)
        f.close()
  
