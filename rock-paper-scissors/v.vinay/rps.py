import sys

def getInput():
    arr = []
    file = open("input.txt", "r")
    for line in file:
        line = line.strip()
        arr.append(line)
    return arr

def get_word(letter):
    if letter == "A" or letter == "X":
        return "rock"
    elif letter == "B" or letter == "Y":
        return "paper"
    elif letter == "C" or letter == "Z":
        return "scissors"
    
def get_word_2(letter):
    if letter == "X":
        return "lose"
    elif letter == "Y":
        return "draw"
    elif letter == "Z":
        return "win"
    
def get_turn_score(mine):
    if mine == "rock":
        return 1
    elif mine == "paper":
        return 2
    elif mine == "scissors":
        return 3

def handle_rock(mine):
    round_score = 0
    round_score += get_turn_score(mine)
    if mine == "rock":
        round_score += 3
    elif mine == "paper":
        round_score += 6
    elif mine == "scissors":
        round_score += 0
    return round_score

def handle_paper(mine):
    round_score = 0
    round_score += get_turn_score(mine)
    if mine == "rock":
        round_score += 0
    elif mine == "paper":
        round_score += 3
    elif mine == "scissors":
        round_score += 6
    return round_score

def handle_scissors(mine):
    round_score = 0
    round_score += get_turn_score(mine)
    if mine == "rock":
        round_score += 6
    elif mine == "paper":
        round_score += 0
    elif mine == "scissors":
        round_score += 3
    return round_score

def handle_rock_2(mine):
    round_score = 0
    if mine == "lose":
        round_score += get_turn_score("scissors")
        round_score += 0
    elif mine == "draw":
        round_score += get_turn_score("rock")
        round_score += 3
    elif mine == "win":
        round_score += get_turn_score("paper")
        round_score += 6
    return round_score

def handle_paper_2(mine):
    round_score = 0
    if mine == "lose":
        round_score += get_turn_score("rock")
        round_score += 0
    elif mine == "draw":
        round_score += get_turn_score("paper")
        round_score += 3
    elif mine == "win":
        round_score += get_turn_score("scissors")
        round_score += 6
    return round_score

def handle_scissors_2(mine):
    round_score = 0
    if mine == "lose":
        round_score += get_turn_score("paper")
        round_score += 0
    elif mine == "draw":
        round_score += get_turn_score("scissors")
        round_score += 3
    elif mine == "win":
        round_score += get_turn_score("rock")
        round_score += 6
    return round_score


def run_round(round):
    elf = get_word(round[0])
    mine = get_word(round[-1])
    score = 0
    if elf == "rock":
        score = handle_rock(mine)
    elif elf == "paper":
        score = handle_paper(mine)
    elif elf == "scissors":
        score = handle_scissors(mine)
    return score

def run_round_2(round):
    elf = get_word(round[0])
    mine = get_word_2(round[-1])
    score = 0
    if elf == "rock":
        score = handle_rock_2(mine)
    elif elf == "paper":
        score = handle_paper_2(mine)
    elif elf == "scissors":
        score = handle_scissors_2(mine)
    return score

def get_part():
    val = sys.argv[1]
    if val == "1":
        return True
    elif val == "2":
        return False
    else:
        return None

def main():
    part = get_part()
    input = getInput()
    total_score = 0
    if part == None:
        print("Invalid part")
        return
    if part:
        for round in input:
            total_score += run_round(round)
    else:
        for round in input:
            total_score += run_round_2(round)
    print(total_score)

if __name__ == "__main__":
    main()


