
def main():
    input = open('./input.txt', 'r')      #https://docs.python.org/3/library/csv.html
    theirMoves = []
    yourMoves = []
    theirMove = 'A'
    yourMove = 'A'
    for line in input:
        print(line)
        theirMove = line[0]
        yourMove = line[1]
        theirMove[line] = theirMove
        yourMove[line] = yourMove

main()