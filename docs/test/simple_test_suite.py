# -*- coding:utf-8 -*-
"""
basic of test suite
"""
import unittest
from docs.test.simple_test_case import AddTestCase
from docs.test.abstract_test_case import MultiplyTestCase, DivideTestCase
from docs.test.named_test_case import MinusTestCase

if __name__ == '__main__':
    toy_test_suit= unittest.TestSuite()
    toy_test_suit.addTest(AddTestCase())
    toy_test_suit.addTest(MinusTestCase('testMinus'))
    toy_test_suit.addTest(MultiplyTestCase())
    toy_test_suit.addTest(DivideTestCase())

    unittest.main()