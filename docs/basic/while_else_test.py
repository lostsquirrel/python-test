# -*- coding: utf-8 -*-
import unittest


def else_exception():
    x = 5
    while x > 0:
        if x < 3:
            raise IndexError()
        print(x)
        x -= 1
    else:
        print('else: {}'.format(x))


class WhileElseTests(unittest.TestCase):

    def test_simple(self):
        x = 5
        while x > 0:
            print(x)
            x -= 1
        else:
            print('else: {}'.format(x))

        self.assertEqual(0, x)

    def test_else_break(self):
        x = 5
        while x > 0:
            if x < 2:
                break
            print(x)
            x -= 1
        else:
            print('else: {}'.format(x))

        self.assertEqual(1, x)

    def test_else_exception(self):
        self.assertRaises(IndexError, else_exception)
