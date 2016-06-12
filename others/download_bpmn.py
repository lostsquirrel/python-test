# -*- coding: utf-8 -*-

import requests
from HTMLParser import HTMLParser
from Queue import Queue


class ItemHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.items = []
        self.data = None

    def handle_data(self, data):
        self.data = data

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for att in attrs:
                if att[0].lower() == 'href' and is_exclude(att[1]):
                    self.items.append(att[1])
                    # print att

    def handle_endtag(self, tag):
        if tag.lower() == 'a':
            # print self.data
            if len(self.items) > 0 and is_exclude_content(self.data):
                self.items.pop()

    def get_items(self):
        return self.items


def parse_path(path):
    uri = 'http://www.omg.org/spec/BPMN/2.0/examples/zip/'
    r = requests.get(uri + path)
    # print(r.content)
    parser = ItemHTMLParser()
    parser.feed(r.content)
    return [path + i for i in parser.get_items()]


def is_path(target):
    # print target
    return target[-1:] == '/'


def is_exclude_content(content):
    ex = [
        'Parent Directory',
        'Name',
        'Last modified',
        'Size',
        'Description',
        'www.omg.org'
    ]

    return content in ex


def is_exclude(url):
    excludes = [
        'http://www.omg.org/spec/',
        '../news/schedule/upcoming.htm',
        '../be-a-member-a.htm',
    ]
    return '_derived/' == url or url in excludes


if __name__ == '__main__':

    items = []
    q = Queue()
    q.put('')
    while q.qsize() > 0:
        x = q.get()
        tmp = parse_path(x)
        # print tmp
        for i in tmp:
            q.put(i)

        if is_path(x):
            print x
        else:
            print x


