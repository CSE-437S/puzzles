
def main():
    input = open('rock-paper-scissors\joey\input.txt', 'r')      #https://docs.python.org/3/library/csv.html
    theirList = []
    yourList = []
    theirMove = ''#BLANK CHAR
    yourMove = ''
    for line in input:
        theirMove = line[0]
        yourMove = line[1]
        theirList.append(theirMove)
        yourList.append(yourMove)
    counter(theirList, yourList)

def counter(theirList, yourList):
    sum = 0
    theirMove = ''
    yourMove = ''
    shapeScores = {
        'X':1,
        'Y':2,
        'Z':3
    }
    '''
    A Y
    B X
    C Z
    '''
    for i in range(len(theirList)):
        theirMove = theirList[i]
        yourMove = yourList[i]
        if yourMove == 'X':
        sum+=1
        elif yourMove == 'Y':
            sum+=2
        elif yourMove == 'Z':
            sum+=3

        if theirMove == 'A':
            if yourMove == 'Y':
                sum+=6
            elif yourMove == 'A':
                sum+=3
        elif theirMove == 'B':
            if yourMove == 'X':
                sum+=6
            elif yourMove == 'B':
                sum+=3
        elif theirMove == 'C':
            if yourMove == 'Z':
                sum+=6
            elif yourMove == 'C':
                sum+=3

    

    print(sum)

main()