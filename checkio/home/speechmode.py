# -*- coding: utf-8 -*-
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
	res = []
	hundred_ = number / 100
	if hundred_ > 0:
		res.append(FIRST_TEN[hundred_ ])
		res.append(HUNDRED)
		number -= 100 * hundred_
	if number >= 20:
		tens = number / 10
		res.append(OTHER_TENS[tens - 2])
		number -= tens * 10
		if number > 0 :
			res.append(FIRST_TEN[number])
	elif number >= 10:
		number -= 10
		res.append(SECOND_TEN[number])
	elif number > 0 :
		res.append(FIRST_TEN[number ])
	return ' '.join(res)

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"

'''
def checkio(i):
    if i < 20:
        result = 'zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')[i]
    elif i < 100:
        result = ',,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')[i//10]
        if i % 10:
            result += ' ' + checkio(i % 10)
    elif i < 1000:
        result = checkio(i // 100) + ' hundred'
        if i % 100:
            result += ' ' + checkio(i % 100)
    return result
 '''