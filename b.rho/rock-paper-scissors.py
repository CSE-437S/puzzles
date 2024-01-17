import numpy
import sys

file = open('puzzle-input.txt', 'r')
f = file.readlines() 

score = 0

# The possible outcomes for rock, paper, scissors - ordered as such:
# BX = Paper/Rock (Win), CX = Scissors/Rock (Loss), AX = Rock/Rock (Tie)
# AY = Rock/Paper (Loss), BY = Paper/Paper (Tie), CY = Scissors/Paper (Win)
# CZ = Paper/Scissors (Tie), AZ = Rock/Scissors (Win), BZ = Paper/Scissors (Loss)
outcomes = [
    'AY','BY','CY',
    'BX','CX','AX',
    'CZ','AZ','BZ'
]

# iterating through doc
for line in f:
    # get rid of white space
    line = line.strip().replace(" ", "")
    # find the combination from the list
    sol = outcomes.index(line)
    # if the sol is above 0 and below/equal to 2 indexed
    if sol >= 0 and sol <= 2:
        # add 3 to the score
        score += 3
    # else if sol is greater than 2 and less/equal to 5
    elif sol > 2 and sol <= 5:
        # add 6 to score
        score += 6
    # calculate the true score
    #score += (sol % 3)


print(score)