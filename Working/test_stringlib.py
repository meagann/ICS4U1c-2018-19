import unittest

import stringlib


class TestStringlib(unittest.TestCase):

    def test_strLength_general1(self):
        self.assertEqual(4, stringlib.strLength("yeye"))

    def test_strLength_general2(self):
        self.assertEqual(6, stringlib.strLength("yeyeye"))

    def test_strLength_corner(self):
        self.assertEqual(0, stringlib.strLength(""))

    def test_strLength_unusual(self):
        self.assertEqual(2, stringlib.strLength(56))
