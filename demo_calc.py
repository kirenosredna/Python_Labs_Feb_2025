#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""

def add(x, z):
    return float(x + z)

def multiply(x, z):
    return float(x * z)

def divide(x, z):
    return round(x/z, 3)

# print(f"4 + 3 = {add(4, 3)}")
# print(f"4 * 3 = {multiply(4, 3)}")
# print(f"4 + 3 = {divide(4, 3)}")
l_add = lambda x, z:float(x+z)
l_mul = lambda x, z:float(x*z)
l_div = lambda x, z:round(x/z, 3)
print(f"4 + 3 = {l_add(4, 3)}")
print(f"4 * 3 = {l_mul(4, 3)}")
print(f"4 + 3 = {l_div(4, 3)}")
