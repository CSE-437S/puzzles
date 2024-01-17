import re

def extract_values(line):
    # -? for optional negative sign
    # \d+ for digits
    numbers = [int(num) for num in re.findall(r"-?\d+", line)]
    return numbers

positions = []
velocities = []
with open("the-stars-align/Test.txt") as file: 
    for line in file: 
        x, y, vx, vy = extract_values(line)
        positions.append((x, y))
        velocities.append((vx, vy))
        

min_x = min(pos[0] for pos in positions)
min_y = min(pos[1] for pos in positions)

# adjust so there are no negatives (means we can easily make a 2D array)
positions = list(map(lambda x: (x[0] - min_x, x[1]), positions))
positions = list(map(lambda x: (x[0], x[1] - min_y), positions))

max_x = max(pos[0] for pos in positions)
max_y = max(pos[1] for pos in positions)
# Create a 2D grid with periods
grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# Mark positions with hashtags
for pos in positions:
    x, y = pos
    grid[max_y - y][x] = '#'

for row in grid:
    print(' '.join(row))

for i in range(3): 
    for i, pos in enumerate(positions): 
        vx, vy = velocities[i]
        positions[i] = pos[0] + vx, pos[1] + vy
    
    # reset grid
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for pos in positions:
        x, y = pos
        grid[max_y - y][x] = '#'

    # Print the grid
    for row in grid:
        print(' '.join(row))