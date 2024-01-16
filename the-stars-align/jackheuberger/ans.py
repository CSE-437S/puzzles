# Open file and read lines
with open("input.txt") as f:
    lines = f.readlines()

# object containing x, y, x_vel, y_vel
points = []
velocities = []

# sample input:
# position=< 54914,  32967> velocity=<-5, -3>


# Parse input
for line in lines:
    line = line.split(">")
    pos = line[0].split("<")[1].split(",")
    vel = line[1].split("<")[1].split(",")
    points.append([int(pos[0]), int(pos[1])])
    velocities.append([int(vel[0]), int(vel[1])])

# What iteration gives a grid of the smallest size
# Start at 0 iterations
areas = []
iterations = 0
for i in range(0, 999999):
    # Find the min and max x value
    min_x = min(points, key=lambda x: x[0])[0]
    max_x = max(points, key=lambda x: x[0])[0]

    # Find the min and max y value
    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key=lambda x: x[1])[1]

    # Find the width and height of the grid
    width = max_x - min_x
    height = max_y - min_y

    areas.append(width * height)

    # print("itr: " + str(i) + " width: " + str(width) + " height: " + str(height))

    # move poitns
    for j in range(0, len(points)):
        points[j][0] += velocities[j][0]
        points[j][1] += velocities[j][1]

print("min area: " + str(min(areas)) + " at iteration: " + str(areas.index(min(areas))))

