import sys

choice_val = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y':2, 'Z':3}
total_score = 0

fileName = sys.argv[1]

def det_outcome(x, y):
  if x == y:
    return 3
  elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
    return 6
  else:
    return 0
  
with open(fileName, 'r') as file:

  for line in file:
    total_score += choice_val[line[2]]
    total_score += det_outcome(choice_val[line[0]], choice_val[line[2]])



print(total_score)