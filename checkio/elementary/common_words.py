# -*- encoding: utf-8 -*-
'''
Created on 2015-05-20

@author: lisong
'''
def checkio(first, second):
    _first = set(first.split(","))
    _second = set(second.split(","))
    cm = _first.intersection(_second);
    _cm = list(cm)
    _cm.sort(cmp=None, key=None, reverse=False)
    res = ""
    if len(_cm) > 0:
        res = ','.join(_cm)
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
    
    
'''
def checkio(first, second):
    """
    set data type has useful methods.
    """
    first_set, second_set = set(first.split(",")), set(second.split(","))
    common = first_set.intersection(second_set)
    return ",".join(sorted(common))
'''