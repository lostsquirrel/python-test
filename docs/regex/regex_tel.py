# -*- coding:utf-8 -*-
"""
match any of following case:
• 800-555-1212
• 800 555 1212
• 800.555.1212
• (800) 555-1212
• 1-800-555-1212
• 800-555-1212-1234
• 800-555-1212x1234
• 800-555-1212 ext. 1234
• work 1-(800) 555.1212 #1234

区号是 800，干线号是 555
电话号的其他数字为 1212
分机号为 1234
"""
import re
import unittest


class TelMatch:

    def __init__(self, pattern):
        self.pp = re.compile(pattern)

    def match(self, tel):
        return self.pp.search(tel)


class TelMatchTest(unittest.TestCase):

    def test_handle_dash_separator(self):
        matcher = TelMatch(r'^(\d{3})-(\d{3})-(\d{4})$')
        assert ('800', '555', '1212') == matcher.match('800-555-1212').groups()
        assert matcher.match('800-555-1212-1234') is None

    def test_handle_ext(self):
        matcher = TelMatch(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
        assert ('800', '555', '1212', '1234') == matcher.match('800-555-1212-1234').groups()
        assert matcher.match('800 555 1212 1234') is None
        assert matcher.match('800-555-1212') is None

    def test_handle_separator(self):
        matcher = TelMatch(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
        assert ('800', '555', '1212', '1234') == matcher.match('800 555 1212 1234').groups()
        assert ('800', '555', '1212', '1234') == matcher.match('800-555-1212-1234').groups()
        assert matcher.match('80055512121234') is None
        assert matcher.match('800-555-1212') is None

    def test_handle_none_separator_or_ext(self):
        matcher = TelMatch(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        assert ('800', '555', '1212', '1234') == matcher.match('80055512121234').groups()
        assert ('800', '555', '1212', '1234') == matcher.match('800.555.1212 x1234').groups()
        assert ('800', '555', '1212', '') == matcher.match('800-555-1212').groups()
        assert matcher.match('(800)5551212 x1234') is None

    def test_handle_head_chars(self):
        matcher = TelMatch(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        assert ('800', '555', '1212', '1234') == matcher.match('(800)5551212 x1234').groups()
        assert ('800', '555', '1212', '') == matcher.match('800-555-1212').groups()
        assert matcher.match('work 1-(800) 555.1212 #1234') is None

    def test_handle_ignore_head(self):
        matcher = TelMatch(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        assert ('800', '555', '1212', '1234') == matcher.match('work 1-(800) 555.1212 #1234').groups()
        assert ('800', '555', '1212', '') == matcher.match('800-555-1212').groups()
        assert ('800', '555', '1212', '1234') == matcher.match('80055512121234').groups()

    def test_all_in_one(self):
        phonePattern = re.compile(r'''
        # don't match beginning of string, number can start anywhere
        (\d{3}) # area code is 3 digits (e.g. '800')
        \D* # optional separator is any number of non-digits
        (\d{3}) # trunk is 3 digits (e.g. '555')
        \D* # optional separator
        (\d{4}) # rest of number is 4 digits (e.g. '1212')
        \D* # optional separator
        (\d*) # extension is optional and can be any number of digits
        $ # end of string
        ''', re.VERBOSE)