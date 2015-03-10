# -*- coding:utf-8 -*-
'''
Created on 2015-03-10

@author: lisong
For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
    
1
2
3
4
5
6
How it is used: Here you can learn about iterating through set type and string data type functions.

Precondition: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)
'''
def checkio(words_set):
    res = False
    amount = len(words_set)
    words = list(words_set)
    for x in range(0, amount):
        for y in range(x + 1, amount):
            xw = words[x].lower()
            yw = words[y].lower()
            if xw.endswith(yw) or yw.endswith(xw):
                res = True
                break
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
    
    '''
    def checkio(words):
    """
    You can iterate throught set.
    """
    for w1 in words:
        for w2 in words:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False
    '''