/*
Predict the Output
Practice using a T-diagram to go through the following code snippets and predict the output.
Once you're done run your code and see if your prediction was correct.
Create a .js file with the code snippets and your predicted output and upload it once you're done.
*/

//Predict 1:
// function greetingcopy(){
//     return "Hello";
//     console.log("World");
// }
// var word = greeting();
// console.log(word);

// Guess: null
// Note: the function is never called and there is no function called 'greeting()' for var word to be set to.

// Predict 2:
// function add(num1, num2){
//     console.log("Summing Numbers!");
//     console.log("num1 is: " + num1);
//     console.log("num2 is: " + num2);
//     var sum = num1 + num2;
//     return sum;
// }
// var result1 = add(3,5);
// var result2 = add(4,7);
// console.log(result1);
// console.log(result2);

// Guess: 8, 11

// Predict 3:
function highFive(num){
    for(var i=0; i<num; i++){
        if(i == 5){
            console.log("High Five!");
        }
        else{
            console.log(i);
        }
    }
}
    
highFive(6);

// Guess: 0, 1, 2, 3, 4, "High Five"
