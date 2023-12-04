# Advent of Code day 4 Problem 1
# Written by Jasper Grant

import regex as re

# Open input file as lines
games = open('input.txt').read().split('\n')

# List for numbers of cards
cards = [1 for i in range(0,len(games))]

# For each game
for game in games:
    # Split numbers into mine and winning
    my_numbers_string, winning_numbers_string = game.split("|")
    # Get game ID
    ID = int(re.findall(r'\d+',my_numbers_string)[0])-1
    # List comprehension to see how many shared
    matches = len([number for number in re.findall(r'\d+', my_numbers_string.split(':')[1]) if number in re.findall(r'\d+', winning_numbers_string)])
    # If score is non zero
    if matches:
        # Match after current card number of points
        for i in range(1,matches+1):
            # Ensure not out of bounds
            if i < len(games):
                # Add cards based on number of current card
                cards[ID+i] += cards[ID]


print(sum(cards))