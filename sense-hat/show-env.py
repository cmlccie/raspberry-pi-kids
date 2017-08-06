#!/usr/bin/env python3
"""Show the environment data on the sense-hat LED grid."""

# Imports
import os
import random
import sys

from sense_hat import SenseHat


# Global variables
sense = SenseHat()

e = (0,   0,   0  )     # empty (no color)
r = (255, 0,   0  )     # red
o = (255, 127, 0  )     # orange
y = (255, 255, 0  )     # yellow
g = (0,   255, 0  )     # green
b = (0,   0,   255)     # blue
i = (75,  0,   130)     # indigo
v = (159, 0,   255)     # violet
c = (0,   255, 255)     # cyan
w = (255, 255, 255)     # white

colors = (r, o, y, g, b, i, v, c, w)

# Helper Functions
def random_color():
    """Return a random color."""
    return random.choice(colors)


def color_cycle():
    """Cycle through the colors."""
    while True:
        for color in colors:
            yield color


def fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return ((celsius/5)*9)+32


# Main Script
def main():
    """Show the environment data on the sense-hat LED grid."""
    while True:
        # Get envrionment data
        env_text = ("{temperature:0.1f}°F {humidity:0.1f}% {pressure:0.1f}mb"
                    "".format(
                        temperature=fahrenheit(sense.get_temperature()),
                        humidity=sense.get_humidity(),
                        pressure=sense.get_pressure(),
                    ))
        
        # Display on stdout
        os.system('clear')
        print(env_text)

        # Display on sense-hat
        sense.set_rotation(0)
        sense.show_message(
            env_text,
            scroll_speed=0.05,
            text_colour=random_color(),
            back_colour=e,
        )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sense.clear()
        os.system('clear')
        sys.exit(0)
