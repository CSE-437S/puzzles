import os

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)

f = open("input.txt")

text = f.read()

matrix = [[*row] for row in text.split()]

row = 1
col = 1

print(len(matrix))
        

def walk(row, col):
    
    """ invalid paths """
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0
    
    curr = matrix[row][col]
    
    matrix[row][col] = "#"
    
    path_len = 0
    
    if curr == "#":
        return 0
    
    elif curr == "^":
        path_len = 1 + walk(row-1, col)
        
    elif curr == "<":
        path_len = 1 + walk(row, col-1)
        
    elif curr == ">":
        path_len = 1 + walk(row, col+1)
    
    elif curr == "v":
        path_len = 1 + walk(row+1, col)
        
    elif curr == ".":
        left_right = max(walk(row, col-1), walk(row, col+1))
        up_down = max(walk(row+1, col), walk(row-1, col))
        path_len = 1 + max(left_right, up_down)
        
    matrix[row][col] = curr    
    
    return path_len

print(walk(1,1))