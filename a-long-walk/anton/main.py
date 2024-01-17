import numpy as np
#paths: .
#forest: #
#slopes :^,>,v,<

#Goal: find longest hike, forest is unhikable, arrows force you in a direction

f = open("problem_input.txt", "r")
data = f.read()

#We can use dp algorithm that searches input. Record longest path found.
#This will explore all paths and return the longest one

problem = data.splitlines() #We can access position with row problem index and column character index in row
print(len(problem))

slope_directions = {"v": (0,-1), "<":(-1,0), "^": (0,1), ">": (1,0)}

longest_answer = np.zeros((len(problem[0]), len(problem))) #DP Table

def hiking_traverse(puzzle, x, y, depth, visited_paths):
    current_char = puzzle[y][x]
    print(visited_paths)
    #Base cases
    if f"{x}{y}" in visited_paths:
        return -1
    if x < 0 or x >= len(puzzle[y]):
        return -1
    if y < 0 or y >= len(puzzle):
        return -1
    if current_char == "#":
        return -1
    if longest_answer[x][y] > 0:
        return longest_answer[x][y] #Duplicate subproblem

    if current_char in slope_directions.keys():
        x_movement = slope_directions[current_char][0]
        y_movement = slope_directions[current_char][1]
        longest_answer[x][y] = hiking_traverse(puzzle, x + x_movement, y + y_movement, depth + 1, (x,y))
        return 1 + longest_answer[x][y]
    else:
        left_paths = visited_paths.copy()
        left_paths.append(f"{x}{y}")
        go_left = hiking_traverse(puzzle, x - 1, y + 0, depth + 1, left_paths)
        right_paths = visited_paths.copy()
        right_paths.append(f"{x}{y}")
        go_right = hiking_traverse(puzzle, x + 1, y + 0, depth + 1, right_paths)
        up_paths = visited_paths.copy()
        up_paths.append(f"{x}{y}")
        go_up = hiking_traverse(puzzle, x, y + 1, depth + 1, up_paths)
        down_paths = visited_paths.copy()
        down_paths.append(f"{x}{y}")
        go_down = hiking_traverse(puzzle, x, y - 1, depth + 1, down_paths)

        longest_answer[x][y] = max(go_left, go_right, go_up, go_down)
        return longest_answer[x][y]

visited_paths = []
answer = hiking_traverse(problem, 1, 0, 0, visited_paths)
print(problem[0][1])
print(longest_answer[0][1])
print(answer)


