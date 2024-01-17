import sys
file = sys.argv[1]
data_seperated = open(file).read().split("\n")
data_seperated = [ match.split(" ") for match in data_seperated]
move_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
# winning for me
winning_combos = [["X", "C"], ["Y", "A"], ["Z", "B"]]
tie_combos = [["X", "A"], ["Y", "B"], ["Z", "C"]]

def calculate_round_score(my_move, their_move):
    combo = [my_move, their_move]
    if combo in winning_combos:
        return 6 + move_score[my_move]
    elif combo in tie_combos: 
        return 3 + move_score[my_move]
    else:
        return move_score[my_move]

def play_all_games(game_pairs):
    running_score = 0
    for game in game_pairs:
        running_score += calculate_round_score(game[1], game[0])
    return running_score

print(play_all_games(data_seperated))
