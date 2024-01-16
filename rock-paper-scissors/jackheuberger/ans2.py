
# Read file
with open("input.txt") as f:
    lines = f.readlines()

opponent  = []
you = []
for line in lines:
    line = line.split(" ")
    opponent.append(line[0].strip())
    you.append(line[1].strip())


# I'm sorry for the butt ugly code

score = 0
win = 6
tie = 3
loss = 0
for i in range(0, len(opponent)):
    if opponent[i] == "A":
        if you[i] == "X":
            score += loss + 3
        elif you[i] == "Y":
            score += tie + 1
        else:
            score += win + 2
    elif opponent[i] == "B":
        if you[i] == "X":
            score += loss + 1
        elif you[i] == "Y":
            score += tie + 2
        else:
            score += win + 3
    elif opponent[i] == "C":
        if you[i] == "X":
            score += loss + 2
        elif you[i] == "Y":
            score += tie + 3
        else:
            score += win + 1

print(score)
