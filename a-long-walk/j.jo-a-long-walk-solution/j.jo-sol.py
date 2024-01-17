
def longest_hike(map_data):
    rows = len(map_data)
    cols = len(map_data[0])

    # slopes
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    # DFS function to explore the map
    def dfs(x, y, visited):
        if x == rows - 1:  # reached the bottom row
            return len(visited)

        max_length = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # check all directions
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and map_data[nx][ny] != '#' and (nx, ny) not in visited:
                # follow the slope direction
                if map_data[x][y] in directions:
                    dir_x, dir_y = directions[map_data[x][y]]
                    if dir_x != dx or dir_y != dy:
                        continue

                visited.add((nx, ny))
                max_length = max(max_length, dfs(nx, ny, visited))
                visited.remove((nx, ny))

        return max_length

    # find the starting position in the top row
    start_pos = [(0, i) for i, cell in enumerate(map_data[0]) if cell == '.'][0]

    # DFS from the initial position
    return dfs(start_pos[0], start_pos[1], set([start_pos]))




def main():

    testMap = [
        "#.#####################",
        "#.......#########...###",
        "#######.#########.#.###",
        "###.....#.>.>.###.#.###",
        "###v#####.#v#.###.#.###",
        "###.>...#.#.#.....#...#",
        "###v###.#.#.#########.#",
        "###...#.#.#.......#...#",
        "#####.#.#.#######.#.###",
        "#.....#.#.#.......#...#",
        "#.#####.#.#.#########v#",
        "#.#...#...#...###...>.#",
        "#.#.#v#######v###.###v#",
        "#...#.>.#...>.>.#.###.#",
        "#####v#.#.###v#.#.###.#",
        "#.....#...#...#.#.#...#",
        "#.#########.###.#.#.###",
        "#...###...#...#...#.###",
        "###.###.#.###v#####v###",
        "#...#...#.#.>.>.#.>.###",
        "#.###.###.#.###.#.#v###",
        "#.....###...###...#...#",
        "#####################.#"
    ]

    result = longest_hike(testMap)
    print(f"Longest hike length for the given map: {result}")

if __name__ == '__main__':
    main()