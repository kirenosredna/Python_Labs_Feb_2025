#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""
import random

# lotto = []
#
# while len(lotto) < 6:
#     num = random.randint(1, 50)
#     if num not in lotto:
#         lotto.append(num)
#     else:
#         print(f"Duplicate number = {num}")

# pythonic solution.
lotto = set()
while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)

print(f"Lottery numbers = {lotto}")

chapter 5
question 1,2,4