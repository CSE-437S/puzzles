import matplotlib.pyplot as plt
positions = []
velocities = []
delimiters = ["<"]
for line in open("input.txt", "r"):
    split = " ".join(line.split("<"))
    result = split.split()
    
    #positions.append(split[0])
    positions.append([result[1][:-1], result[2][:-1]])
    velocities.append([result[4][:-1], result[5][:-1]])

for coords in positions:
    x = coords[0]
    y = coords[1]
plt.scatter(x,y)
plt.show()
