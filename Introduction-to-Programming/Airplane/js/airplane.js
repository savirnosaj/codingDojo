// Objects
var player = {
    left : 525,
    top : 625
}

var enemies = [
    {left : 175, top : 50},
    {left : 825, top : 50},
    {left : 675, top : 150},
    {left : 350, top : 150},
    {left : 525, top : 250}
]

var missiles = []

// Javascript to create our player so it's components can be altered;
function drawPlayer(){
     content = "<div class='airplane' style='left : " + player.left + "px; top : " + player.top + "px;'></div>";
     document.getElementById('player').innerHTML = content;
}

function drawEnemies (){
    content = "";
    console.log(enemies);

    // for every array within "enemies" array, add a string;
    for(var idx = 0; idx < enemies.length; idx++){
        // add the div string to "content", for every array within "enemies" array, along with it's set positons;
        content += "<div class='enemy' style='left : " + enemies[idx].left + "px; top : " + enemies[idx].top + "px;'></div>";
    }
    // print to screen the newly created string "content";
    document.getElementById('enemies').innerHTML = content;
}

function drawMissiles(){
    content = "";

    for(var idx = 0; idx < missiles.length; idx++){
        content += "<div class='missile' style='left : " + missiles[idx].left + "px; top : " + missiles[idx].top + "px;'></div>"
    }
    // print to screen the newly created string "content";
    document.getElementById('missiles').innerHTML = content;
}

function moveEnemies(){
    for(var idx = 0; idx < enemies.length; idx++){
        enemies[idx].top = enemies[idx].top + 1;
    }
}

function moveMissiles(){
    for(var idx = 0; idx < missiles.length; idx++){
        missiles[idx].top = missiles[idx].top - 6;
    }
}

// Move Player
document.onkeydown = function(keydown) {
    // console.log(keydown);
    if(keydown.keyCode == 37 && player.left > 5) { // LEFT
        player.left = player.left - 10;
    }
    else if(keydown.keyCode == 38 && player.top > 500) { // TOP
        player.top = player.top - 10;
    }
    else if(keydown.keyCode == 39 && player.left < 1000) { // RIGHT
        player.left = player.left + 10;
    }
    else if(keydown.keyCode == 40 && player.top < 675) { // DOWN
        player.top = player.top + 10;
    }
    if(keydown.keyCode == 32) { // SHOOT MISSILE
        missiles.push({left : player.left + 20, top : player.top + 8})
        drawMissiles();
}
    drawPlayer();
}

function gameLoop(){
    console.log("gameLoop is running!");

    drawPlayer();

    moveEnemies();
    drawEnemies();

    moveMissiles();
    drawMissiles();

    setTimeout(gameLoop, 50)
}
gameLoop();
