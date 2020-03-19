// Creating the Stage by storing values as strings made of our HTML elements;
var World = [
    [2,2,2,2,2,2,2,2,2],
    [2,0,0,2,0,2,0,1,2],
    [2,0,0,0,0,0,0,0,2],
    [2,2,0,3,0,0,0,2,2],
    [2,0,0,0,0,0,0,3,2],
    [2,0,0,0,2,0,0,0,2],
    [2,3,0,0,0,0,0,0,2],
    [2,2,0,0,0,3,0,2,2],
    [2,0,0,0,0,0,0,0,2],
    [2,1,0,2,0,2,0,1,2],
    [2,2,2,2,2,2,2,2,2]
];

// Creating values and assigning each individual number as our appropiate HTML element;
var WorldDictionary = {
    0 : 'blank',
    1 : 'sushi',
    2 : 'wall',
    3 : 'onigiri'
}

// Create a div using JS called "row" for each index value in our World array;
function DrawWorld(){
    output = "";

    // iterate through 'World' array;
    for(var row = 0; row < World.length; row++){
        // insert the beginning of HTML div named 'row' into 'output' empty string;
        output += "<div class='row'>";
        // iterate through each individual array's index values in our World array;
        for(var cont = 0; cont < World[row].length; cont++){
            // add our HTML element incatinated value which is our value that is in our array that's in our World array, to our new string 'output';
            output += "<div class = '" + WorldDictionary[World[row] [cont]] + "'></div>"
        }
        // & close our newly created string which returns our newly created div;
        output += "</div>"
    }
    // print to the screen in the 'world' div, the HTML string stored in 'output';
    document.getElementById('world').innerHTML = output;
    // console.log(output);
}
// call the function immediately when the web-page is ran; 
DrawWorld()

// setting our Ninja's location;
var ninjaLocation = {
    x : 1,
    y : 1
}

// function to move ninja across the play-field by altering it's stored location starting from the far top left corner;
function MoveNinjaMan(){
    document.getElementById('ninja-man').style.top = ninjaLocation.y * 40 + 'px'
    document.getElementById('ninja-man').style.left = ninjaLocation.x * 40 + 'px'
}
MoveNinjaMan()

var count = 0;

document.onkeydown = function(keydown){
    // console.log(keydown);
    if(keydown.keyCode == 37){ // LEFT
        if(World[ninjaLocation.y][ninjaLocation.x - 1] != 2){
            ninjaLocation.x--;
        }
    }
    else if(keydown.keyCode == 38){ // TOP
        if(World[ninjaLocation.y - 1][ninjaLocation.x] != 2){
            ninjaLocation.y--;
        }
    }
    else if(keydown.keyCode == 39){ // RIGHT
        if(World[ninjaLocation.y][ninjaLocation.x + 1] != 2){
            ninjaLocation.x++;
        }
    }
    else if(keydown.keyCode == 40){ // DOWN
        if(World[ninjaLocation.y + 1][ninjaLocation.x] != 2){
            ninjaLocation.y++;
        }
    }
    // if Ninja location is where the initial check is, the do something which is add to score according to which sushi was passed;
    if(World[ninjaLocation.y][ninjaLocation.x] == 1){
        count = count + 10;
        console.log("Picked up a Sushi! " + "10 Points");
    }
    else if(World[ninjaLocation.y][ninjaLocation.x] == 3){
        count = count + 5;
        console.log("Picked up a Onigiri! " + "5 Points");
    }
    World[ninjaLocation.y][ninjaLocation.x] = 0;
    MoveNinjaMan()
    DrawWorld()
    console.log("Total = " + count);
}

// Need to Incorporate following -

// Generate random world when web-page is reloaded
// create algorithm that makes ghost case Ninja-Man
