
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
    if theirMove == 'A':
    
    print(sum)

main()