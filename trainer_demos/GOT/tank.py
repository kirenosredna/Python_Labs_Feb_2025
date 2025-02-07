#! /usr/bin/env python3
# Author: DCameron
# Description: This module describes a Class of Tank
"""
    Tank class for - Game of Tanks
"""
import vehicle

class Tank(vehicle.Vehicle, , , , , ):
    # Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        super().__init__(country, model)
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._shells = 20
        self._health = 100
        # No Explicit Return, as called implicitly.

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # SOME SPECIAL METHODS
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    def __del__(self):
        print("Boom..boom..boom")
        return None

    # Example of a GETTER + SETTER method.
    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None

    # Wrap access to the getter and setter using ONE variable name interface
    # tank_health = property(get_health, set_health)

    # Alternative using DECORATORS!
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None
