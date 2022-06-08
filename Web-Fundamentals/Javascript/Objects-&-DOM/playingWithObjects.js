// Playing with Objects

// Objectives:

// Practice iterating through an array of objects/dictionaries.
// Imagine that you are given an array of objects.  For example:
var users = [
    {
        name: "Michael",
        age: 37
    },
    {
        name: "John",
        age: 30
    },
    {
        name: "David",
        age: 27
    }
];

// Challenges:
// How would you print/log John's age?
console.log(users[1].name + "'s age is: " + users[1].age);
// How would you print/log the name of the first object?
console.log("Name on the first object is: " + users[0].name);
// How would you print/log the name and age of each user using a for loop?  Your output should look something like this:
for(var user in users){
    console.log(users[user].name + " - " + users[user].age);
}

// Michael - 37
// John - 30
// David - 27
