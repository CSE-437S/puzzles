


file1 = open('input.txt', 'r')
Lines = file1.readlines()

def calculate_score(input_data):
    move_scores = {"X": 1, "Y": 2, "Z": 3}
    outcome_scores = {"win": 6, "draw": 3, "loss": 0}
    move_to_win = {"A": "Z", "B": "X", "C": "Y"}

    total_score = 0

    for line in input_data:
        opponent_move, your_move = line.split()

        shape_score = move_scores[your_move]

        if your_move == move_to_win[opponent_move]:  
            outcome_score = outcome_scores["win"]
        elif opponent_move == your_move:  
            outcome_score = outcome_scores["draw"]
        else:  
            outcome_score = outcome_scores["loss"]

        total_score += shape_score + outcome_score

    return total_score

print(calculate_score(Lines))
