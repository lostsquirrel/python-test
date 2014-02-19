'''
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z
给定一段由单词组成的文本, 单词被空格和标点分隔, 
数字包括包含数字的词不做统计, 
统计不包含两个连续元音或辅音的单词的数量
一个字母的单词不做统计
不区分大小写
'''
def is_vowel(letter) :
	letter = letter.upper()
	return 'AEIOUY'.find(letter) != -1

def is_consonant(letter):
	letter = letter.upper()
	return "BCDFGHJKLMNPQRSTVWXZ".find(letter) != -1
def split(text):
	words = list()
	word = ''
	for letter in text:
		if (letter.isalpha() or letter.isdigit()) :
			word += letter
		else:
			words.append(word)
			word = ''
	words.append(word)
	return words
def striped(word):
	last_letter = ''
	if len(word) < 2:
		return 0
	for letter in word:
		if (letter.isdigit()) :
			return 0
		elif (is_vowel(letter) and last_letter == 'is_vowel'):
			return 0
		elif (is_vowel(letter) and not last_letter == 'is_vowel') :
			last_letter = 'is_vowel'
		elif (is_consonant(letter) and last_letter == 'is_consonant'):
			return 0
		elif (is_consonant(letter) and not last_letter == 'is_consonant'):
			last_letter = 'is_consonant'
	return 1

def checkio(text):
	count = 0
	for word in split(text):
		print word
		count += striped(word)
		print striped(word)
	return count


# if __name__ == '__main__':
#     # print checkio("My name is ...")
#     # print split("My name is ...")
#     # print checkio("Hello world") 
#     print checkio("A quantity of striped words.") 
'''
import re
checkio=lambda t:sum(any(all('@'<c and j^(c in'aeiouyAEIOUY')^i&1
for i,c in enumerate(w))for j in(0,1))for w in re.findall(r"\w\w+",t))
'''