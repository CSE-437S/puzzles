def isForest(tile):
    if tile == "#":
        return True
    else:
        return False

def isPath(tile):
    if tile == ".":
        return True
    else:
        return False
    
def isSlope(tile):
    if tile == "<" or tile ==">" or tile=="v" or tile =="^":
        return True
    else:
        return False
    
def process_board(board):
    for i in board:
        for j in i:
            print( j , end ="")
        print()
        
            
def get_board():
    board = []
    file = open( "input.txt", "r")
    for line in file:
        line = line.strip()
        arr = [char for char in line]
        board.append(arr)
    return board

def main():
    board = get_board()
    process_board(board)
    

if __name__ == "__main__":
    main()