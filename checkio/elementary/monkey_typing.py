# -*- coding:utf-8 -*-
'''
Created on 2015-03-06

@author: lisong
'''
def count_words(text, words):
    amount = 0
    for w in words:
        if w in text.lower():
            amount += 1
    return amount
''

if __name__ == '__main__':
    #These uu"1sserts" using only for self-checking and not necessary for auto-testing
    print count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"})
    assert count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"}) == 3, "Example"
    assert count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"}) == 2, "BANANAS!"
    assert count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {u"sum", u"hamlet", u"infinity", u"anything"}) == 1, "Weird text"

'''
def count_words(text, words):
    return sum(w in text.lower() for w in words)
    
'''
