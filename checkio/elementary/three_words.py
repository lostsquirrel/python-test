# -*- coding:utf-8 -*-
'''
Created on 2015-03-06

@author: lisong
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. You should check if the string contains three words in succession.
 For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
Precondition: The input contains words and/or numbers. 
There are no mixed words (letters and digits combined).
0 < len(words) < 100

'''
def checkio(words):
    amount = 0
    for w in words.split(' '):
        if amount >= 3:
            break;
        if w.isalpha():
            amount += 1
        else:
            amount = 0
    return amount >= 3

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
    
    
'''
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
    
'''