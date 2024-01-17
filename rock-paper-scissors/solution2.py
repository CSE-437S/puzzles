result = []
theirMove = []
score = 0

for line in open("input.txt", "r"):
    split = line.strip().split()
    theirMove.append(split[0])
    result.append(split[1])


for x, y in zip(result, theirMove):
    tempScore = 0
    if x == "X":
        tempScore = tempScore
        if y == "A":
            tempScore = tempScore + 3
        elif y == "B":
            tempScore = tempScore + 1
        else:
            tempScore = tempScore + 2
    elif x == "Y":
        tempScore = tempScore + 3
        if y == "B":
            tempScore = tempScore + 2
        elif y == "C":
            tempScore = tempScore + 3
        else:
            tempScore = tempScore + 1
    elif x == "Z":
        tempScore = tempScore + 6
        if y == "C":
            tempScore = tempScore + 1
        elif y == "A":
            tempScore = tempScore + 2
        else:
            tempScore = tempScore + 3
    score = score + tempScore
print(score)
    