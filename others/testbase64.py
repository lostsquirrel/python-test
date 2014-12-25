# -*- coding: utf-8 -*-
#测试使用base64
import base64
# import urllib2


# link = "/home/lisong/Downloads/19F272ED05428A601BDA6558FA15AE53_280.jpg"
# link = "http://eee.so"
# link = "https://www.youtube.com/"
# proxyserver = "127.0.0.1:8087"
# proxy = urllib2.ProxyHandler({'https': 'https://%s/' % proxyserver})
# opener = urllib2.build_opener(proxy)
# urllib2.install_opener(opener)
# f = urllib2.urlopen(link)
# myfile = f.read()
# print myfile
# myfile = open(link).read()
# print base64.b64encode(myfile)
fl = open("cv2.txt")
content = ""
for x in fl:
    content += x

xx = base64.b64decode(content)
fx = open('w.jpg', 'w')
fx.write(xx)
fl.close()
fx.close()
print xx
print 'finished...........'