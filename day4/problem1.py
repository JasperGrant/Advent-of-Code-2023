# Advent of Code day 4 Problem 1
# Written by Jasper Grant

import regex as re

# Initialize sum as 0
s = 0

# For each game
for game in open('input.txt'):
    # Split numbers into mine and winning
    my_numbers_string, winning_numbers_string = game.split("|")
    # List comprehension to see how many shared
    matches = len([number for number in re.findall(r'\d+', my_numbers_string.split(':')[1]) if number in re.findall(r'\d+', winning_numbers_string)])
    # If score is non zero
    if matches:
        # Calculate score with exponent
        s += 2 ** (matches - 1)

print(s)
