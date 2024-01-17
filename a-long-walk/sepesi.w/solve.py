PATH = "input.txt"

# Board class to represent hike
class Board:
    def __init__(self):
        self.board = []

    def print_board(self):
        for row in self.board:
            for char in row:
                print(char, end='')
            print()

    def load_board(self, filename):
        with open(filename) as f:
            for y, line in enumerate(f):
                row = []
                for x, char in enumerate(line):
                    if char == '\n':
                        continue
                    else:
                        row.append(char)
                self.board.append(row)

    def remove_spot(self, x, y):
        self.board[x][y] = 'O'

    def set_starting_spot(self, x, y):
        self.board[x][y] = 'S'

# player class for traversal
class Player:
    def __init__(self, board):
        # deep copy board
        self.original_board = []
        for row in board.board:
            self.original_board.append(row.copy())
        self.board = board
        self.x = None
        # parse the board for the only "." tile in the top row, which is our starting position
        for x, row in enumerate(self.board.board):
            for y, char in enumerate(row):
                if char == '.':
                    self.x = x
                    self.y = y
                    self.board.set_starting_spot(x,y)
                    return
        if self.x is None:
            raise Exception("couldn't find starting position")
        
    def print_original_board(self):
        for row in self.original_board:
            for char in row:
                print(char, end='')
            print()
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_position_and_wipe_current(self, x, y):
        orig_at_cur_pos = self.original_board[self.x][self.y]
        self.board.board[self.x][self.y] = orig_at_cur_pos
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y
    
    def get_distance_to_exit(self):
        # manhattan heuristic to exit (only . in bottom row)
        x_dist = len(self.board.board) - 1 - self.x
        exit_y = None
        for y, char in enumerate(self.board.board[-1]):
            if char == '.':
                exit_y = y
        if exit_y is None:
            raise Exception("couldn't find exit")
        y_dist = abs(exit_y - self.y)
        return x_dist + y_dist
        
    def get_moves(self):
        # if on ., we can move in any direction that isnt a # or an S or an O
        # if on an arrow, we can move in the direction of the arrow
        # if on the bottom row, we can move to 'END'
        moves = []
        if self.x == len(self.board.board) - 1:
            moves.append('END')
            return moves
        if self.board.board[self.x][self.y] == '.' or self.board.board[self.x][self.y] == 'S' or self.board.board[self.x][self.y] == 'O':
            if self.board.board[self.x-1][self.y] != '#' and self.board.board[self.x-1][self.y] != 'O' and self.board.board[self.x-1][self.y] != 'S' and self.x != 0 and self.board.board[self.x-1][self.y] != 'v':
                moves.append('UP')
            if self.board.board[self.x][self.y-1] != '#' and self.board.board[self.x][self.y-1] != 'O' and self.board.board[self.x][self.y-1] != 'S' and self.y != 0 and self.board.board[self.x][self.y-1] != '>':
                moves.append('LEFT')
            if self.board.board[self.x][self.y+1] != '#' and self.board.board[self.x][self.y+1] != 'O' and self.board.board[self.x][self.y+1] != 'S' and self.y != len(self.board.board[0]) - 1 and self.board.board[self.x][self.y+1] != '<':
                moves.append('RIGHT')
            if self.board.board[self.x+1][self.y] != '#' and self.board.board[self.x+1][self.y] != 'O' and self.board.board[self.x+1][self.y] != 'S' and self.x != len(self.board.board) - 1 and self.board.board[self.x+1][self.y] != '^':
                moves.append('DOWN')
        elif self.board.board[self.x][self.y] == '^':
            moves.append('UP')
        elif self.board.board[self.x][self.y] == '<':
            moves.append('LEFT')
        elif self.board.board[self.x][self.y] == '>':
            moves.append('RIGHT')
        elif self.board.board[self.x][self.y] == 'v':
            moves.append('DOWN')
        else:
            raise Exception("invalid character on board")
        
        return moves
    
    def get_moves_dry(self):
        # same as get moves, but no restraints on arrow characters
        moves = []
        arrow_chars = ['^', '<', '>', 'v']
        if self.x == len(self.board.board) - 1:
            moves.append('END')
            return moves
        if self.board.board[self.x][self.y] == '.' or self.board.board[self.x][self.y] == 'S' or self.board.board[self.x][self.y] == 'O' or self.board.board[self.x][self.y] in arrow_chars:
            if self.board.board[self.x-1][self.y] != '#' and self.board.board[self.x-1][self.y] != 'O' and self.board.board[self.x-1][self.y] != 'S' and self.x != 0:
                moves.append('UP')
            if self.board.board[self.x][self.y-1] != '#' and self.board.board[self.x][self.y-1] != 'O' and self.board.board[self.x][self.y-1] != 'S' and self.y != 0:
                moves.append('LEFT')
            if self.board.board[self.x][self.y+1] != '#' and self.board.board[self.x][self.y+1] != 'O' and self.board.board[self.x][self.y+1] != 'S' and self.y != len(self.board.board[0]) - 1:
                moves.append('RIGHT')
            if self.board.board[self.x+1][self.y] != '#' and self.board.board[self.x+1][self.y] != 'O' and self.board.board[self.x+1][self.y] != 'S' and self.x != len(self.board.board) - 1:
                moves.append('DOWN')

        return moves


    def print_board(self):
        self.board.print_board()

    def move(self, direction):
        if direction == 'UP':
            self.x -= 1
        elif direction == 'DOWN':
            self.x += 1
        elif direction == 'LEFT':
            self.y -= 1
        elif direction == 'RIGHT':
            self.y += 1
        elif direction == 'END':
            raise Exception("reached end of board")
        else:
            raise Exception("invalid direction")
        
        try:
            self.board.remove_spot(self.x, self.y)
        except Exception as e: 
            self.print_board()
            print(self.x, self.y)
            raise Exception(e)

# we seek to maximize the number of steps taken to get from the starting position to END
# to find the longest path, we can use a depth first search. but search over just the number of steps, not the path itself. 

def dfs(player, num_steps):
    if num_steps > 100000:
        raise Exception("too many steps")
    moves = player.get_moves()
    if 'END' in moves:
        if num_steps == 154:
            player.print_board()
        return num_steps
    max_steps = 0
    if len(moves) == 0:
        return -100000
    for move in moves:
        coords = player.get_position()
        player.move(move)
        max_steps = max(max_steps, dfs(player, num_steps + 1))
        player.set_position_and_wipe_current(coords[0], coords[1])
    return max_steps

board = Board()
board.load_board(PATH)
player = Player(board)

print("Part I:")
print(dfs(player, 0))

print("Part II:")
print("NOT COMPLETED")