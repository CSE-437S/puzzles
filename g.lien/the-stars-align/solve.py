def visualizeStars():
    #stratguidefile = input("Please input the absolute file path of the file")
    star = open("/Users/geoffreylien/git/CSE437S/puzzles/g.lien/the-stars-align/star_positions.txt", "r")
    lines = star.readlines()

    for line in lines:
        x =line.strip()
        print(x)

visualizeStars()