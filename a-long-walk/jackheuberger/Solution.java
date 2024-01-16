import java.util.*;


public class Solution {

    public static void main(String[] args) {
        // Read input.txt into a 2d array of chars
        char[][] input = new char[141][141];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 141; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < 141; j++) {
                input[i][j] = line.charAt(j);
            }
        }

        // Print input to check
        for (int i = 0; i < 141; i++) {
            for (int j = 0; j < 141; j++) {
                System.out.print(input[i][j]);
            }
            System.out.println();
        }

        // next steps: recursive backtracking
    }
}