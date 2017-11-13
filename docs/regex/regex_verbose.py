# -*- coding:utf-8 -*-
"""
verbose regex, so you case recognize it after 6 months
"""
import re


class Rome:

    def __init__(self):
        self.pattern = '''
        ^ # beginning of string
        M{0,3} # thousands - 0 to 3 M's
        (CM|CD|D?C{0,3}) # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
        # or 500-800 (D, followed by 0 to 3 C's)
        (XC|XL|L?X{0,3}) # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
        # or 50-80 (L, followed by 0 to 3 X's)
        (IX|IV|V?I{0,3}) # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
        # or 5-8 (V, followed by 0 to 3 I's)
        $ # end of string
        '''

    def isRome(self, source):
        return re.search(self.pattern, source, re.VERBOSE) is not None

if __name__ == '__main__':
    ro = Rome()
    print ro.isRome('MCMLXXXIX')