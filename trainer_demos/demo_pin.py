#! /usr/bin/env python3
# Author: DCameron
# Description: This script will simulate a high street bank
# ATM PIN machine. Max 3 attempts!
"""
    Docstring:
"""

master_pin = "0123"
pin = None
attempts = 0

# Loop whilst PIN is incorrect
while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break # Break out ENTIRE loop and ignore else
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # Executes ONLY ONCE when LOOP becomes False
    print("Too many attempts", attempts)
    print("Your card has been retained. Have a nice day!")


print("Done.")

