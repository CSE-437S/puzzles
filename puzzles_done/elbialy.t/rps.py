import shlex
L = ["A Y\n", "B X\n", "C Z\n"]


score = 0
for line in L:
    opponent, you = shlex.split(line)
    # A for Rock, B for Paper, and C for Scissors.
    # X for Rock, Y for Paper, and Z for Scissors
    # first adddition is for whats played the second is for win draw or loss
    if opponent == 'A' and opponent == 'X':
        score += 1   
        score += 3
    elif opponent == 'A' and you == 'Y':
        score += 2
        score += 6
    elif opponent == 'A' and you == 'Z':
        score +=  3 
        score += 0
    elif opponent == 'B' and you == 'X':
        score +=    1
        score += 0
    elif opponent == 'B' and you == 'Y':
        score +=    2
        score += 3
    elif opponent == 'B' and you == 'Z':
        score +=   3 
        score += 6
    elif opponent == 'C' and you == 'X':
        score +=    1
        score += 6
    elif opponent == 'C' and you == 'Y':
        score +=    2
        score += 0
    elif opponent == 'C' and you == 'Z':
        score +=    3
        score += 3



print(score)