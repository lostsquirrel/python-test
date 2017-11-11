# -*- coding:utf-8 -*-
"""
name test method other than runTest of unittest
"""


import unittest
from docs.unittest.toy_math import minus

class MinusTestCase(unittest.TestCase):

    def testMinus(self):
        a = 11
        b = 22
        assert minus(a, b) == a - b, 'add bug found'

if __name__ == '__main__':
    unittest.main()