#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This module describes a Class of Tank
"""
    Tank class for -  Game of Tanks
"""
class Tank:
    # Attributes/ Data  and Behavior/Methods
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._location = {'x': 0, 'y':0, 'z': 0}
        self._direction = 0
        self._shells = 20
        self._health = 100
        # no explicit return, called implicitly

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return

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

    # some special methods
    # example of operator overloading
    def __add__(self, other):
        return self._health + other._health

    def __del__(self):
        print("Boom..boom.boom!")
        return None

    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None

    #wrap access to the getter and setter using ONE variable name. Get first then set methods
    tank_health = property(get_health, set_health)

    # Alternative using DECORATORS
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None



