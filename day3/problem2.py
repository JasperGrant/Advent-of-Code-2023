# Advent of Code day 3 Problem 2
# Written by Jasper Grant

import regex as re
from collections import defaultdict

# Sum is 0
s = 0

# Dictionary to hold asterisk locations and valid gear values
gears = defaultdict(list)

# Open file as string
input_file = open('input.txt').read()

line_length = 141


# Function that takes an index to the input file, 
# Returns the character if it is numeric or '' if is non-numeric or out of nounds
def get_character(index):
    try:
        return input_file[index] if input_file[index].isnumeric() else ''
    except IndexError:
        return ''


# Function that takes an index to the input file found to be numeric
# If it is part of a larger number returns larger number
def continue_number(index):
    # Declare starting number
    number = get_character(index)
    # If number continues to the right append
    if get_character(index + 1) != '':
        number += get_character(index + 1)
        if get_character(index + 2) != '':
            number += get_character(index + 2)
    # If number continues to the left append
    if get_character(index - 1) != '':
        number = get_character(index - 1) + number
        if get_character(index - 2) != '':
            number = get_character(index - 2) + number
    # Return result
    return number


# For gear center
for i in range(0, len(input_file)):
    if input_file[i] == '*':

        # Define variables to make positions easier to work with
        top_left = i - line_length - 1
        top_center = i - line_length
        top_right = i - line_length + 1
        left = i - 1
        right = i + 1
        bottom_left = i + line_length - 1
        bottom_center = i + line_length
        bottom_right = i + line_length + 1

        # Top cases
        if get_character(top_left) != '' and get_character(top_center) == '' and get_character(top_right) != '':
            gears[i].append(continue_number(top_left))
            gears[i].append(continue_number(top_right))
        elif get_character(top_left) != '':
            gears[i].append(continue_number(top_left))
        elif get_character(top_center) != '':
            gears[i].append(continue_number(top_center))
        elif get_character(top_right) != '':
            gears[i].append(continue_number(top_right))

        # Middle cases
        if get_character(left) != '':
            gears[i].append(continue_number(left))
        if get_character(right) != '':
            gears[i].append(continue_number(right))

        # Bottom cases
        if get_character(bottom_left) != '' and get_character(bottom_center) == '' and get_character(bottom_right) != '':
            gears[i].append(continue_number(bottom_left))
            gears[i].append(continue_number(bottom_right))
        elif get_character(bottom_left) != '':
            gears[i].append(continue_number(bottom_left))
        elif get_character(bottom_center) != '':
            gears[i].append(continue_number(bottom_center))
        elif get_character(bottom_right) != '':
            gears[i].append(continue_number(bottom_right))

# For each gear with two ratios multiply them and add to sum
for i in gears:
    if len(gears[i]) == 2:
        s += int(gears[i][0]) * int(gears[i][1])

print(s)
