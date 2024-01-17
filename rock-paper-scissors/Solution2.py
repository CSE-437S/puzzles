import os

totalScore = 0
charToScore = {"A":1, "B":2, "C":3}
winScore, drawScore, lossScore = 6, 3, 0
# A, X = rock
# B, Y = paper
# C, Z = scissors
opponentMoveToOurMove = {"X":"LOSE", "Y":"DRAW", "Z":"WIN"}
# with open("rock-paper-scissors/Test.txt", "r") as file: 
with open("rock-paper-scissors/Problem.txt", "r") as file: 
    for line in file: 
        opponentMove, whatWeMustDo = line[0], opponentMoveToOurMove[line[2]]
        # 6 = win, 3 = draw, 0 = loss
        outcome = float("inf")
        ourMove = float("inf")
        if whatWeMustDo == "WIN": 
            outcome = 6
            if opponentMove == "A": 
                ourMove = "B"
            elif opponentMove == "B": 
                ourMove = "C"
            else: 
                ourMove = "A"

        elif whatWeMustDo == "DRAW": 
            outcome = 3
            ourMove = opponentMove # just move what the opponent moves
        else: 
            outcome = 0
            if opponentMove == "A": 
                ourMove = "C"
            elif opponentMove == "B": 
                ourMove = "A"
            else: 
                ourMove = "B"
        # figure out move we must make
        totalScore += charToScore[ourMove] + outcome

print("Score:", totalScore)
        

