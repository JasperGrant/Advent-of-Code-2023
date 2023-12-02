# Advent of Code day 1 Problem 2
# Written by Jasper Grant

# Import regular expressions
import re

# Define replacement lists
ints = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
extraints = ["zeroo", "onee", "twoo", "threee", "four", "fivee", "six", "sevenn", "eightt", "ninee"]
# Open file
file = open('input.txt').read()

# Replace numbers with versions that have extra ending characters
for number in range(0, 10):
    file = file.replace(ints[number], extraints[number])

# Replace numbers with decimals
for number in range(0, 10):
    file = file.replace(ints[number], str(number))

# For each line in the file use a regex int finder to get all ints, concanate first and last, and then sum these numbers
print(sum(int(re.findall(r'\d', line)[0] + re.findall(r'\d', line)[-1]) for line in file.split('\n')))
