#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo simulate an ATM pin machine
"""
    Docstring:
"""
master_pin = "0123"
pin = None
attempts = 0
# loop while pin is incorrect
while  pin != master_pin and attempts < 3:
    pin = int(input("Enter pin: "))

    if pin == master_pin:
        print("valid pin")
    else:
        print("invalid pin")
        attempts += 1

print("done")