PATH = "input.txt"

def parse_input(filename):
    # list of opponent moves in first column (A = ROCK, B = PAPER, C = SCISSORS), then space, then list of your moves (X = ROCK, Y = PAPER, Z = SCISSORS)
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data

def get_points(pairing):
    def theirs_as_yours(theirs):
        if theirs == 'A':
            return 'X'
        elif theirs == 'B':
            return 'Y'
        elif theirs == 'C':
            return 'Z'
    # scoring system: 1pt for rock, 2 for paper, 3 for scissors. then, 0 for lose, 3 for draw, 6 for win
    yours = pairing[2]
    theirs = pairing[0]

    score = 0
    # playing score
    if yours == 'X':
        score += 1
    elif yours == 'Y':
        score += 2
    elif yours == 'Z':
        score += 3

    # winning score
    if yours == 'X' and theirs == 'C':
        score += 6
    elif yours == 'Y' and theirs == 'A':
        score += 6
    elif yours == 'Z' and theirs == 'B':
        score += 6
    elif yours == theirs_as_yours(theirs):
        score += 3
    return score


instructions = parse_input(PATH)

# part I

total_score = 0
for i in instructions:
    round_score = get_points(i)
    total_score += round_score
print("Part I:")
print(total_score)

# part II

# change how get_points works. X means need to lose, Y means need to draw, Z means need to win
def get_points_two(pairing):
    # somewhat easier really. first need to calculate what you need to do to achieve the outcome
    yours = pairing[2]
    theirs = pairing[0]

    chosen_move = ''
    if yours == 'X':
        # pick losing move
        if theirs == 'A':
            chosen_move = 'Z'
        elif theirs == 'B':
            chosen_move = 'X'
        elif theirs == 'C':
            chosen_move = 'Y'
    elif yours == 'Y':
        # pick drawing move
        if theirs == 'A':
            chosen_move = 'X'
        elif theirs == 'B':
            chosen_move = 'Y'
        elif theirs == 'C':
            chosen_move = 'Z'
    elif yours == 'Z':
        # pick winning move
        if theirs == 'A':
            chosen_move = 'Y'
        elif theirs == 'B':
            chosen_move = 'Z'
        elif theirs == 'C':
            chosen_move = 'X'

    # now calculate score
    score = 0
    # playing score
    if chosen_move == 'X':
        score += 1
    elif chosen_move == 'Y':
        score += 2
    elif chosen_move == 'Z':
        score += 3

    # winning score
    if yours == 'X':
        score += 0
    elif yours == 'Y':
        score += 3
    elif yours == 'Z':
        score += 6

    return score

# simulate
total_score = 0
for i in instructions:
    round_score = get_points_two(i)
    total_score += round_score

print("Part II:")
print(total_score)