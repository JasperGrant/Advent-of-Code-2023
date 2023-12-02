# Advent of Code day 1 Problem 1
# Written by Jasper Grant

# Import regular expressions
import re

# For each line in the file use a regex int finder to get all ints, concanate first and last, and then sum these numbers
print(sum(int(re.findall(r'\d', line)[0] + re.findall(r'\d', line)[-1]) for line in open('input.txt')))
