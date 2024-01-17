
# it just wants to find out how many steps, not to retrace the path
# therefore, we can do a bfs 


# idea: do a BFS (recursive) and keep track of the longest path that gets to finish

dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]


# turns out input into a 2D array
def parse_input(grid):
    grid = grid.split('\n')
    grid = [list(row) for row in grid]
    # print("INPUT PARSED")
    # print(grid)
    return grid

# check that indices are valid
def verify_indices(r, c, grid):
    return r > -1 and r < len(grid) and c > -1 and c < len(grid[0])

def solution(grid):
    grid = parse_input(grid) 

    # find the starting point (NOTE points are tuple(row, col)))
    starting_point = (0, grid[0].index('.'))

    LONGEST_PATH_LENGTH = 0
    CTR = 0

    def bfs(point, path_length, visited_set):
        nonlocal LONGEST_PATH_LENGTH

        r = point[0]
        c = point[1]
        cur_symbol = grid[r][c]

        # check all cases where we can't explore anymore
        if not verify_indices(r, c, grid) or point in visited_set or cur_symbol == '#':
            return 

        visited_set.add(point)
        path_length += 1

        # check if we're finished
        if r == len(grid) - 1 and cur_symbol == '.':
            LONGEST_PATH_LENGTH = max(LONGEST_PATH_LENGTH, path_length)
            return
        
        # if we are on a slope, only explore in the direction of the slope
        new_point = None
        if cur_symbol == '^':
            new_point = (r-1, c)
            bfs((r-1, c), path_length, visited_set.copy())
        elif cur_symbol == '>':
            new_point = (r, c+1)
            bfs((r, c+1), path_length, visited_set.copy())
        elif cur_symbol == 'v':
            new_point = (r+1, c)
            bfs((r+1, c), path_length, visited_set.copy())
        elif cur_symbol == '<':
            new_point = (r, c-1)
            bfs((r, c-1), path_length, visited_set.copy())

        # else we explore in all directions
        for d in dirs:
            new_point = (r + d[0], c + d[1])
            bfs(new_point, path_length, visited_set.copy())
        
        return
    
    # make sure to pass in COPIES of the visited set
    
    bfs(starting_point, 0, set())
    return LONGEST_PATH_LENGTH
    

# There's a map of nearby hiking trails (your puzzle input) that indicates paths (.), forest (#), and steep slopes (^, >, v, and <)

# if you step onto a slope tile, your next step must be downhill (in the direction the arrow is pointing)
    # basically, you can normally go in any diretion, but for this one you can only go in the direction of the arrow

# never step on same tile twice, GOAL is to find the longest possible hike
    # will go from the single path tile in the top row to the single path tile in the bottom row

if __name__ == '__main__':
    with(open('a-long-walk/ben.j.mueller/miniInput.txt', 'r')) as f:
        grid = f.read()
        longestLength = solution(grid)
        print(longestLength)
