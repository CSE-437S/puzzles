def parseFunction(input):
    inputByLine = input.splitlines()
    rowLen = len(inputByLine)
    colLen = len(inputByLine[0])
    matrix = [[''] * colLen for i in range(rowLen)]
    for r, line in enumerate(inputByLine):
        for c in range(colLen):
            matrix[r][c] = line[c]
    return matrix

def longestPathAlgo(matrix):
    rowLen = len(matrix)
    colLen = len(matrix[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    maxLength = [0]
    visited = set()

    def dfs(r, c, curr):
        if r == rowLen - 1:
            maxLength[0] = max(curr, maxLength[0])
            return
        if r not in range(rowLen) or c not in range(colLen) or matrix[r][c] == "#" or (r,c) in visited:
            return

        visited.add((r,c))

        if matrix[r][c] == ".":
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                dfs(nr, nc, curr + 1)
        elif matrix[r][c] == "<":
            dfs(r, c - 1, curr + 1)
        elif matrix[r][c] == ">":
            dfs(r, c + 1, curr + 1)
        elif matrix[r][c] == "v":
            dfs(r + 1, c, curr + 1)
        elif matrix[r][c] == "^":
            dfs(r - 1, c, curr + 1)

        visited.remove((r,c))

    for i in range(colLen):
        dfs(0, i, 0)
    return maxLength[0]

resInput = '''#PUT YOUR INPUT HERE'''
resMatrix = parseFunction(resInput)
print(longestPathAlgo(resMatrix))
