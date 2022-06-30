// Intermediate Foundation

// Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number (inclusive).
// Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

// function sigma(num){
//     var sumOfSigma = 0;
//     for(var i = 1; i <= num; i++){
//         sumOfSigma+= i;
//     }
//     return sumOfSigma;
// }

// console.log(sigma(5));

// Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive).
// For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).

// function factorial(num){
//     var sumOfFactorial = 1;
//     for(var i = 1; i <= num; i++){
//         sumOfFactorial*= i;
//     }
//      return sumOfFactorial;
// }

// console.log(factorial(5));

// Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1.
// Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).

// Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1),
// fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).
// Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as we'll be introducing this concept in Part 2 of this assignment.

// function fibonacci(num){
//     var fib1 = 0;
//     var fib2 = 1;
//     var nextSeq = null;

//     nextSeq = fib1 + fib2;
//     console.log(nextSeq);
    
//     while(num > nextSeq){
//         fib1 = fib2;
//         fib2 = nextSeq;
//         console.log(fib2);
//         nextSeq = fib1 + fib2;
//     }

//     return nextSeq;
// }

// console.log(fibonacci(3));

// Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".
// If array is too short, return null.

// function returnSecond2Last(arr){
//     var value = null;
//     for(i = 0; i < arr.length; i++){
//         if(arr.length >=2){
//             if(i == arr.length - 2){
//                 value = arr[i];
//             }
//             else{
//                 continue;
//             }
//         }
//         else{
//             return null;
//         }
//     }
//     return value;
// }

// console.log(returnSecond2Last([42, true, 4, "Liam", 7]));

// Array: Nth-to-Last: Return the element that is N-from-array's-end.
// Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.

// function returnNth2Last(arr, n){
//     var value = null;
//     for(i = 0; i < arr.length; i++){
//         if(n <= arr.length){
//             if(i == arr.length - n){
//                 value = arr[i];
//             }
//             else{
//                 continue;
//             }
//         }
//         else{
//             return null;
//         }
//     }
//     return value;
// }

// console.log(returnNth2Last([5,2,3,6,4,9,7],3));

// Array: Second-Largest: Return the second-largest element of an array.
// Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

// function secondLargest(arr){
//     var one = 0;
//     var two = 0;
//     for(i = 0; i < arr.length; i++){
//         if(arr[i] > one){
//             two = one;
//             one = arr[i];
//         }
//         else if(arr[i] < one && arr[i] > two){
//             two = arr[i];
//         }
//         else {
//             continue;
//         }
//     }
//     return two;
// }

// console.log(secondLargest([42,1,4,3.14,7]));

// Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order.
// Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].

// function doubleTrouble(arr){
//     var tracker = 0;
//     var copy = [];
//     for(var i = arr.length; i > 0; i--){
//         arr.push(arr[tracker]);
//         copy.push(arr[tracker]);
//         tracker++;
//     }
//     var track = 0;
//     for(var j = 0; j < arr.length; j++){
//         arr[j] = copy[track];
//         arr[j + 1] = copy[track];
//         track++;
//         j++;
//     }
    
//     return arr;
// }

// console.log(doubleTrouble([4, "Ulysses", 42, false]));
