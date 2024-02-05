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

#  Rosewater 	#f5e0dc
#  Flamingo 	#f2cdcd
#  Pink 	#f5c2e7
#  Mauve 	#cba6f7
#  Red 	#f38ba8
#  Maroon 	#eba0ac
#  Peach 	#fab387
#  Yellow 	#f9e2af
#  Green 	#a6e3a1
#  Teal 	#94e2d5
#  Sky 	#89dceb
#  Sapphire 	#74c7ec
#  Blue 	#89b4fa
#  Lavender 	#b4befe
#  Text 	#cdd6f4
#  Subtext1 	#bac2de
#  Subtext0 	#a6adc8
#  Overlay2 	#9399b2
#  Overlay1 	#7f849c
#  Overlay0 	#6c7086
#  Surface2 	#585b70
#  Surface1 	#45475a
#  Surface0 	#313244
#  Base 	#1e1e2e
#  Mantle 	#181825
#  Crust 	#11111b

# make map of name and tuple (hex string, int)
cols = {
  'Rosewater': 'f5e0dc',
  'Flamingo': 'f2cdcd',
  'Pink': 'f5c2e7',
  'Mauve': 'cba6f7',
  'Red': 'f38ba8',
  'Maroon': 'eba0ac',
  'Peach': 'fab387',
  'Yellow': 'f9e2af',
  'Green': 'a6e3a1',
  'Teal': '94e2d5',
  'Sky': '89dceb',
  'Sapphire': '74c7ec',
  'Blue': '89b4fa',
  'Lavender': 'b4befe',
  'Text': 'cdd6f4',
  'Subtext1': 'bac2de',
  'Subtext0': 'a6adc8',
  'Overlay2': '9399b2',
  'Overlay1': '7f849c',
  'Overlay0': '6c7086',
  'Surface2': '585b70',
  'Surface1': '45475a',
  'Surface0': '313244',
  'Base': '1e1e2e',
  'Mantle': '181825',
  'Crust': '11111b'
}

for color, code in cols.items():
  print(f'{color} is closest to {match(code)}')

