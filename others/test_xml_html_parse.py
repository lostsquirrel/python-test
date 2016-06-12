from HTMLParser import HTMLParser

from others.cware_package.tree_parser import convert_to_utf8


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data


parser = MyHTMLParser()
xue_xml = 'F:/package_source/TRMS0000061/XML_V1.0//GJY-T-4.xml'
parser.feed(convert_to_utf8(xue_xml))