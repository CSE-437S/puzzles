import java.io.*;
import java.nio.file.*;
import java.util.*;

public class RockPaperScissors {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("strategy.txt"));
        int totalScore = 0;

        for (String line : lines) {
            totalScore += calculateRoundScore(line.trim());
        }

        System.out.println("Total score: " + totalScore);
    }

    private static int calculateRoundScore(String round) {
        char opponentMove = round.charAt(0);
        char yourResponse = round.charAt(2);

        Shape opponentShape = Shape.fromChar(opponentMove);
        Shape yourShape = Shape.fromChar(yourResponse);

        boolean win = didWin(yourShape, opponentShape);
        boolean draw = yourShape == opponentShape;

        return calculatePoints(win, draw, yourShape);
    }

    private static int calculatePoints(boolean win, boolean draw, Shape shape) {
        int score = shape.getScore();
        if (win) {
            score += 6;
        } else if (draw) {
            score += 3;
        }
        return score;
    }

    private static boolean didWin(Shape yourShape, Shape opponentShape) {
        return (yourShape == Shape.Rock && opponentShape == Shape.Scissors) ||
               (yourShape == Shape.Paper && opponentShape == Shape.Rock) ||
               (yourShape == Shape.Scissors && opponentShape == Shape.Paper);
    }

    private static char convertResponseToMove(char response) {
        switch (response) {
            case 'X': return 'A';
            case 'Y': return 'B';
            case 'Z': return 'C';
            default:  return ' ';
        }
    }

    private enum Shape {
        Rock(1), Paper(2), Scissors(3);

        private final int score;

        Shape(int score) {
            this.score = score;
        }

        public int getScore() {
            return this.score;
        }

        public static Shape fromChar(char c) {
            switch (c) {
                case 'A':
                case 'X':
                    return Rock;
                case 'B':
                case 'Y':
                    return Paper;
                case 'C':
                case 'Z':
                    return Scissors;
                default:
                    throw new IllegalArgumentException("Invalid character for shape: " + c);
            }
        }
    }
}
