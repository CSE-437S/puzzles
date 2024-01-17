# the second column says how the round needs to end: 
    # X means you need to lose, 
    # Y means you need to end the round in a draw, 
    # Z means you need to win

# first column is still what your opponent is going to play:
    # A for Rock
    # B for Paper
    # C for scissors

# points: (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

def solutionPartTwo(strategy):
    lines = strategy.split('\n')
    score = 0
    for line in lines:
        line = line.split(' ')
        turn_score = 0
        opponentChoice = line[0]
        desiredOutcome = line[1]

        if opponentChoice == 'A':
            if desiredOutcome == 'X':
                # you need to chooce scissors
                turn_score += 3
            elif desiredOutcome == 'Y':
                # you need to choose rock (draw)
                turn_score += 1
                turn_score += 3
            elif desiredOutcome == 'Z':
                # you need to choose paper
                turn_score += 2
                turn_score += 6
        
        if opponentChoice == 'B': # paper
            if desiredOutcome == 'X':
                # you need to choose rock
                turn_score += 1
            if desiredOutcome == 'Y':
                # you need to choose paper (draw)
                turn_score += 2
                turn_score += 3
            if desiredOutcome == 'Z':
                # you need to choose scissors
                turn_score += 3
                turn_score += 6
        
        if opponentChoice == 'C': # scissors
            if desiredOutcome == 'X':
                # you need to choose paper
                turn_score += 2
            if desiredOutcome == 'Y':
                # you need to choose scissors (draw)
                turn_score += 3
                turn_score += 3
            if desiredOutcome == 'Z':
                # you need to choose rock
                turn_score += 1
                turn_score += 6
        
        score += turn_score

    return score

def solution(strategy):
    lines = strategy.split('\n')
    score = 0
    for line in lines:
        line = line.split(' ')
        turn_score = 0

        if line[1] == 'X':
            turn_score += 1

            if line[0] == 'A':
                turn_score += 3
            elif line[0] == 'B':
                turn_score += 0
            elif line[0] == 'C':
                turn_score += 6

        elif line[1] == 'Y':
            turn_score += 2

            if line[0] == 'A':
                turn_score += 6
            elif line[0] == 'B':
                turn_score += 3
            elif line[0] == 'C':
                turn_score += 0

        elif line[1] == 'Z':
            turn_score += 3

            if line[0] == 'A':
                turn_score += 0
            elif line[0] == 'B':
                turn_score += 6
            elif line[0] == 'C':
                turn_score += 3

        score += turn_score
    
    return score

# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

# Your total score is the sum of your scores for each round (want to maximize this)
# The score for a single round is the score for the shape you selected 
    # (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

if __name__ == '__main__':
    with(open('rock-paper-scissors/ben.j.mueller/input2.txt', 'r')) as f:
        strategy = f.read()
        score = solutionPartTwo(strategy)
        print(score)
        # print(strategy)
    print("Hello, world!")