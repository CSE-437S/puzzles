import os

f = open("input.txt")

text = f.read()

# print(text)

matrix = [[*row] for row in text.split()]

row = 1
col = 1

print(len(matrix))

"""
space = no restriction
all others indicated by arrow
"""
restriction = " "

cache = {}

def max_of_dir(row, col, restriction):
    loc = str(row) + " " + str(col)
    
    if restriction != ".":
        if restriction ==  "^":
            cache[loc] = walk(row-1, col)
            return cache[loc]
        elif restriction == ">":
            cache[loc] = walk(row, col+1)
            return cache[loc]
        elif restriction == "<":
            cache[loc] = walk(row, col-1)
            return cache[loc]
        elif restriction == "v":
            cache[loc] = walk(row+1, col)
            return cache[loc]
    else:
        
        lr = max(walk(row, col-1), walk(row, col+1))
        ud = max(walk(row+1, col), walk(row-1, col))
        
        return max(lr, ud)
        

def walk(row, col):
    
    """ invalid paths """
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0
    
    curr = matrix[row][col]
    
    if curr == "#":
        return 0
    
    else:
        
        matrix[row][col] = "#"
        
        path_len = 1 + max_of_dir(row,col, curr)
        
        matrix[row][col] = curr
        
    return path_len




# def search():
#     stack = []
    
#     max_len = 0

#     stack.append([1,1])
    
#     while not len(stack) == 0:
#         coords = stack.pop()
        
#         row = coords[0]
#         col = coords[1]
        
#         if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
#             max_len = max(max_len, len(stack))
            
#             continue
        
#         if matrix[row][col] != "#":
            
#             curr = matrix[row][col]
#             matrix[row][col] = "#"
#             if curr == ".":
#                 stack.append([row-1, col])
#                 stack.append([row+1, col])
#                 stack.append([row, col-1])
#                 stack.append([row, col+1])
#             elif curr == "^":
#                 stack.append([row-1, col])
#             elif curr == ">":
#                 stack.append([row, col+1])
#             elif curr == "<":
#                 stack.append([row, col-1])
#             elif curr == "v":
#                 stack.append([row+1, col])
                
#     return max_len
        
        
# print(search())


    

walk(1,1)