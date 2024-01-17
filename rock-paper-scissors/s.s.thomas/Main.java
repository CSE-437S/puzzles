import java.io.File;
import java.util.Objects;
import java.util.Scanner;
import java.io.FileNotFoundException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("/Users/sandhyathomas/IdeaProjects/RockPaperScissorsPuzzle/src/input.txt");
        Scanner sc = new Scanner(file);

        int total = 0;

        while (sc.hasNextLine()){
            String line = sc.nextLine();
            String[] turn = line.split(" ");

            String first = turn[0];
            String second = turn[1];
            int secondScore = 0;

            if (second.equals("X")){
                secondScore = 1;
            }
            else if (second.equals("Y")){
                secondScore = 2;
            }
            else if (second.equals("Z")){
                secondScore = 3;
            }

            String result = getWinner(first, second);
            total += secondScore;
            if (result.equals("draw")){
                total += 3;
            }
            else if (result.equals("second")){
                total += 6;
            }

        }

        // X 1 rock, Y 2 paper, Z 3 scissors
        // 0 loss, 3 draw, 6 won

        System.out.println(total);
    }

    public static String getWinner(String first, String second){
        if (first.equals("A") && second.equals("Y")){
            return "second";
        }
        else if (first.equals("A") && second.equals("Z")){
            return "first";
        }
        else if (first.equals("B") && second.equals("X")){
            return "first";
        }
        else if (first.equals("B") && second.equals("Z")){
            return "second";
        }
        else if (first.equals("C") && second.equals("X")){
            return "second";
        }
        else if (first.equals("C") && second.equals("Y")){
            return "first";
        }
        else {
            return "draw";
        }

    }
}
