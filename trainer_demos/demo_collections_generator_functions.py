#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO yield objects one at a time
# Using a generator function.
"""
    Docstring:
"""

def get_numbers():
    """ Return a list of numbers """
    numbers = []
    for x in range(0, 100000000000):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ Yield one object at a time """
    for x in range(0, 10):
        yield x


# for z in get_numbers():
for z in generate_numbers():
    print(z)

# Alternatively, we could use a while loop..
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Alternatively, we could just request the next yielded value manually..
gen = generate_numbers()
num1 = next(gen, False)
num2 = next(gen)
num3 = next(gen)
print(num1, num2, num3)





