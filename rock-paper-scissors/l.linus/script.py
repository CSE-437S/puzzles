#============ PART ONE =================

with open("input.txt") as f:
    score = 0
    for line in f:
        line_text = line.strip()
        move1 = line_text[:1]
        move2 = line_text[2:]
        if move2 == 'X':
            score += 1
            if move1 == 'A':
                score += 3
            elif move1 == 'C':
                score += 6
        if move2 == 'Y':
            score += 2
            if move1 == 'B':
                score += 3
            elif move1 == 'A':
                score += 6
        if move2 == 'Z':
            score += 3
            if move1 == 'C':
                score += 3
            elif move1 == 'B':
                score += 6

        print(line_text)
    print(score)



#============ PART TWO =================

# with open("input.txt") as f:
#     score = 0
#     for line in f:
#         line_text = line.strip()
#         move1 = line_text[:1]
#         move2 = line_text[2:]
#         if move2 == 'X':
#             if move1 == 'A':
#                 score += 3
#             elif move1 == 'B':
#                 score += 1
#             elif move1 == 'C':
#                 score += 2
#         if move2 == 'Y':
#             score += 3
#             if move1 == 'A':
#                 score += 1
#             elif move1 == 'B':
#                 score += 2
#             elif move1 == 'C':
#                 score += 3
#         if move2 == 'Z':
#             score += 6
#             if move1 == 'A':
#                 score += 2
#             elif move1 == 'B':
#                 score += 3
#             elif move1 == 'C':
#                 score += 1

#         print(line_text)
#     print(score)