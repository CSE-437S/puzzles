rockScore = 1
paperScore = 2
scissorsScore = 3

myScore = 0

suggestedOp = []  
suggestedMe = []  

with open("input.txt", "r") as f:
    for line in f:
        split = line.strip().split()
        suggestedOp.append(split[0]) 
        suggestedMe.append(split[1]) 

for x, y in zip(suggestedOp, suggestedMe):
    if x == 'A':  
        if y == 'Y':  
            myScore += paperScore + 6  # Win
        elif y == 'Z':  # scissors
            myScore += scissorsScore  # Lose
        else:  # rock
            myScore += rockScore + 3  # Draw

    elif x == 'B':  # Paper
        if y == 'Y':  # Paper
            myScore += paperScore + 3 
        elif y == 'Z':  # Scissors
            myScore += scissorsScore + 6
        else:  # Rock
            myScore += rockScore 

    else:  #Scissors
        if y == 'Y':  #Paper
            myScore += paperScore  # Lose
        elif y == 'Z':  # Scissors
            myScore += scissorsScore + 3  # Draw
        else:  # Rock
            myScore += rockScore + 6  # Win

print(myScore)
