# -*- coding:utf-8 -*-
"""
string replace by regex
"""
import unittest
import re


class AddressReplaceTest(unittest.TestCase):

    def testStringReplace(self):
        s = '100 NORTH MAIN ROAD'
        t = '100 NORTH MAIN RD.'
        self.processor(lambda : s.replace('ROAD', 'RD.'), t)

    def processor(self, worker, t):
        r = worker()
        assert r == t, 'expected: %s, but get: %s' % (t, r)

    def testStringReplaceTrick(self):
        s = '100 NORTH BROAD ROAD'
        t = '100 NORTH BROAD RD.'
        # r = s.replace('ROAD', 'RD.')
        self.processor(lambda: s[:-4] + s[-4:].replace('ROAD', 'RD.'), t)

    def testRegexTail(self):
        s = '100 NORTH BROAD ROAD'
        t = '100 NORTH BROAD RD.'
        self.processor(lambda : re.sub('ROAD$', 'RD.', s), t)

    def testRegexWholeWordTail(self):
        s = '100 BROAD'
        t = '100 BROAD'
        # worker = lambda: re.sub('ROAD$', 'RD.', s)
        worker = lambda: re.sub('\\bROAD$', 'RD.', s)
        self.processor(worker, t)

    def testRegexWholeWordTailWithR(self):
        s = '100 BROAD'
        t = '100 BROAD'
        worker = lambda :re.sub(r'\bROAD$', 'RD.', s)
        self.processor(worker, t)

    def testRegexWholeWorldNotTailWithR(self):
        s = '100 BROAD ROAD APT.3'
        t = '100 BROAD RD. APT.3'
        worker = lambda : re.sub(r'\bROAD\b', 'RD.', s)
        self.processor(worker, t)
