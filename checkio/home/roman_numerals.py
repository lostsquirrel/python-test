# -*- coding: utf-8 -*-
# I 1 (unus)
# V 5 (quinque)
# X 10 (decem)
# L 50 (quinquaginta)
# C 100 (centum)
# D 500 (quingenti)
# M 1,000 (mille)

def checkio(data):
	tmp = list()
	base =  [ "","I","II","III","IV","V","VI","VII","VIII","IX"]
	if data < 4000:
		if data >= 1000:
			a = data // 1000
			tmp.append("M" * a)
			data -= 1000 * a
		if data >= 900:
			tmp.append("CM")
			data -= 900
		if data >= 500:
			tmp.append("D")
			data -= 500
		if data >= 400:
			tmp.append("CD")
			data -= 400
		if data >= 100:
			b = data // 100
			tmp.append("C" * b)
			data -= 100 * b
		if data >= 90:
			tmp.append("XC")
			data -= 90
		if data >= 50:
			tmp.append("L")
			data -= 50
		if data >= 40:
			tmp.append("XL")
			data -= 40
		if data >= 10:
			c = data // 10
			tmp.append("X" * c)
			data -= 10 * c
		if data > 0:
			tmp.append(base[data])
	print tmp
	return ''.join(tmp)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
'''
def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
    roman = ''
    romanmappings = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 
                     40: "XL", 50: "L", 90: "XC", 100: "C", 
                     400: "CD", 500: "D", 900: "CM", 1000: "M" }                     
    for intVal in sorted(romanmappings.keys(), reverse=True):
        while number >= intVal:
            roman += romanmappings[intVal]
            number -= intVal
    return roman
   '''