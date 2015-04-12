# -*- encoding: utf-8 -*-
'''
Created on 2015-04-12

@author: lisong
Do you remember the radix and Numeral systems from math class? Let's practice with it.
You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.
Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.
Input: Two arguments. A number as string and a radix as an integer.
Output: The converted number as an integer.
Precondition: 
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36
'''
radix_all = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 
             'G', 'H', 'I', 'J', 'K', 'L', 
             'M', 'N', 'O', 'P', 'Q', 'R', 
             'S', 'T', 'U', 'V', 'W', 'X', 
             'Y', 'Z',
             )
def checkio(str_number, radix):
    r = len(str_number)
    count = 0;
    res = 0
    r -= 1;
    while(r >= 0):
        x = str_number[r]
        if not x in radix_all[:radix]:
            res = -1
            break;
        res += radix_all.index(x) * radix** count
#         print radix_all.index(x), count
        r -= 1
        count += 1
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(u"AF", 16)
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
''' python3
def checkio(*a):
    try: return int(*a)
    except ValueError: return -1
'''