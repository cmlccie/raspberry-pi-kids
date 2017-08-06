#!/usr/bin/env python3
"""Show emojis on the sense-hat LED grid."""

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


# Main Script
def main(message):
    """Show emojis on the sense-hat LED grid."""
    for color in color_cycle():
        try:
            sense.set_rotation(90)
            sense.show_message(
                message,
                scroll_speed=0.05,
                text_colour=color,
                back_colour=e,
            )
        except KeyboardInterrupt:
            sense.clear()
            os.system('clear')
            message = input("\nNew Emoji: ").strip()

if __name__ == "__main__":
    _, message = sys.argv
    try:
        main(message=message)
    except KeyboardInterrupt:
        sense.clear()
        os.system('clear')
        sys.exit(0)
