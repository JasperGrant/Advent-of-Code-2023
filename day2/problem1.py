# Advent of Code day 2 Problem 1
# Written by Jasper Grant

import re

# Init sum as 0
s = 0
# Init dict of colors and values
color_pairs = {'green': 13, 'red': 12, 'blue': 14}
# Parse lines of input
for line in open('input.txt'):
    # Pull out ID of line
    ID = re.findall(r'\d+', line)[0]
    # Reset possible
    possible = True
    # If a color is impossible in a game, possible is false
    for color in color_pairs:
        for number in re.findall(r'(\d+) ' + color, line):
            if int(number) > color_pairs[color]:
                possible = False
    # If possible add to list
    if possible:
        s += int(ID)

print(s)
