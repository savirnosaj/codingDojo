// Create a birthday countdown.

// var daysUntilMyBirthday = 60;

// For every day, print how many days left.
// If it's more than 30 days, print a sad message.
// If it's less than 30 days, print a message that sounds excited!
// If it's less than 5 days, SCREAM IT!

// ONCE IT'S YOUR BIRTHDAY, HAVE A PARTY!

// 60 days until my birthday. Such a long time... :(
// 59 days until my birthday. Such a long time... :(
// 58 days until my birthday. Such a long time... :(
// 2 DAYS UNTIL MY BIRTHDAY!!!
// 1 DAY UNTIL MY BIRTHDAY!!!
// ♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*
// ♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪
// *•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«

//While You Wait

var dayOfMyBirthday = 181;

for(var dayToday = 131; dayToday <= dayOfMyBirthday; dayToday++) {
    if(dayToday < (dayOfMyBirthday - 30)) {
        console.log("Today is the " + dayToday + " day of the year. " + (dayOfMyBirthday - dayToday) + " days until my birthday. Such a long time ... :(")
    }
    else if(dayToday >= (dayOfMyBirthday - 30) && dayToday < dayOfMyBirthday) {
        console.log("Today is the " + dayToday + " day of the year. " + (dayOfMyBirthday - dayToday) + " DAYS UNTIL MY BIRTHDAY!!")
    }
    else (
        console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«")
    )
}
