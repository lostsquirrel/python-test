import unittest

from docs.test.toy_math import divide


class MyTestCase(unittest.TestCase):
    def test_exception(self):
        def ex():
            divide(1, 0)

        self.assertRaises(ZeroDivisionError, ex)


if __name__ == '__main__':
    unittest.main()
