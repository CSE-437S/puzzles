import java.io.*;


public class solution {

    public static void main(String[] args) throws IOException {
        //please replace the pathname with your input below:
        String pathname = "/Users/sammyhong/Documents/a-long-walk/rock-paper-scissors/h.samantha/input.txt";
       
        File file = new File (pathname); 
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        int sum = 0;

      while (( st = br.readLine()) != null){
        char opp_move = st.charAt(0);
        char my_move = st.charAt(2);
        String result;

        switch (opp_move){
            case 'A': //opp chooses rock
                if (my_move == 'X'){
                    result = "draw";
                    sum = sum + 3 + 1;
                }
                else if (my_move == 'Y'){
                    result = "win";
                    sum = sum + 6 + 2;
                }
                else if (my_move == 'Z'){
                    result = "loss";
                    sum = sum + 3;
                }
                break;
            case 'B': //opp chooses paper
                if (my_move == 'X'){
                    result = "loss";
                    sum = sum + 1;
                }
                else if (my_move == 'Y'){
                    result = "draw";
                    sum = sum + 3 + 2;
                }
                else if (my_move == 'Z'){
                    result = "win";
                    sum = sum + 6 + 3;
                }
                    break;
            case 'C': //opp chooses scissors
                if (my_move == 'X'){
                    result = "win";
                    sum = sum + 6 + 1;
                }
                else if (my_move == 'Y'){
                    result = "loss";
                    sum = sum + 2;
                }
                else if (my_move == 'Z'){
                    result = "draw";
                    sum = sum + 3 + 3;
                }
                break;
        }

      }
      System.out.println("Total is: " + sum);
    }
}
