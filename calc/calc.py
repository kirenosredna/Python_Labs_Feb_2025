#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This is an ultra realistic calculator app with features!
"""
    Calc App with basic and adv functions:
"""


import sys
import adv
import basic

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
        print(f"Modulus of 100 by 45 =  {adv.mod(100, 45)}")
        print(f"Square root of 25 = {adv.sqrt(25)}")
    else:
        print("invalid option")

    return None

# namespace trick
if __name__ == "__main__":
    main()
    sys.exit(0)


sys.exit(0)

