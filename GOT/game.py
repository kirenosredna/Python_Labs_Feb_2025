#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This is Game of Tanks
"""
    Game of Tanks:
"""
import tank
import sys


def main():

    erik_tank = tank.Tank("German", "Tiger")
    zane_tank = tank.Tank("American", "Sherman")
    aram_tank = tank.Tank("British", "Churchhill")

    erik_tank.accel(61)
    zane_tank.accel(44)

    aram_tank.rotate_left(289)
    aram_tank.accel(31)
    aram_tank.shoot()

    erik_tank.take_damage(2)
    zane_tank.take_damage(32)

    return None

if __name__ == "__main__"
    main()
    sys.exit(0)