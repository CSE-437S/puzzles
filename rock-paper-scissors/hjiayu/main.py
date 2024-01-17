f = open('input2.txt')
plays = []
for line in f:
    plays.append((line[0], line[2]))

SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

SCORES2 = {
    'A': 1,
    'B': 2,
    'C': 3
}

SCORES_GAME = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3
}

score = 0

for r in plays:
    score += SCORES_GAME[r]
    score += SCORES[r[1]]

print("Part 1 Final Score: ", score)

WIN = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

DRAW = {
    'A': 'A',
    'B': 'B',
    'C': 'C'
}

LOSE = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

RELATIONSHIP = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}

SCORES_GAME2 = {
    ('A', 'A'): 3,
    ('A', 'B'): 6,
    ('A', 'C'): 0,
    ('B', 'A'): 0,
    ('B', 'B'): 3,
    ('B', 'C'): 6,
    ('C', 'A'): 6,
    ('C', 'B'): 0,
    ('C', 'C'): 3
}

scores2 = 0

for r in plays:
    choice = RELATIONSHIP[r[1]][r[0]]
    scores2 += SCORES_GAME2[(r[0], choice)]
    scores2 += SCORES2[choice]

print(scores2)