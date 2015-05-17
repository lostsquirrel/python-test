# -*- coding: utf-8 -*-
'''
U+2119:   DOUBLE-STRUCK CAPITAL P
U+01B4:   LATIN SMALL LETTER Y WITH HOOK
U+2602:   UMBRELLA
U+210C:   BLACK-LETTER CAPITAL H
U+00F8:   LATIN SMALL LETTER O WITH STROKE
U+1F24:   GREEK SMALL LETTER ETA WITH PSILI AND OXIA
'''
import sys
just_width = 60
print '=' * (just_width + 20)
print 'sys.getdefaultencoding()'.ljust(just_width),sys.getdefaultencoding()



print '=' * (just_width + 20)
my_string = "Hello World"
print "type(my_string)".ljust(just_width),type(my_string)


print '=' * (just_width + 20)
my_unicode = u"Hi \u2119\u01b4\u2602\u210c\xf8\u1f24"
print "len(my_unicode)".ljust(just_width), len(my_unicode)
print "type(my_unicode)".ljust(just_width), type(my_unicode)
print 'my_unicode.encode("ascii", "replace")'.ljust(just_width), my_unicode.encode("ascii", "replace")
print 'my_unicode.encode("ascii", "xmlcharrefreplace")'.ljust(just_width), my_unicode.encode("ascii", "xmlcharrefreplace")
print 'my_unicode.encode("ascii", "ignore")'.ljust(just_width), my_unicode.encode("ascii", "ignore")


print '=' * (just_width + 20)
my_utf8 = my_unicode.encode('utf-8')
print "len(my_utf8)".ljust(just_width), len(my_utf8)
print 'my_utf8'.ljust(just_width), my_utf8
print 'my_utf8.decode(utf-8)'.ljust(just_width), my_utf8.decode('utf-8')
print 'my_utf8.decode("ascii", "ignore")'.ljust(just_width), my_utf8.decode("ascii", "ignore")
print 'my_utf8.decode("ascii", "replace")'.ljust(just_width), my_utf8.decode("ascii", "replace")

print '=' * (just_width + 20)
my_x = "\x78\x9a\xbc\xde\xf0"
print 'my_x'.ljust(just_width), my_x
# print my_x.decode("utf-8")
# UnicodeDecodeError: 'utf8' codec can't decode byte 0x9a in position 1: invalid start byte

# print my_unicode.encode()
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 3-8: ordinal not in range(128)

print '=' * (just_width + 20)
p = u"\u2119 \u01B4 \u2602 \u210C \u00F8 \u1F24"
print p
currency = u"€"
# print hex(currency)
print ord(currency)
print currency

print '=' * (just_width + 20)
#连接字符串
print u"Hello " + "world"
print u"Hello " + ("world".decode("ascii"))
# print u"Hello " + my_utf8
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 3: ordinal not in range(128)
# print u"Hello " + (my_utf8.decode("ascii"))
print "Title: %s" % my_unicode
print my_unicode
# print my_utf8.encode('utf-8') #UnicodeDecodeError
print my_string.encode('utf-8')

print u'\u2603 SNOWMAN ' 
print u'\u2620 SKULL AND CROSSBONES ' 
print u'\u1F30E EARTH GLOBE AMERICAS ' 
print u'\u1F30F EARTH GLOBE ASIA-AUSTRALIA ' 
print u'\u1F40D SNAKE ' 
print u'\u1F41D HONEYBEE ' 
print u'\u1F426 BIRD ' 
print u'\u1F44C OK HAND SIGN ' 
print u'\u1F44D THUMBS UP SIGN ' 
print u'\u1F47D EXTRATERRESTRIAL ALIEN ' 
print u'\u1F4A5 COLLISION SYMBOL ' 
print u'\u1F4A9 PILE OF POO ' 
print u'\u1F601 GRINNING FACE WITH SMILING EYES ' 
print u'\u1F60E SMILING FACE WITH SUNGLASSES ' 
print u'\u1F61E DISAPPOINTED FACE ' 
print u'\u1F620 ANGRY FACE ' 
print u'\u1F648 SEE-NO-EVIL MONKEY ' 
print u'\u1F649 HEAR-NO-EVIL MONKEY ' 
print u'\u1F64A SPEAK-NO-EVIL MONKEY'