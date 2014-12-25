'''
Created on Sep 27, 2014

@author: lisong
'''
import xml.etree.ElementTree as ET
import requests

mindhaks = 'http://mindhacks.cn/feed/'
resp = requests.get(mindhaks)
root = ET.fromstring(resp.content)
for child in root[0].findall("item"):
    print child.attrib
if __name__ == '__main__':
    pass