
rockScore = 1
paperScore = 2
scissorsScore = 3


myScore = 0


opMoves = []  # Opponent's moves
reqOutcomes = []  # Required outcomes


with open("input.txt", "r") as f:
    for line in f:
        split = line.strip().split()
        opMoves.append(split[0])  # Op
        reqOutcomes.append(split[1]) 


for op, outcome in zip(opMoves, reqOutcomes):
    if op == 'A':  
        if outcome == 'Y':  # Draw
            myScore += rockScore + 3
        elif outcome == 'X':  # Lose
            myScore += scissorsScore
        else:  # Win
            myScore += paperScore + 6

    elif op == 'B':  
        if outcome == 'Y':  # Draw
            myScore += paperScore + 3
        elif outcome == 'X':  # Lose
            myScore += rockScore
        else:  # Win
            myScore += scissorsScore + 6

    else:  
        if outcome == 'Y':  # Draw
            myScore += scissorsScore + 3
        elif outcome == 'X':  # Lose
            myScore += paperScore
        else:  # Win
            myScore += rockScore + 6

print(myScore)
