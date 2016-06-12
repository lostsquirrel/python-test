import xml.sax
import StringIO
from xml.sax import parseString
class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""
      self.itemStack = []

   # Call when an element starts
   def startElement(self, tag, attributes):
        if 'item' == tag:
            process_item_attr(attributes, self.itemStack)
            self.itemStack.append('item')

   # Call when an elements ends
   def endElement(self, tag):
        if 'item' == tag:
            self.itemStack.pop()


   def characters(self, content):
       pass

def process_item_attr(attrs, itemStack):
    if len(attrs.getNames()) > 0:
        print len(itemStack)
        x = 'addtree(\'' + '-' * len(itemStack) +attrs.getValue('name') + '\''
        url = attrs.getValue('url')
        if len(url) > 0:
            x += ', \'resource/' + url.replace('http://192.168.0.16:8080/dmt_1400_713/CSXT/', '')
            x += '\', \'innerTarget\''
        x += ');'
        print x

if ( __name__ == "__main__"):

   xue_xml = 'G:/TRCF0000040/XML_1.0/CSXT_xue.xml'
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   h = open(xue_xml)
   content = ''

   for l in h:
       print l
       content += l.decode('gb2312').encode('utf-8').strip() + '\n'
   # print parseString(content, parser.parse)
   content = content.replace("gb2312", "utf-8")

   # print content
   hh = open('x.xml', 'w')
   hh.write(content)
   parser.parse('x.xml')
