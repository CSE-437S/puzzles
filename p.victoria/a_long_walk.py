import sys
sys.setrecursionlimit(20000)
file = sys.argv[1]
if(len(sys.argv) == 1):
    raise Exception("gimme file please")

c = open(file).read().split("\n")
start_index = c[0].find(".")
contents = []
for x in range(0, len(c)):
    print(c[x].split())
    contents.append([*c[x]])

# print(start_index)

def max_path(contents : list, curr_row : int, curr_col : int):
    if(curr_row >= len(contents) or curr_col >= len(contents[0]) or curr_row < 0 or curr_col < 0 or contents[curr_row][curr_col] == "#"):
        return 0
    else:
        print(curr_row, curr_col)
        current_cell = contents[curr_row][curr_col]
        past = current_cell
        if(current_cell == "^"):
            return max_path(contents, curr_row - 1, curr_col) + 1
        if(current_cell == "<"):
            return max_path(contents, curr_row, curr_col - 1) + 1
        if(current_cell == ">"):
            return max_path(contents, curr_row, curr_col + 1) + 1
        if(current_cell == "v"):
            return max_path(contents, curr_row + 1, curr_col) + 1
        print(contents[curr_row][curr_col])
        contents[curr_row][curr_col] = "#"
        dir_left = max_path(contents, curr_row, curr_col - 1)
        dir_right = max_path(contents, curr_row, curr_col + 1)
        dir_up = max_path(contents, curr_row - 1, curr_col)
        dir_down = max_path(contents, curr_row + 1, curr_col)
        contents[curr_row][curr_col] = past
        return max(dir_left, dir_right, dir_up, dir_down) + 1

res = max_path(contents, 0, start_index)
print(res - 1)