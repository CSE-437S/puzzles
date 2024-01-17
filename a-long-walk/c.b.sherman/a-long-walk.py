# turn the input into a 2d array
# dfs the 2d array
# dfs conditions: return if character is # or already visited, move in directions of slopes, calculate maximum length

# is that even close to right??? i guess i have to save the path as well to see if the element im on is already visited
# do people actually know how to do this??? i didnt know i had to know how to leetcode for this class

# to be entirely honest i have absolutely zero clue how to implement any of this

arr = []

with open("input.txt", "r") as file:
    for line in file:
        split_array = line.split()
        for row in split_array:
            arr.append(list(row))

print(arr)

# okay, we've made a 2d array! yay! (this is probably the only thing im able to do)

visited = []
path_length = 0

def dfs(row, col, visited):
    if arr[row][col] == '#':
        return
    if (row, col) in visited:
        return
    # mark coordinate as visited and increment path length
    visited.append((row, col))
    path_length += 1
    # dfs to neighboring cells
    up_neighbor = dfs(row - 1, col, visited)
    down_neighbor = dfs(row + 1, col, visited)
    left_neighbor = dfs(row, col - 1, visited)
    right_neighbor = dfs(row, col + 1, visited)

    

# uhhhhhhh


