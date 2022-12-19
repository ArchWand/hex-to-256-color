''' Match an input hex with the closest 256 color '''

import json

# load the json into multiple dicts
colors_json = '256colors.json' # pylint: disable=invalid-name
with open(colors_json, encoding='utf-8') as f:
    colors = json.load(f)

def match(color_to_match):
    '''
    Return the int value of the 256 color
    that most closely matches the input hex
    '''
    # Convert hex to rgb
    red = int(color_to_match[0:2], 16)
    green = int(color_to_match[2:4], 16)
    blue = int(color_to_match[4:6], 16)

    # Find the closest color
    closest = 0
    closest_distance = 1000000
    for i in range(0, 256):
        # Store the color values
        red2 = colors[i]['rgb']['r']
        green2 = colors[i]['rgb']['g']
        blue2 = colors[i]['rgb']['b']

        # Calculate the distance
        distance = ((red - red2) ** 2) + ((green - green2) ** 2) + ((blue - blue2) ** 2)

        # If this is the closest color, store it
        if distance < closest_distance:
            closest = i
            closest_distance = distance

    return closest

# ask the user for a hex code
hex_code = input("Enter a hex code: #")

# if the input starts with a #, remove it
if hex_code[0] == '#':
    hex_code = hex_code[1:]

# match the hex to the closest 256 color
color = match(hex_code)

# print the result
print("The closest 256 color is: " + str(color))
