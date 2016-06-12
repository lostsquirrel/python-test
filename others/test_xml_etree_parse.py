import xml.etree.ElementTree as ET


def process_item(item):
    print item.tag
    print len([i for i in item.iter()])
    # if len([i for i in item.iter()]) > 0:
    #     process_item(item)
def process_item_attr(attrs):
    x = 'addtree(\'' + attrs['name'] + '\''
    if len(attrs['url']) > 0:
        x += ', \'resource/' + attrs['url'].replace('http://192.168.0.16:8080/dmt_1400_713/CSXT/', '')
        x += '\', \'innerTarget\''
    x += ');'
    print x
xue_xml = 'F:/package_source/TRMS0000061/XML_V1.0//GJY-T-4.xml'

xmlp = ET.XMLParser(encoding="utf-8")
f = ET.parse(xue_xml, parser=xmlp)
item = f.findall('resourceTree')[0]
itema =  item.findall('./item')
# for i in item.iter('item'):
#     attrs = i.attrib
#     process_item_attr(attrs)



