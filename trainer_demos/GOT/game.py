#! /usr/bin/env python3
# Author: DCameron
# Description: This is a Game of Tanks
"""
    GOT - Game of Tanks
"""
import tank
import sys

def main():
    # Instantiate/Create 3 Tank objects
    erik_tank = tank.Tank("german", "tiger")
    zane_tank = tank.Tank("american", "sherman")
    aram_tank = tank.Tank("british", "churchill")

    # And the game begins..
    erik_tank.accel(61)
    zane_tank.accel(44)

    aram_tank.rotate_left(289)
    aram_tank.accel(31)
    aram_tank.shoot()

    # ..and success!
    erik_tank.take_damage(37)
    zane_tank.take_damage(49)

    # And now for some visuals..
    # print(f"Health of Erik's tank is {erik_tank._health}") # POOR!

    # Example of Operator Overloading
    print(f"Status of Erik's and Zane's tank is {erik_tank + zane_tank}")

    # Erik receives a HEALTH BOOST!
    # erik_tank._health = 100 # POOR
    # print(f"New health of Erik's Tank is {erik_tank._health}") # POOR
    erik_tank.set_health(101) # SETTER GOOD!
    print(f"New health of Erik's Tank is {erik_tank.get_health()}")  # GETTER GOOD!

    erik_tank.tank_health = 102
    print(f"New health of Erik's Tank is {erik_tank.tank_health}")  # GETTER GOOD!
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)