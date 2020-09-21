//If You Don't Mind, Can I Have The Time?
//Create a program that will tell you the time.
//With the following variables...
//var HOUR = 8;
//var MINUTE = 50;
//var PERIOD = "AM";
//...your program should print "It's almost 9 in the morning"
//And when changed to...
//var HOUR = 7;
//var MINUTE = 15;
//var PERIOD = "PM";
//...your program should print "It's just after 7 in the evening"
//Challenge:
//If minutes less than 30, "just after" the hour, more than 30, "almost" the next hour
//AM / PM, "in the morning", "in the evening",
//HINT
//You can add as many items into console.log as you need (They will be separated by spaces)
//Example:
//var person = "Jack";
//var me = "Jill";
//console.log("Hello", person, "I am ", me, ".");
// Hello Jack I am Jill.
//Bonus (Only If You Have Time):
//Add functionality for "quarter after", "half past", "5 after" ...
//Distinguish between "in the afternoon", "at night", "noon", "midnight" ...

var HOUR = 6;
var MINUTE = 5;
var PERIOD = "PM";

var str = "It's ";

if(MINUTE > 30) {
    str = str + "almost " + (HOUR + 1);
}
else {
    str = str + "just after " + HOUR;
}

if(PERIOD == "AM") {
    str = str + " in the morning"
}
else {
    str = str + " in the evening"
}

console.log(str)

// BONUS
var str = "It's "
if(MINUTE == 5) {
    str = str +  "5 after " + HOUR;
}
else if(MINUTE == 15) {
    str = str + "a quarter after " + HOUR;
}
else if(MINUTE == 30) {
    str = str + "half past" + HOUR;
}

if(PERIOD == "PM"){
    if(HOUR > 6) {
        str = str + " in the evening"
    }
    else {
        str = str + " in the afternoon"
    }
}
else {
    str = str + " in the morning"
}

console.log(str)
