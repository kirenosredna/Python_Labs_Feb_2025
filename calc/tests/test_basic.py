import unittest
from ..calc import basic



class TestCases(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3), 7, "Should be 7")
        self.assertEqual(basic.add(4, 3, 2), 9, "Should be 9")

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 7, "Should be 7")
        self.assertEqual(basic.mul(4, 3, 2), 24, "Should be 24")