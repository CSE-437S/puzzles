import sys

def path(island, curr, visited):
    
    currx = curr[0]
    curry = curr[1]

    ## i did not get time to finish this but im guessing you check the four different directions you can go in / if its a slope, check if its valid and then add it to the visited set and recursively call this function on each new direction and save the max distance

    return

    

if __name__ == '__main__':
    file = open(sys.argv[1])
    island = []
    for line in file.readlines():
        line = line.strip("\n")
        island.append(list(line))

    visited = set()

    print(path(island, [0,1], visited))