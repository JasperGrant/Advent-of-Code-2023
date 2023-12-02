# Advent of Code day 2 Problem 2
# Written by Jasper Grant

import re

# Init sum as 0
s = 0
# Init dict of colors and values
color_pairs = {'green': 0, 'red': 0, 'blue': 0}
# Parse lines of input
for line in open('input.txt'):
    # For each of the three colors
    for color in color_pairs:
        # Get max value and then store in color_pairs
        color_pairs[color] = int(max([int(x) for x in re.findall(r'(\d+) ' + color, line)]))
        # Add to sum
    s += color_pairs['red']*color_pairs['green']*color_pairs['blue']
print(s)
