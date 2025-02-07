#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import unittest
import sys
sys.path.append(r"c:\users\donal\course\Python_Labs_Feb_2025\trainer_demos\calc")
from calc import basic



class TestCases(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3), 7, "Should be 7")
        self.assertEqual(basic.add(4, 3, 2), 9.1, "Should be 9")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 13, "Should be 12")
        self.assertEqual(basic.mul(4, 3, 2), 24, "Should be 24")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.333, "Should be 1.333")
        self.assertEqual(basic.div(5, 4), 1.25, "Should be 1.25")
        return None

if __name__ == "__main__":
    unittest.main()
