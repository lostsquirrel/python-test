# -*- coding:utf-8 -*-

"""
test python multiply inherit
"""


class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def foo(self):
        print(self.a, self.b)


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def foo(self):
        print('a = %s, b = %s' % (self.a, self.b))


class C(A, B):

    def foox(self):
        print('{a: %s, b: %s}' % (self.a, self.b))


if __name__ == '__main__':
    aa = '123'
    bb = '789'
    x = A(aa, bb)
    x.foo()
    y = B(aa, bb)
    y.foo()
    z = C(aa, bb)
    z.foo()
