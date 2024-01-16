# Read file
with open("input.txt") as f:
    lines = f.readlines()

opponent  = []
you = []
for line in lines:
    line = line.split(" ")
    opponent.append(line[0].strip())
    you.append(line[1].strip())


score = 0
for i in range(0, len(opponent)):
    if opponent[i] == "A":
        if you[i] == "X":
            score += 4
        elif you[i] == "Y":
            score += 8
        else:
            score += 3
    elif opponent[i] == "B":
        if you[i] == "X":
            score += 1
        elif you[i] == "Y":
            score += 5
        else:
            score += 9
    elif opponent[i] == "C":
        if you[i] == "X":
            score += 7
        elif you[i] == "Y":
            score += 2
        else:
            score += 6

print(score)
