# -*- coding: utf-8 -*-
'''
输入一段由英语字母和标点符号组成的文本
返回文本中出现次数最多的字母，如果出现次数最多的字母有多个，返回字母顺序第一个
不计算标点符号和空格
'''

def checkio(text):
	tmp = dict()
	for letter in text:
		if letter.isalpha():
			if letter.isupper() :
				upper_count = text.count(letter)
				lower_count = text.count(letter.lower())
			else : 
				lower_count = text.count(letter)
				upper_count = text.count(letter.upper())

			key = lower_count + upper_count
			if tmp.has_key(key) :
				tmp[key].add(letter.lower())
			else :
				tmp[key] = set(letter.lower())
	# print tmp
	keys = tmp.keys();
	keys.sort()

	most = tmp[keys[len(keys) - 1]]
	# print most
	most = list(most)
	most.sort()
	return most[0]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(u"Hello World!") == "l", "Hello test"
	assert checkio(u"How do you do?") == "o", "O is most wanted"
	assert checkio(u"One") == "e", "All letter only once."


'''
import string
 
def checkio(text):
    return max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))
'''