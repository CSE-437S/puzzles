with open('/Users/wtriantis/willtriantis/rock-paper-scissors/wtriantis/RPSinput.txt') as f:
    input = f.readlines()
rows=len(input)
cols=len(input[0])
score=0

for i in input:
    temp=0
    if 'X' in i:
        temp=temp+1
        if 'A' in i:
            temp=temp+3
        if 'C' in i:
            temp=temp+6

    elif 'Y' in i:
        temp=temp+2
        if 'B' in i:
            temp=temp+3
        if 'A' in i:
            temp=temp+6
    elif 'Z' in i:
        temp=temp+3
        if 'C' in i:
            temp=temp+3
        if 'B' in i:
            temp=temp+6
    score=score+temp

print(score)