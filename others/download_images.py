import urllib2

images = [
'http://s9tu.com/images/2017/10/05/02d35f9.jpg',
'http://s9tu.com/images/2017/10/05/035ac00.jpg',
'http://s9tu.com/images/2017/10/05/048da8b.jpg',
'http://s9tu.com/images/2017/10/05/058332d.jpg',
'http://s9tu.com/images/2017/10/05/0609519.jpg',
'http://s9tu.com/images/2017/10/05/07616bb.jpg',
'http://s9tu.com/images/2017/10/05/085654a.jpg',
'http://s9tu.com/images/2017/10/05/0925f68.jpg',
'http://s9tu.com/images/2017/10/05/10128b1.jpg',
'http://s9tu.com/images/2017/10/05/11fe112.jpg',
'http://s9tu.com/images/2017/10/05/1280b51.jpg',
'http://s9tu.com/images/2017/10/05/13d757b.jpg',
'http://s9tu.com/images/2017/10/05/14c11ec.jpg',
'http://s9tu.com/images/2017/10/05/15e095d.jpg',
'http://s9tu.com/images/2017/10/05/1608f95.jpg',
'http://s9tu.com/images/2017/10/05/177f4a7.jpg',
'http://s9tu.com/images/2017/10/05/184e10b.jpg',
'http://s9tu.com/images/2017/10/05/19a0476.jpg',
'http://s9tu.com/images/2017/10/05/203109a.jpg',
'http://s9tu.com/images/2017/10/05/21e0563.jpg',
'http://s9tu.com/images/2017/10/05/22b2e5a.jpg',
'http://s9tu.com/images/2017/10/05/23d769b.jpg',
'http://s9tu.com/images/2017/10/05/24d5d3c.jpg',
]
if __name__ == '__main__':
    for image in images:
        # fh = open(image)
        name = image.split('/')[-1]
        s = open('C:\\Users\\lisong\\Downloads\\abc\\%s' % name, 'wb')
        req = urllib2.Request(image, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        s.write(con.read())
        s.close()
        print name


