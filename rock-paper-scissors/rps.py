sum =0

lines = open('input.txt').read().split('\n\n')

#opponent: A for rock, B for paper, C for scissors
#your move: X for rock (+1), Y for paper (+2), Z for scissors (+3)
#outcome : +0 for loss, +3 for tie, +6 for win


# points = {
#     "A X": 0 + 3,
#     "A Y": 3 + 1,
#     "A Z": 6 + 2,
#     "B X": 0 + 1,
#     "B Y": 3 + 2,
#     "B Z": 6 + 3,
#     "C X": 0 + 2,
#     "C Y": 3 + 3,
#     "C Z": 6 + 1,
# }

score = 0
rpsArray = [
    'BX','CX','AX', #Loss
    'AY','BY','CY', #Ties
    'CZ','AZ','BZ' #Wins
]

for line in lines:
    solution = rpsArray.index(line)
    if solution > 2 and solution <= 5:
        score = score+ 3
    elif solution > 5:
        score = score+6
    score = score+(solution % 3) + 1

print(score)