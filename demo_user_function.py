#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo howto define, name, call
# user function with optional parameters and optionally return a value
"""
    Docstring:
"""

# Annotations
def say_hello(greeting:str="bonjour", recipient:str="mes amis")-> str:
    message = f"{greeting} {recipient}"
    return message


print(say_hello("hola", "amigos"))
print(say_hello("ciao", "amici")) #positional parameters
print(say_hello(greeting="ciao", recipient="amici")) # named parameters
print(say_hello("ciao", recipient="amici")) # mixed param passing but named come after
print(say_hello("howdy", ))

print("Annotations for say_hello = ", say_hello.__annotations__) # fact finding.