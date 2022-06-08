// Predict the Output - Loops:


// Practice using a T-diagram to go through the following code snippets and predict the output.  Once you're done run your code and see if your prediction was correct.  Create a .js file with the code snippets and your predicted output and upload it once you're done.



// Predict 1: 

// for(var num = 0; num < 15; num++){
//     console.log(num);
// }

// ANSWER: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
// ACTUAL ANSWER: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

// Predict 2:

// for(var i = 1; i < 10; i+=2){
//     if(i % 3 == 0){
//         console.log(i);
//     }
// }

// ANSWER: 3, 6, 9
// ACTUAL ANSWER: 3, 9

// Predict 3:

for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}

// ANSWER: 4, 4, 5, 10, 12, 14, 16, 17
// ACTUAL ANSWER: 1, 4, 5, 8, 10, 11, 14, 16
