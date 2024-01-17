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

def main():
    input = getInput()
    total_score = 0
    for round in input:
        total_score += run_round(round)
    print(total_score)

if __name__ == "__main__":
    main()


