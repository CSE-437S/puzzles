import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

def calcTotalScore():
    stratguidefile = input("Please input the absolute file path of the file")
    stratguide = open(stratguidefile, "r")
    lines = stratguide.readlines()

    totalScoreCount = 0

    for line in lines:
        oppVal = line[0]
        myVal = line[2]
        if oppVal == "A":
            if myVal == "X":
                totalScoreCount +=4
            elif myVal == "Y":
                totalScoreCount +=8
            elif myVal == "Z":
                totalScoreCount +=3
        elif oppVal == "B":
            if myVal == "X":
                totalScoreCount +=1
            elif myVal == "Y":
                totalScoreCount +=5
            elif myVal == "Z":
                totalScoreCount +=9
        elif oppVal == "C":
            if myVal == "X":
                totalScoreCount +=7
            elif myVal == "Y":
                totalScoreCount +=2
            elif myVal == "Z":
                totalScoreCount +=6

    return totalScoreCount



print(calcTotalScore())
