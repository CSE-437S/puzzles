import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Longest {
    private static final char PATH = '.';
    private static final char TREE = '#';
    private static final Map<Character, int[]> DIRECTIONS = Map.of(
            '^', new int[] { -1, 0 },
            '>', new int[] { 0, 1 },
            'v', new int[] { 1, 0 },
            '<', new int[] { 0, -1 });

    public static void main(String[] args) throws IOException {
        List<String> map = Files.readAllLines(Paths.get("walk_input.txt"));
        int longest = findLongest(map);
        System.out.println("The longest walk is " + longest + " steps long.");
    }

    private static int findLongest(List<String> map) {
        int rows = map.size();
        int cols = map.get(0).length();
        boolean[][] visited = new boolean[rows][cols];
        int startY = map.get(0).indexOf(PATH);

        return dfs(map, 0, startY, visited, 1) - 1;
    }

    private static int dfs(List<String> map, int x, int y, boolean[][] visited, int length) {
        if (x == map.size() - 1 && map.get(x).charAt(y) == PATH) {
            return length;
        }

        visited[x][y] = true;
        int maxLen = 0;

        if (DIRECTIONS.containsKey(map.get(x).charAt(y))) {
            int[] dir = DIRECTIONS.get(map.get(x).charAt(y));
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (isValid(nx, ny, visited, map)) {
                maxLen = Math.max(maxLen, dfs(map, nx, ny, visited, length + 1));
            }
        } else {
            for (int[] dir : DIRECTIONS.values()) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (isValid(nx, ny, visited, map)) {
                    maxLen = Math.max(maxLen, dfs(map, nx, ny, visited, length + 1));
                }
            }
        }

        visited[x][y] = false;
        return maxLen;
    }

    private static boolean isValid(int x, int y, boolean[][] visited, List<String> map) {
        return x >= 0 && x < map.size() && y >= 0 && y < map.get(0).length() && !visited[x][y]
                && map.get(x).charAt(y) != TREE;
    }
}