# -*- encoding: utf-8 -*-
'''
Created on Dec 3, 2014

@author: lisong
'''
#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    x = int(number)
    res = list()
    if x % 3 == 0:
        res.append("Fizz")
        
    if x % 5 == 0:
        res.append("Buzz")
    #replace this for solution
    y = len(res)
    if y == 0:
        return str(number)
    elif y == 1:
        return res[0]
    elif y == 2:
        return "%s %s" % (res[0], res[1])


'''
参考
def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)

'''
#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
