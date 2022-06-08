// Basic Foundation II

// Biggie Size - Given an array, write a function that changes all positive numbers in the array to the string "big".  Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].
// function biggieSize(arr){
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] > 0){
//             arr[i] = 'big';
//         }
//         else {
//             continue;
//         }
//     }
//     return arr;
// }

// console.log(biggieSize([-1, 3, 5, -5]));

// Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.
// function printLowReturnHigh(arr){
//     var low = 0;
//     var high = 0;
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] < low){
//             low = arr[i];
//         }
//         else if(arr[i] > high){
//             high = arr[i];
//         }
//         else {
//             continue;
//         }
//     }
//     console.log(low);
//     return high;
// }

// console.log(printLowReturnHigh([-11, 33, 5, -5]));

// Print One, Return Another - Build a function that takes in an array of numbers.  The function should print the second-to-last value in the array, and return the first odd value in the array.
// function printOneReturnAnother(arr){
//     var placeholder = 0;
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] % 2 == 1){
//             placeholder = arr[i];
//             break;
//         }
//         else {
//             continue;
//         }
//     }
//     console.log(arr[arr.length - 2]);
//     return placeholder;
// }

// console.log(printOneReturnAnother([-77, 11, 45, 5, 16, 77]));

// Double Vision - Given an array (similar to saying 'takes in an array'), create a function that returns a new array where each value in the original array has been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing the original array.
// function doubleVision(arr){
//     var newArr = [];
//     for(var i = 0; i < arr.length; i++){
//         newArr.push(arr[i] * 2);
//     }
//     console.log(arr);
//     return newArr;
// }

// console.log(doubleVision([1, 2, 3, 4]));

// Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.
// function countPositive(arr){
//     var count = 0;
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] > 0){
//             count++;
//         }
//         else {
//             continue;
//         }
//     }
//     arr[arr.length - 1] = count;
//     return arr;
// }

// console.log(countPositive([-1, 1, 1, 1]));

// Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".
// function evensAndOdds(arr){
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] % 2 == 1 && arr[i + 1] % 2 == 1 && arr[i + 2] % 2 == 1){
//             console.log("That's Odd")
//         }
//         else if(arr[i] % 2 == 0 && arr[i + 1] % 2 == 0 && arr[i + 2] % 2 == 0){
//             console.log("Even more so!")
//         }
//         else {
//             continue;
//         }
//     }
// }

// Even
// evensAndOdds([0, 2, 4, 5]);
// Odd
// evensAndOdds([1, 3, 5, 6]);

// Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.
// function incrementTheSeconds(arr){
//     for(var i = 0; i < arr.length; i++){
//         if(i % 2 == 1){
//             arr[i] += 1;
//         }
//         else {
//             continue;
//         }
//     }
// // seems to me like adding another forloop to print the index values individually is ineffective - need to find better solution more appealing to myself (want to add this logic in just the console.log method)
//     for(var i = 0; i < arr.length; i++){
//         console.log(arr[i]);
//     }
//     return arr;
// }

// console.log(incrementTheSeconds([1, 2, 3, 4, 5]));

// Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an array') containing strings.  Working within that same array, replace each string with a number - the length of the string at the previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. Hint: Can for loops only go forward?
// function previousLengths(arr){
//     for(var i = arr.length - 1; i > 0; i--){
//         arr[i] = arr[i - 1].length;
//     }
//     return arr;
// }

// // Expectation: ['Jason', 5, 8]
// console.log(previousLengths(['Jason', 'Consuelo', 'Ileana']));

// Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each. Do not alter the original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a new array.
// function addSeven(arr){
//     var newArr = [];
//     for(var i = 0; i < arr.length; i++){
//         newArr.push(arr[i]);
//         newArr[i] += 7;
//     }
//     return newArr;
// }

// console.log(addSeven([1, 2, 3]));

// Reverse Array - Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).
// function reverseArray(arr){
//     var track = 0;
//     var increment = 0;
//     for(var i = arr.length - 1; i > 0; i--){
//         track = arr[increment];
//         console.log(track);
//         arr[i] = track;
//         console.log(arr[i]);
//         increment++;
//     }
//     return arr;
// }

// console.log(reverseArray([3, 1, 6, 4, 2]));

// Outlook: Negative - Given an array, create and return a new one containing all the values of the original array, but make them all negative (negative values should remain negative). Given [1,-3,5], return [-1,-3,-5].
// function outlookNegative(arr){
//     var newArr = [];
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] > 0){
//             arr[i] *= -1;
//             newArr.push(arr[i]);
//         }
//         else {
//             newArr.push(arr[i]);
//         }
//     }
//     return newArr;
// }

// console.log(outlookNegative([1, -3, 5, 7, -4]));

// Always Hungry - Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food".  If no array values are "food", then print "I'm hungry" once.
// function alwaysHungry(arr){
//     var counter = 0;
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] === 'food' || arr[i] === 'Food'){
//             console.log('Yummy');
//             counter ++;
//         }
//         else {
//             continue;
//         }
//     }
//     if(counter == 0){
//         console.log("I'm Hungry");
//     }
// }

// alwaysHungry([0, 1, 'food', 3, 4, 'Food']);
// alwaysHungry([0, 1, 3, 4]);

// Swap Toward the Center - Given an array, swap the first and last values, third and third-to-last values, etc.  Example: swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into ["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns the array into [6,2,4,3,5,1].  No need to return the array this time.
// function swapTowardsCenter(arr){
//     var placeholder = 0;
//     var plaseholder = 0;
//     for(var i = 0; i < arr.length; i++){
//         if(arr.length < 6){
//             if(i == 0){
//                 placeholder = arr[i];
//                 arr[i] = arr[arr.length - 1];
//             }
//             else if(i == arr.length - 1){
//                 arr[i] = placeholder;
//             }
//             else {
//                 continue;
//             }
//         }
//         else {
//             if(i == 0){
//                 placeholder = arr[i];
//                 arr[i] = arr[arr.length - 1];
//             }
//             else if(i == 2){
//                 plaseholder = arr[i];
//                 arr[i] = arr[arr.length - 3];
//             }
//             else if(i == arr.length - 3){
//                 arr[i] = plaseholder;
//             }
//             else if(i == arr.length - 1){
//                 arr[i] = placeholder;
//             }
//             else {
//                 continue;
//             }
//         }
//     }
//     return arr;
// }

// console.log(swapTowardsCenter([true,42,"Ada",2,"pizza"]));
// console.log(swapTowardsCenter([1, 2, 3, 4, 5, 6]));

// Scale the Array - Given an array arr and a number num, multiply all values in the array arr by the number num, and return the changed array arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9].
// function scaleArray(arr, num){
//     for(var i = 0; i < arr.length; i++){
//         arr[i] *= num;
//     }
//     return arr;
// }

// console.log(scaleArray([1, 2, 3], 3));
