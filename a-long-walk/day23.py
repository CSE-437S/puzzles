def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def parse_grid(input_lines):
    grid = [list(line) for line in input_lines]
    return grid

def is_valid_move(grid, x, y, visited):
    # Check if (x, y) is within the grid boundaries
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False

    # Check if the tile is a forest (#) or has been visited before
    if grid[x][y] == '#' or (x, y) in visited:
        return False

    return True

def dfs(grid, x, y, visited, current_length, max_length):
    # Check if the current position is valid
    if not is_valid_move(grid, x, y, visited):
        return
    
    if x == len(grid) - 1:
        max_length[0] = max(max_length[0], current_length)
        return

    # Mark the current position as visited
    visited.add((x, y))
    current_length += 1

    # Update the maximum path length
    max_length[0] = max(max_length[0], current_length)

    # If the current tile is a slope, determine the next position
    if grid[x][y] in ['>', '<', 'v', '^']:
        nx, ny = next_position(x, y, grid[x][y])
        if is_valid_move(grid, nx, ny, visited):
            dfs(grid, nx, ny, visited, current_length, max_length)
    else:
        # If it's a flat tile, explore all four adjacent tiles
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # right, left, down, up
            nx, ny = x + dx, y + dy
            if is_valid_move(grid, nx, ny, visited):
                dfs(grid, nx, ny, visited, current_length, max_length)

    # Backtrack: unmark the current position as visited
    visited.remove((x, y))

def next_position(x, y, tile):
    # Return the next position based on the slope direction
    directions = {'>': (1, 0), '<': (-1, 0), 'v': (0, -1), '^': (0, 1)}
    dx, dy = directions[tile]
    return x + dx, y + dy
    

def find_longest_path(grid):
    max_length = [0]
    visited = set()
    for y in range(len(grid[0])):
        if grid[0][y] == '.':
            dfs(grid, 0, y, visited, 0, max_length)
    return max_length[0]

input_lines = read_input("adventday23.txt")
grid = parse_grid(input_lines)
longest_path = find_longest_path(grid)
print("Longest Path Length:", longest_path)

