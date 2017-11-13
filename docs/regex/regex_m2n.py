# -*- coding:utf-8 -*-
"""
match m to n pattern by regex
"""
import unittest
import re


class RegexMatch(unittest.TestCase):

    case_values = (['M' * i for i in range(6)],
                   )

    def testMatchM2N(self):
        """ match 0 - 3 M only"""
        pattern = '^M?M?M?$'
        pattern = '^M{0,3}$'
        for t in self.case_values[0]:
            r = re.search(pattern, t)
            i = len(t)
            if i < 4:
                assert r is not None, 'ERROR: pattern %s should match %s' % (pattern, t)
            else:
                assert r is None, 'ERROR: pattern %s should NOT match %s' % (pattern, t)

    def testMatchXorY(self):
        """
        match any of these cases:
        CM
        CD
        0 - 3 C
        D + 0 - 3 C
        :return:
        """
        sc = ('', 'MCM', 'MD', 'MMMCCC',)
        fc = ('MCMC',)
        pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
        pattern = '^M{0,3}(CM|CD|D?C{0,3})$'
        for c in sc:
            assert re.search(pattern, c) is not None, 'ERROR: pattern %s should match %s' % (pattern, c)
        for c in fc:
            assert re.search(pattern, c) is None, 'ERROR: pattern %s should NOT match %s' % (pattern, c)

