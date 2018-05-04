# -*- coding: utf-8 -*-
# 生成目录
import urllib
from BeautifulSoup import BeautifulSoup


def read_page(url):
    data = urllib.urlopen(url)
    parsed_html = BeautifulSoup(data)
    title = parsed_html.body.find('h1', attrs={'class': 'artical-title'}).text
    print('%s %s' % (title, url))
    next_page = parsed_html.body.find('a', attrs={'class': 'fr'})['href']
    return next_page


if __name__ == '__main__':
    # print(read_page('http://blog.51cto.com/cloudman/1854750'))
    url = 'http://blog.51cto.com/cloudman/1854750'
    while True:
        url = read_page(url)
        if url is None or len(url) < 4:
            break
