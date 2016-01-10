__author__ = 'lisong'

def get_greatest_common_divisor(a, b):
    if a == b :
        return b
    x = a % b
    a = b
    b = x
    if b == 0:
        return a
    else:
        return get_greatest_common_divisor(a, b)




print get_greatest_common_divisor(6, 9)
print get_greatest_common_divisor(727, 30)