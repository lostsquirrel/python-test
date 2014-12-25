# -*- coding: utf-8 -*-
def to_mose(x, bit):
	x = x[2:]
	x = '0' * (bit - len(x)) + x
	res = x.replace('0', '.')
	res = res.replace('1', '-')
	return res
def checkio(data):
	res = ''
	bits = [2,4,3,4,3,4]
	index = 0
	tmp = list()
	for item in data.split(':'):
		tmp.append('0' * (2 - len(item)) + item)

	complete = ":".join(tmp)
	for letter in complete:
		if letter.isdigit():
			res += to_mose(bin(int(letter) ), bits[index]) + ' '
			index += 1
		else:
			res += letter + ' '
	return res[:-1]
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    print checkio("00:1:02")
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

'''
def checkio(data):
    ret = []
    for i, d in enumerate(data.split(':')):
        r, d = '', int(d)
        f, s = d / 10, d % 10
        if i == 0:
            r += '{0:02b} '.format(f)
        else:
            r += '{0:03b} '.format(f)
        r += '{0:04b}'.format(s)
        ret.append(r)
    ret = ' : '.join(ret)
    return ret.replace('0', '.').replace('1', '-')
    '''