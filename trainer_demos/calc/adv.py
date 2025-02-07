#! /usr/bin/env python3
# Author: DCameron
# Description: This module contains a collection of advanced calculator functions
"""
    Advanced Calc functions including mod, power, and sqrt
"""

import sys

def mod(x, z):
    """ Return REMAINDER of x divided by z """
    return x % z

def power(x, z):
    """ Return POWER of x to z """
    return x**z

def sqrt(x):
    """ Return square root of x """
    return round(x**0.5, 2)

def main():
    print("ADVANCED Calculator App")
    print("-" * 30)

    print(f"100 % 30 = {mod(100, 30)}")
    print(f"100 ** 3 = {power(100, 3)}")
    print(f"\N{square root}100 = {sqrt(100)}")
    return None

# Namespace TRICK.
if __name__ == "__main__":
    # EXECUTES only when run directly as a program
    main()
    sys.exit(0) # Exit program with 0 errors.