def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def parse_grid(input_lines):
    grid = [list(line) for line in input_lines]
    return grid

def find_score(grid):
    # A, X = rock, B, Y = Paper, C, Z = Scissors
    scores = {'X' : 1, 'Y' : 2, 'Z' : 3}
    outcome_scores = {
        ('A', 'Y'): 6,  # Win (Rock vs Paper)
        ('B', 'Z'): 6,  # Win (Paper vs Scissors)
        ('C', 'X'): 6,  # WIn (Scissors vs Rock)
        ('C', 'Z'): 3,  # Draw (Scissors vs Scissors)
        ('A', 'X'): 3,  # Draw (Rock vs Rock)
        ('B', 'Y'): 3,  # Draw (Paper vs Paper)
        ('B', 'X'): 0,  # Lose (Paper vs Rock)
        ('A', 'Z'): 0,  # Lose (Rock vs Scissors)
        ('C', 'Y'): 0   # Lose (Scissors vs Paper)
    }
    
    total_score = 0
    for round in grid:
        opp_choice = round[0]
        my_choice = round[2]
        
        round_score = scores[my_choice] + outcome_scores[(opp_choice, my_choice)]
        total_score += round_score

    return total_score

input_lines = read_input("day2.txt")
grid = parse_grid(input_lines)
final_score = find_score(grid)
print("Total Score:", final_score)


