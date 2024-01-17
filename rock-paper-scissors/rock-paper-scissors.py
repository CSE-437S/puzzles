player_dict = {'X': 1,
               'Y': 2,
               'Z': 3}
opp_dict = {'A': 1,
            'B': 2,
            'C': 3}
#Rock = 1, Paper = 2, Scissors = 3
#Paper > Rock, Scissors > Paper, Rock > Scissors
cum_points = 0
with open('/Users/cilantro/puzzles/rock-paper-scissors/input.txt') as f:
    for line in f:
        move = line.strip().split(' ')
        opp_move = opp_dict[move[0]]
        player_move = player_dict[move[1]]
        #tie
        if opp_move == player_move:
            outcome = 3
        #player lose
        elif (opp_move == 1 and player_move == 3) or opp_move > player_move:
            outcome = 0
        #player win
        elif  (opp_move == 3 and player_move == 1) or opp_move < player_move:
            outcome = 6
        points = outcome + player_move
        cum_points += points

print(cum_points)