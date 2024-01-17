package a_long_walk;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        StringBuilder mapBuilder = new StringBuilder();
        Scanner read = new Scanner(System.in);
        
        while (read.hasNextLine()) {
            mapBuilder.append(read.nextLine()).append("\n");
        }

        read.close();

        String mapString = mapBuilder.toString().trim();
        String[] lines = mapString.split("\n");
        char[][] map = new char[lines.length][];
        for (int i = 0; i < lines.length; i++) {
            map[i] = lines[i].toCharArray();
        }

        Algorithm algorithm = new Algorithm();

        int result = algorithm.main(map);

        System.out.println("Longest hike length: " + result);
    }
}
