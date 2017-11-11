# -*- coding:utf-8 -*-
"""
extends of unittest
"""
import unittest
import random
from docs.unittest.toy_math import divide, multiply


class BaseTestCase(unittest.TestCase):

    # def __init__(self):
    case_values = [(random.randint(-100, 100), random.randint(-1000, 1000) + x) for x in range(10)]


class DivideTestCase(BaseTestCase):

    def runTest(self):
        for x, y in self.case_values:
            if y <> 0:
                assert divide(x, y) == x / y, 'bug found in add'


class MultiplyTestCase(BaseTestCase):

    def runTest(self):
        for x, y in self.case_values:
            assert multiply(x, y) == x * y, 'bug found in multiply'


if __name__ == '__main__':

    unittest.main()