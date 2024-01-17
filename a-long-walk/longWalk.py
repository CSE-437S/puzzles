


directions = {
    '>': [1, 0],
    '<': [-1, 0],
    '^': [0, 1],
    'v': [0, -1],
    '.': [[1,0], [-1,0], [0,1], [0,-1]],
}


class Graph:
    def __init__(self, data):
        self.data = data
        self.width = len(data[0])
        self.height = len(data)
        self.graph = self.makeGraph()

    def makeGraph(self):
        graph = {}
        for y in range(self.height):
            for x in range(self.width):
                if self.data[y][x] != '#':
                    graph[(x,y)] = self.nextPath((x,y))
        return graph

    def nextPath(self, start):
        x, y = start
        path = []
        for dx, dy in directions[self.data[y][x]]:
            if 0 <= x+dx < self.width and 0 <= y+dy < self.height:
                if self.data[y+dy][x+dx] != '#':
                    path.append((x+dx, y+dy))
        return path

    def __getitem__(self, key):
        return self.graph[key]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.data])

    def __repr__(self):
        return str(self)


def findPath(graph, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        elif node not in visited:
            for adjacent in graph[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.add(node)

    