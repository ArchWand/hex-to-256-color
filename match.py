# Match an input hex with the closest 256 color

import json
import sys

# load the json into multiple dicts
colors_json = '256colors.json'
with open(colors_json) as f:
    colors = json.load(f)

# Return the int value of the 256 color
# that most closely matches the input hex
def match(color):
    # Convert hex to rgb
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    # Find the closest color
    closest = 0
    closest_distance = 1000000
    for i in range(0, 256):
        # Store the color values
        r2 = colors[i]['rgb']['r']
        g2 = colors[i]['rgb']['g']
        b2 = colors[i]['rgb']['b']

        # Calculate the distance
        distance = (r - r2)**2 + (g - g2)**2 + (b - b2)**2

        # If this is the closest color, store it
        if distance < closest_distance:
            closest = i
            closest_distance = distance

    return closest

# ask the user for a hex code
hex = input("Enter a hex code: #")

# match the hex to the closest 256 color
color = match(hex)

# print the result
print("The closest 256 color is: " + str(color))
