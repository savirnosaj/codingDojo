/*
Make a function that takes a number of quarters (1 quarter = 1 game).

There is a 1 in 100 chance to win the slot machine (which will give you between 50 - 100 quarters -- use Math.random and Math.floor to pick a random number of coins).

While the user still has quarters, use Math.random to determine if they won.

If they ever win, return the number of quarters (ex: they had 50 remaining quarters and won 90, so it should return 140).

Return 0 if all the quarters were wasted.

Bonus (Only If You Have Time):

Let the user pass the number they are willing to leave
(ex: If they won the lottery and still have 40 coins, they will keep playing until they have collected 200 coins)
*/

// Random Chance
function slotMachine(quarters, goal){
    var winNum = Math.trunc(Math.random() * goal);
    var coinsWon = 0;
    
    while(quarters > 0){
        var slotNum = Math.trunc(Math.random() * goal);

        console.log(`1) Coin Inserted!`)
        quarters -= 1;
        //console.log(`You have ${quarters} remaining quarters`)
        if(slotNum === winNum){
            // reward
            coinsWon = coinsWon + Math.floor(Math.random() * goal / 2) + 1;
            console.log(`2) HIT! You earned ${coinsWon} quarters!`);
            
            
            quarters += coinsWon;
            console.log(`3) ${coinsWon} Added to Quarters. Total: ${quarters}`);
            // when jackpot is hit, allows player to play until he reaches goal quarters
            if(quarters >= goal){
                console.log(`4) You reached your goal! Congradulations`)
                break;
            }
            else {
                coinsWon += Math.floor(Math.random() * goal /2);
                quarters += coinsWon;
                console.log(quarters);
            }
            
            //console.log(`You recieved the remaining quarters, plus the ones you won. Total: ${quarters} quarters`)
        }
        else {
            console.log(`2) Miss! Try Again`);
            console.log(`3) ${quarters} quarters remaining!`);
        }
    }
    if(quarters == 0){
        console.log(`Game Over. Please insert more quarters!`);
        return 0;
    }
}

slotMachine(10, 20);
