# -*- coding: utf-8 -*-
#测试使用base64
import base64
import urllib2


link = "https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt"
# link = "http://eee.so"
# link = "https://www.youtube.com/"
proxyserver = "127.0.0.1:8087"
proxy = urllib2.ProxyHandler({'https': 'https://%s/' % proxyserver})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
f = urllib2.urlopen(link)
myfile = f.read()
# print myfile
print base64.b64decode(myfile)
print 'finished...........'