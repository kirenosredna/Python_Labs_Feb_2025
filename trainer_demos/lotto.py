#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import random

# lotto = []

# while len(lotto) < 6:
#   num = random.randint(1, 50)
#    if num not in lotto:
#        lotto.append(num)
#    else:
#        print("Duplicate number =", num)

lotto = set() # Empty SET

# Pythonic solution - using a FEATURE that Python has!
while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)

print("Lottery numbers =", sorted(lotto))