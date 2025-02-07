#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name, and call
# a user function with optional parameters and optionally return a value
"""
    Docstring:
"""
# Example of a USER function with
# optional parameter passing and default values.
# Annotations - embedded comment for preferred parameter datatype.
def say_hello(greeting:str="bonjour", recipient:str="mes amis")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None


say_hello("hola", "amigos") # Positional parameter passing
say_hello(greeting="ciao", recipient="amici") # Named parameter passing
say_hello(recipient="dosto", greeting="namaste") # Named parameter passing (different order)
say_hello("yo", recipient="homies") # Mixed parameter passing (positional->named)
say_hello("bonjour", 5)
say_hello()

print("Annotations for say_hello = ", say_hello.__annotations__) # Fact Finding.