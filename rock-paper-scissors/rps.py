f = open("input.txt")

lines = f.read().splitlines()

score = 0

bonus = {"X":1, "Y":2, "Z":3}

for line in lines:
    moves = line.split(" ")
    opp = moves[0]
    player = moves[1]
    
    
    score += bonus[player]
    
    if opp == "A":
        if player == "X":
            score += 3
        elif player == "Y":
            score += 6
        else:
            score += 0
    elif opp == "B":
        if player == "X":
            score += 0
        elif player == "Y":
            score += 3
        else:
            score += 6
    else:
        if player == "X":
            score += 6
        elif player == "Y":
            score += 0
        else:
            score += 3
            
print(score)