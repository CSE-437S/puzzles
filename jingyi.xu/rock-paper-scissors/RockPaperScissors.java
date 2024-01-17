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
        Map<Character, Integer> moveScores = Map.of('X', 1, 'Y', 2, 'Z', 3);
        Map<Character, Character> winningMoves = Map.of('C', 'X', 'A', 'Y', 'B', 'Z');

        char opponentMove = round.charAt(0);
        char yourResponse = round.charAt(2);

        int moveScore = moveScores.get(yourResponse);
        int outcomeScore = 0;

        if (winningMoves.get(opponentMove) == yourResponse) {
            outcomeScore = 6; // Win
        } else if (opponentMove == convertResponseToMove(yourResponse)) {
            outcomeScore = 0; // Loss
        } else {
            outcomeScore = 3; // Draw
        }

        return moveScore + outcomeScore;
    }

    private static char convertResponseToMove(char response) {
        switch (response) {
            case 'X': return 'A';
            case 'Y': return 'B';
            case 'Z': return 'C';
            default:  return ' ';
        }
    }
}