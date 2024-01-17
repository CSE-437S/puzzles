//Player 1 Key: 
// A: Rock
// B: Paper
// C: Scissors 

//Player 2 Key: 
// X: Rock
// Y: Paper
// Z: Scissors

//Point System: 
// 1:Rock, 2:Paper, 3:Scissors
// 0:Lost, 3:Draw, 6:win 
// Add those up for final points

//global variables 
String player1; //determine through column 1
String player2; //determine through column 2
String player1wins;String player2wins;String player1loses;String player2loses;String draw;int player1points;int player2points;

public class rockPaperScissors {
    if (player1 == "A" && player2 == "X"){
        player1 = draw;
        player2 = draw;
    } 
    else if(player1 == "A" && player2 == "Y"){
        player1 = player1loses;
        player2 = player2wins;
    }
    else if(player1 == "A" && player2 == "Z"){
        player1 = player1wins;
        player2 = player2loses;
    }
    else if(player1 == "B" && player2 == "X"){
        player1 = player1wins;
        player2 = player2loses;
    } 
    else if(player1 == "B" && player2 == "Y"){
        player1 = draw;
        player2 = draw;
    } 
    else if (player1 == "C" && player2 == "X"){
        player1 = player1loses;
        player2 = player2wins;
    }
    else if (player1 == "C" && player2 == "Y"){
        player1 = player1wins;
        player2 = player2loses;
    }
    else(player1 == "C" && player2 == "Z"){
        player1 = draw;
        player2 = draw;
    }
}

public class points {
    if(player1 == player1wins && player1 == "A"){
        player1points = 6 + 1;
    } else if (player1 == player1loses && player1== "A" ){
        player1points = 0 + 1;
    } else (player1 == draw && player1 == "A"){
        player1points = 3 + 1;
    }

    if(player1 == player1wins && player1 == "B"){
        player1points = 6 + 2;
    } else if (player1 == player1loses && player1== "B" ){
        player1points = 0 + 2;
    } else (player1 == draw && player1 == "B"){
        player1points = 3 + 2;
    }

    if(player1 == player1wins && player1 == "C"){
        player1points = 6 + 3;
    } else if (player1 == player1loses && player1== "A" ){
        player1points = 0 + 3;
    } else (player1 == draw && player1 == "A"){
        player1points = 3 + 3;
    }

    if(player2 == player2wins && player2 == "X"){
        player2points = 6 + 1;
    } else if (player2 == player2loses && player2== "X" ){
        player2points = 0 + 1;
    } else (player2 == draw && player2 == "X"){
        player2points = 3 + 1;
    }

    if(player2 == player3wins && player2 == "Y"){
        player3points = 6 + 2;
    } else if (player2 == player2loses && player2== "Y" ){
        player3points = 0 + 2;
    } else (player2 == draw && player2 == "Y"){
        player2points = 3 + 2;
    }

    if(player2 == player2wins && player2 == "Z"){
        player2points = 6 + 3;
    } else if (player2 == player2loses && player2== "Z" ){
        player2points = 0 + 3;
    } else (player2 == draw && player2 == "Z"){
        player2points = 3 + 3;
    }
}