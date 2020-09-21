// There is an old tale about a king who offered a servant $10,000 as a reward. The servant instead asked that for 30 days he be given an amount that would double, starting with a penny. (1 penny for the first day, 2 for the second, 4 for the third, then 8, 16, 32 pennies, and so on).

// Use for loops to answer the following:

// How much was the reward after 30 days?
// remember, a penny isn't 1, but 0.01

// Bonus (Only If You Have Time):

// How many days would it take the servant to make $10,000?
// How about 1 billion?
// In JavaScript, there is a value Infinity . How many days until the servant has infinite money?

// For a Few Billion

var cash = 0.1;

for(var i = 2; i < 1030;i++){
    cash *= 2
    if(cash > 10000 && cash < 19000) {
        console.log("On day", i, ", the servent's reward was now worth $", cash, "! Which now has surpassed the Kings request by a dramatic increase.")
        continue;
    }
    else if (cash > 1000000000 && cash < 1900000000) {
        console.log("On day", i, ", the servent's reward reached a billion!")
        continue;
    }
    else if (cash == Infinity) {
        console.log("On day", i, ", the servent's reward has now become uncalculable. Done!")
        break
    }
    else {
        console.log("Day", i, "$", cash)
    }
}

// Coding Dojo Solution

// var earnings = .01;
// var amount = .01;
// for (var i = 2; i <= 100000; i++) {
//     earnings = earnings * 2
//     console.log("earnings", earnings)
//     amount = amount + earnings
//     console.log("amount", amount)
//     if(amount == Infinity){
//         console.log(i)
//         break
//     }
// }
