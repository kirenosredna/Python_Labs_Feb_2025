#! /usr/bin/env python3
# Author: DCameron
# Description: This module contains a collection of calculator functions
"""
    Basic Calculator functions including add, multiply and divide.
"""
import sys

def add(*args):
    """ Return SUM of all parameters
    >>> add(4, 3)
    7
    >>> add(4, 3, 2, 1)
    10
    """
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """ Return PRODUCT of all parameters
    >>> mul(4, 3, 2)
    24
    """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    >>> div(5, 4)
    1.25
    """
    return round(x/z, 3)

def main():
    print("Basic Calculator App")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 + 3 + 2 = {add(4, 3, 2)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

# Namespace TRICK.
if __name__ == "__main__":
    # EXECUTES only when run directly as a program
    # IGNORE if imported
    import doctest
    doctest.testmod()
    main()
    sys.exit(0) # Exit program with 0 errors.