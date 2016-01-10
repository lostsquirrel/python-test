__author__ = 'lisong'
from HTMLParser import HTMLParser
import requests;


# print(content)


class ItemHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if 'a' == tag:
            print(attrs[0][1])


def get_code_list():
    root = 'http://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/'
    r = requests.get(root)
    content = r.content
    pr = ItemHTMLParser()
    pr.feed(content)


def get_code_item():
    root = 'http://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/avl/avl.h.htm'
    r = requests.get(root)
    content = r.content
    content = content.decode('gbk')
    print(content)

get_code_item()