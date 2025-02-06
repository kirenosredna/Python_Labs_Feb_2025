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

    # visuals ;-)
    #print(f"Health of Erik's tank is {erik_tank._health}")
    #example of operator overloading
    print(f"Status of Erik's and Zane's tank is {erik_tank + zane_tank}")

    erik_tank.set_health(101)
    erik_tank.tank_health = 102
    print(f"New health of Erik's tank is {erik_tank.get_health()}")
    print(f"New health of Erik's tank is {erik_tank.tank_health}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)