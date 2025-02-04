#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""


#                    1         2         3         4
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))
print(Belgium.replace(",", ":"))

pop_country = int(Belgium[8:16]) # Remember to CONVERT str into int!
pop_capital = int(Belgium[26:32])

print(f"Population of Country and capital = {pop_country + pop_capital}")
print("-" * len(Belgium))