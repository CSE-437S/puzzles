import java.io.*;
import java.util.*;
import java.util.regex.*;

class Point {
    int x, y;
    int vx, vy;

    Point(int x, int y, int vx, int vy) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
    }

    void move() {
        x += vx;
        y += vy;
    }
}

public class StarMessage {
    public static void main(String[] args) {
        List<Point> points = new ArrayList<>();
        try {
            points = parseInput("input.txt");
        } catch (IOException e) {
            System.err.println("Error reading input file: " + e.getMessage());
            return;
        }

    }

    private static List<Point> parseInput(String filename) throws IOException {
        List<Point> points = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line;
        Pattern pattern = Pattern.compile("position=<\\s*(-?\\d+),\\s*(-?\\d+)> velocity=<\\s*(-?\\d+),\\s*(-?\\d+)>");
        while ((line = reader.readLine()) != null) {
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                int x = Integer.parseInt(matcher.group(1));
                int y = Integer.parseInt(matcher.group(2));
                int vx = Integer.parseInt(matcher.group(3));
                int vy = Integer.parseInt(matcher.group(4));
                points.add(new Point(x, y, vx, vy));
            }
        }
        reader.close();
        return points;
    }

}
