# -*- coding:utf-8 -*-

__author__ = 'lisong'

"""
The Hamming distance between two binary integers is the number of bit positions that differs
(read more about the Hamming distance on Wikipedia). For example:

    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3

You are given two positive numbers (N, M) in decimal form.
You should calculate the Hamming distance between these two numbers in binary form.

Input: Two arguments as integers.

Output: The Hamming distance as an integer.

Example:

checkio(117, 17) == 3
checkio(1, 2) == 2
checkio(16, 15) == 5

How it is used: This is a basis for Hamming code and other linear error-correcting programs.
The Hamming distance is used in systematics as a measure of genetic distance. On a grid (ie: a chessboard,)
the Hamming distance is the minimum number of moves it would take a rook to move from one cell to the other.

Precondition:
0 < n < 10e6
0 < m < 10e6
"""
def hamming_distance(bigger, smaller):
    distance = 0
    bigger = bin(bigger)[2:]

    smaller = bin(smaller)[2:]
    db = len(bigger)
    ds = len(smaller)
    d = db - ds
    smaller = '0' * d + smaller
    # print bigger
    # print smaller
    for x in range(len(smaller)):
        distance += (int(smaller[x]) + int(bigger[x])) % 2

    return distance

def checkio(n, m):
    res = None
    if m > n:
        res = hamming_distance(m, n)
    else:
        res = hamming_distance(n, m)

    return res

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    # print type(bin(117))
    # print bin(117)
    # print bin(117 ^ 17) 异或

'''
def checkio(n, m):
    return bin(n ^ m).count('1')
'''