# -*- coding:utf-8 -*-
"""
basic of unittest
"""
import unittest
from docs.unittest.toy_math import add


class AddTestCase(unittest.TestCase):

    def runTest(self):
        a = 11
        b = 22
        assert add(a, b) == a + b, 'add bug found'


if __name__ == '__main__':
    unittest.main()