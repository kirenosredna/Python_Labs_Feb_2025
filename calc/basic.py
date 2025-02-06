#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This module  contains collection of calculator functions
"""
    basic calc functions :
"""

import sys

def add(*args):
    """ return sum of all parameters"""
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    return round(x/z, 3)


def main():


    print("Basic Calculator App")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 + 3 + 2 = {add(4, 3, 2)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None


# namespace trick
if __name__ == "__main__":
    main()
    sys.exit(0)