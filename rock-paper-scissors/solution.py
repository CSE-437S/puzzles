myMoves = []
theirMove = []
score = 0

for line in open("other.txt", "r"):
    split = line.strip().split()
    theirMove.append(split[0])
    myMoves.append(split[1])


for x, y in zip(myMoves, theirMove):
    tempScore = 0
    if x == "X":
        tempScore = tempScore + 1
        if y == "A":
            tempScore = tempScore + 3
        elif y == "B":
            tempScore = tempScore
        else:
            tempScore = tempScore + 6
    elif x == "Y":
        tempScore = tempScore + 2
        if y == "B":
            tempScore = tempScore + 3
        elif y == "C":
            tempScore = tempScore
        else:
            tempScore = tempScore + 6
    elif x == "Z":
        tempScore = tempScore + 3
        if y == "C":
            tempScore = tempScore + 3
        elif y == "A":
            tempScore = tempScore
        else:
            tempScore = tempScore + 6
    score = score + tempScore
print(score)
    

