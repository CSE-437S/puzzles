let redCubeMaximum = 12;
let greenCubeMaximum = 13;
let blueCubeMaximum = 14;

var gamesThatPass = [];

//Firstly let us start with an input of just one color

function checkColor(numberOfSuchCubes, colorOfCubes) {
    var currentMax = 0;
    switch(colorOfCubes) {
        case "red":
            currentMax = 12;
            break;
        case "blue":
            currentMax = 14;
            break;
        case "green":
            currentMax = 13;
            break;
        default:
            return false;
    }
    if (currentMax < numberOfSuchCubes) {
        return false;
    }
    return true;
}

//Tests: Passed
console.log(checkColor(1, "red")); // Should return true
console.log(checkColor(15, "red")); // Should return false
console.log(checkColor(4, "green")); // Should return true
console.log(checkColor(81, "blue")); // Should return false


//Now I get text for a game, I just need to keep track of color and, I also need the game number and end
function processGame(gameString) {
    var gameStringArray = gameString.split(": ");
    var gameNumber = parseInt(gameString[0].trim().replace("Game ", ""));
    var arrayOfHands = gameStringArray[1].split("; ");
    checkArrayOfHands(arrayOfHands);
    //console.log(arrayOfHands);
    //console.log(gameNumber);
}

function checkArrayOfHands(arrayOfHands) {
    arrayOfHands.forEach((hand) => {
        var arrayOfEntries = hand.split(", ");
        checkArrayOfEntries(arrayOfEntries);
    });
}
function checkArrayOfEntries(arrayOfEntries) {
    arrayOfEntries.forEach((entry) => {
        var arrayOfHands = entry.split(", ");
        checkColorFromStringWithBothTextAndColor(arrayOfHands);
    });
}

function checkColorFromStringWithBothTextAndColor(arrayOfEachStringWithColor) {
    arrayOfEachStringWithColor.forEach((stringWithBothToCheck) => {
        var myStringToCheck = stringWithBothToCheck.split(" ");
        checkColor(parseInt(myStringToCheck[0].trim()), myStringToCheck[1]);
    });
}
var chicken = processGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green");

//Then go to one game
//Then all games
