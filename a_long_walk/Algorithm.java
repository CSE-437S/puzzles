package a_long_walk;

import java.util.HashSet;
import java.util.Set;

class Algorithm {
    public int main(char[][] map) {
        // First, find the starting position
        char[] startingRow = map[0];
        int startingPoint = 0;
        Set<String> visited = new HashSet<>();

        for (int i = 0; i < startingRow.length; i++) {
            if (map[0][i] == '.') {
                startingPoint = i;
                break; 
            }
        }

        return DFS(map, 0, startingPoint, 0, visited);
    }

    public int DFS(char[][] map, int row, int col, int length, Set<String> visited) {
        if (row < 0 || row == map.length || col < 0 || col == map[0].length) {
            return length;
        }

        if (map[row][col] == '#' || visited.contains(row + "," + col)) {
            return length;
        }

        visited.add(row + "," + col);

        if (map[row][col] == '^') {
            return DFS(map, row - 1, col, length + 1, visited);
        }
        if (map[row][col] == '<') {
            return DFS(map, row, col - 1, length + 1, visited);
        }
        if (map[row][col] == '>') {
            return DFS(map, row, col + 1, length + 1, visited);
        }
        if (map[row][col] == 'v') {
            return DFS(map, row + 1, col, length + 1, visited);
        }
        if (map[row][col] == '.') {
            int up = DFS(map, row - 1, col, length + 1, visited);
            int down = DFS(map, row + 1, col, length + 1, visited);
            int left = DFS(map, row, col - 1, length + 1, visited);
            int right = DFS(map, row, col + 1, length + 1, visited);
            visited.remove(row + "," + col); // Backtrack

            return Math.max(Math.max(up, down), Math.max(left, right));
        }

        return 0; // Default return statement (should not reach here)
    }
}
