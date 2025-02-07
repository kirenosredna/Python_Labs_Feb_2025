#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""

from calc import basic

def test_add():
    assert basic.add(4, 3) == 7, "Should be 7"
    assert basic.add(4, 3, 2) == 9, "Should be 9"
    return None

def test_mul():
    assert basic.mul(4, 3) == 12, "Should be 12"
    assert basic.mul(4, 3, 2) == 24, "Should be 24"
    return None

def test_div():
    assert basic.div(4, 3) == 1.333, "Should be 1.333"
    assert basic.div(5, 4) == 1.25, "Should be 1.25"
    return None

def main():
    print("Starting tests - only report ONE error at a time!")
    test_add()
    test_mul()
    test_div()
    print("All tests successful")
    return None

if __name__ == "__main__":
    main()