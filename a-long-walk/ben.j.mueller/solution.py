
# it just wants to find out how many steps, not to retrace the path
# therefore, we can do a bfs 

def solution():
    pass

# There's a map of nearby hiking trails (your puzzle input) that indicates paths (.), forest (#), and steep slopes (^, >, v, and <)

# if you step onto a slope tile, your next step must be downhill (in the direction the arrow is pointing)
    # basically, you can normally go in any diretion, but for this one you can only go in the direction of the arrow

# never step on same tile twice, GOAL is to find the longest possible hike
    # will go from the single path tile in the top row to the single path tile in the bottom row

if __name__ == '__main__':
    print("Hello, world!")