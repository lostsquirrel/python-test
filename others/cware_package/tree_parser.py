# encoding: utf-8
from xml.dom import minidom


def process_item(res_context,item, x, ss):
    nodes = item.childNodes
    x += 1
    if len(nodes) > 0:
        # print nodes
        for node in nodes:
            if node.nodeName == 'item' and node.attributes['name'] is not None:
                cc = process_item_attr(res_context, node.attributes['name'].nodeValue, node.attributes['url'].nodeValue, x)
                ss.append(cc)
                process_item(res_context, node, x, ss)
    x -= 1


def process_item_attr(res_context, name, url, n):
    x = 'addtree(\'' + '-' * n + name + '\''
    url = url[url.find(res_context) + len(res_context):]
    print url
    ux = url.split('/')
    if len(ux) > 1 and ux[1] == u'resource':
        url = url.replace(u'resource', u'resources')
    if len(url) > 0:
        x += ', \'resource' + url
        x += '\', \'innerTarget\''
    x += ');\n'
    return x


def convert_to_utf8(xml_file):
    h = open(xml_file)
    content = ''

    for l in h:
        content += l.decode('gb2312').encode('utf-8').strip() + '\n'
    # print parseString(content, parser.parse)
    content = content.replace("gb2312", "utf-8")

    return content


class Container(object):

    def __init__(self):
        self.content = ''

    def content(self):
        return self.content

    def append(self, cc):
        self.content += cc


def parse_tree(res_context, xml_path):
    doc = minidom.parseString(convert_to_utf8(xml_path.decode('utf-8').encode('gbk')))
    item = doc.getElementsByTagName("resourceTree")[0]
    x = 0
    # print type(Container)
    ss = Container()
    process_item(res_context, item, x, ss)
    return ss.content


if __name__ == '__main__':
    xue_xml = 'F:\\package_source\\TRSS0000010\\XML_1.0/EI32-JD型计算机联锁_xue.xml'
    print parse_tree('Gt_WJLS', xue_xml)
