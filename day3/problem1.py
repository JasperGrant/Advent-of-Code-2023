# Advent of Code day 3 Problem 1
# Written by Jasper Grant

# Needed regex for variable length positive look behind
import regex as re

# Really gross one liner
# Andy said this one was hard so I wanted to do it in one line.
# Very gross long regex finds a tuple of 8 capture groups and one will have the correct number
# if it fits the conditions of a character around a number.
# Finally sums up these 8 numbers, sums up those and prints

print(sum([sum([int(y) for y in x if (y != '')]) for x in re.findall(r'(?<=[@#$%&*/=+-])(\d+)|(\d+)(?=[@#$%&*/=+-])|(?<=[@#$%&*/=+-][.\s\S]{137,141})(\d{3})|(\d{3})(?=[.\s\S]{137,141}[@#$%&*/=+-])|(?<=[@#$%&*/=+-][.\s\S]{138,141})(\d{2})|(\d{2})(?=[.\s\S]{138,141}[@#$%&*/=+-])|(?<=[@#$%&*/=+-][.\s\S]{139,141})(\d)|(\d)(?=[.\s\S]{139,141}[@#$%&*/=+-])', open('input.txt').read())]))