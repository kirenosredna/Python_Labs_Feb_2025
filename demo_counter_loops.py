#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to repeat block of
# commands a specific number of times using  counter loop.
"""
    Docstring:
"""

count = 0 # initialize
while count < 10:
    print(count)
    count += 1 # increment /decrement counter or could get infinite loop


# alternate use for loop and range function
# range( start, stop, step=1) step 1 is default, start is 0 default

for num in range(0, 10, 1):
    print(num)

