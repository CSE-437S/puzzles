import sys

def score(file):
    d_player = {"X": 1, "Y": 2, "Z": 3}
    d_elf = {"A": "X", "B": "Y", "C": "Z"}
    d_win = {"A": "Y", "B": "Z", "C": "X"}
    f = open(file)
    total = 0
    for line in f.readlines():
        line = line.strip("\n")
        elf = str(line.split(" ")[0])
        player = str(line.split(" ")[-1])
        
        total += d_player[player]

        if player == d_elf[elf]:
            total += 3
        elif player == d_win[elf]:
            total += 6
    
    return total

if __name__ == '__main__':
    print(score(sys.argv[1]))