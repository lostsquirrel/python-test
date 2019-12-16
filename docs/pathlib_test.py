# -*- coding: UTF-8 -*-

import unittest
from pathlib import Path


class PathLibTests(unittest.TestCase):

    def test_parent(self):
        p = Path(__file__)
        print(p, p.parent)
        self.assertTrue(str(p).startswith(str(p.parent)))
