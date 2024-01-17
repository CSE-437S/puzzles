with open('/Users/wtriantis/willtriantis/wtriantis/map.txt') as f:
    board = f.readlines()
rows=len(board)
cols=len(board[0])
print(rows)
print(cols)
maxcount=0
for x in range(rows):
    for y in range(cols):
        count=0
        xx=x
        yy=y
        while board[xx][yy]=='<' or '^' or '>' or 'v' or '.':
            if xx==rows-2 and yy==cols-1: #end point
                if count>maxcount:
                    maxcount=count
            if board[xx][yy]=='<':
                yy=yy-1
                count+1
            elif board[xx][yy]=='^':
                xx=xx-1
                count+1
            elif board[xx][yy]=='>':
                yy=yy+1
                count+1
            elif board[xx][yy]=='v':
                xx=xx+1
                count+1
            elif board[xx+1][yy]=='.':
                xx=xx+1
                count+1
            elif board[xx][yy+1]=='.':
                yy=yy+1
                count+1

        