#! /usr/bin/env python3
# Author: DCameron
# Description: This is an ULTRA REALISTIC Calculator App with tons of features!
"""
    Calc App with BASIC and ADVANCED functions.
"""

import sys
import basic
# from basic import add, mul
import adv

def main():
    menu = """
            Calculator App
            --------------
            1. Test Basic
            2. Test Adv
    """
    print(menu)
    option = input("Choose 1 or 2: ")
    if option == "1":
        print(f"100 + 50 + 25 + 12.5 = {basic.add(100, 50, 25, 12.5)}")
        print(f"100 * 50 * 25 * 12.5 = {basic.mul(100, 50, 25, 12.5)}")
    elif option == "2":
        print(f"Modulus of 100 by 45 = {adv.mod(100, 45)}")
        print(f"Square root of 25 = {adv.sqrt(25)}")
    else:
        print("Invalid Option")
    return None

# Namespace TRICK.
if __name__ == "__main__":
    # EXECUTES only when run directly as a program
    main()
    sys.exit(0) # Exit program with 0 errors.
