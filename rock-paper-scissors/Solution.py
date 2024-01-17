import os

totalScore = 0
charToScore = {"A":1, "B":2, "C":3}
winScore, drawScore, lossScore = 6, 3, 0
# A, X = rock
# B, Y = paper
# C, Z = scissors
opponentMoveToOurMove = {"X":"A", "Y":"B", "Z":"C"}
#with open("rock-paper-scissors/Test.txt", "r") as file: 
with open("rock-paper-scissors/Problem.txt", "r") as file: 
    for line in file: 
        opponentMove, ourMove = line[0], opponentMoveToOurMove[line[2]]
        # 6 = win, 3 = draw, 0 = loss
        outcome = float("inf")

        # it's a draw
        if opponentMove == ourMove: 
            outcome = 3
        else: 
            # cases where opponent wins

            # rock beats scissors
            # paper beats rock
            # scissors beats paper
            if((opponentMove == "A" and ourMove == "C") or 
               (opponentMove == "B" and ourMove == "A") or 
               (opponentMove == "C" and ourMove == "B")): 
                outcome = 0
            # case where we win
            else: 
                outcome = 6
        totalScore += charToScore[ourMove] + outcome

print("Score:", totalScore)
        

