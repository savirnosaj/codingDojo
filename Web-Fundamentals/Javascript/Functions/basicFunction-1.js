/*Basic Function I

Objectives:
* Understand how a computer executes each line of code
* Get comfortable with how a function works and how its return statement works
* Identify some common mistakes students make and learn how to avoid them
* Predict the output of the following code snippets.  Please do NOT run any of this code directly, but first predict the output using the T-diagram.  If you're not used to using the T-diagram to run through the code yet, please get comfortable now.  This will help you down the line.  Once you've predicted the output for all of the codes, then run the code one by one and compare the two.
*/

// Please turn in a text file that includes your prediction for each problem and the actual output. At the top of the file, indicate how many out of 15 you predicted correctly.

// function a(){
//     return 35;
// }
// console.log(a());

// Prediction: 35
// Answer: 35

// function a(){
//     return 4;
// }
// console.log(a()+a());

// Prediction: 8
// Answer: 8

// function a(b){
//     return b;
// }
// console.log(a(2)+a(4));

// Prediction: 6
// Answer: 6

// function a(b){
//     console.log(b);
//     return b*3;
// }
// console.log(a(3));

// Prediction: 3, 9
// Answer: 3, 9

// function a(b){
//    return b*4;
//    console.log(b);
// }
// console.log(a(10));

// Prediction: 40
// Answer: 40

// function a(b){
//     if(b<10) {
//         return 2;
//     }
//     else     {
//         return 4;
//     }
//     console.log(b);
// }
// console.log(a(15));

// Prediction: 4
// Answer: 4

// function a(b,c){
//     return b*c;
// }
// console.log(10,3);
// console.log( a(3,10) );

// Prediction: 30, 30
// Answer: 10 3, 30
// What I Did Wrong: I mistakenly thought the first console.log was sending value as parameter to function

// function a(b){
//     for(var i=0; i<10; i++){
//         console.log(i);
//     }
//     return i;
// }
// console.log(3);
// console.log(4);

// Prediction: 3, 4
// Answer: 3, 4

// function a(){
//     for(var i=0; i<10; i++){
//         i = i +2;
//         console.log(i);
//     }
// }
// a();

// Prediction: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
// Answer: 2, 5, 8, 11
// What I Did Wrong: 

// function a(b,c){
//     for(var i=b; i<c; i++) {
//        console.log(i);
//    }
//    return b*c;
// }
// a(0,10);
// console.log(a(0,10));

// Prediction: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
// Answer: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
// What I Did Wrong: I didn't consider the forloop console.logging when line 109  in function is ran

// function a(){
//     for(var i=0; i<10; i++){
//        for(var j=0; j<10; j++){
//            console.log(j);
//        }
//        console.log(i);
//     }
// }

// Prediction: null
// Answer: null

// function a(){
//     for(var i=0; i<10; i++){
//         for(var j=0; j<10; j++){
//             console.log(i,j);
//         }
//         console.log(j,i);
//     }
// }
// var z = 10;

// Prediction: null
// Answer: null

// function a(){
//     var z = 15;
//     console.log(z);
// }
// console.log(z);
// var z = 10;

// Prediction: 10
// Answer: undefined
// What I Did Wrong: the console.log was called before z was ever assigned a value

// function a(){
//     var z = 15;
//     console.log(z);
// }
// a();
// console.log(z);
// var z = 10;

// Prediction: 15, undefined
// Answer: 15, undefined

// function a(){
//     var z = 15;
//     console.log(z);
//     return z;
// }
// z = a();
// console.log(z);

// Prediction: 15, 15  
// Answer: 15, 15