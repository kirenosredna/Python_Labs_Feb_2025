#! /usr/bin/env python3
# Author: DCameron
# Description: This script will simulate a calculator APP
"""
    Calculator App with add. multiply and divide functions
"""

def add(x, z):
    """ Return Sum of x and z as a float """
    return float(x+z)

def mul(x, z):
    """ Return product of x and z as a float """
    return float(x*z)

def div(x, z):
    """ Return quotient of x divided by z to 3 decimal places """
    return round(x/z, 3)


print(f"4 + 3 = {add(4, 3)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")


# Alternative way of defining SIMPLE functions without
# using def statement.
l_add = lambda x, z:float(x+z)
l_mul = lambda x, z:float(x*z)
l_div = lambda x, z:round(x/z, 3)

print(f"4 + 3 = {l_add(4, 3)}")
print(f"4 * 3 = {l_mul(4, 3)}")
print(f"4 / 3 = {l_div(4, 3)}")