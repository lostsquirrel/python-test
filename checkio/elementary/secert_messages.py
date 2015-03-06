# -*- coding:utf-8 -*-
'''
Created on 2015-03-06

@author: lisong
'''
def find_message(text):
    """Find a secret message"""
    message = ""
    for c in text:
        if c.isupper():
            message += c
    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    
    
'''
find_message = lambda text: ''.join(filter(str.isupper, text))
'''