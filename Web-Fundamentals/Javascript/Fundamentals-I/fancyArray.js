/*
Normally, if you print an array such as ["James", "Jill", "Jane", "Jack"], you will see the following:

[ "James", "Jill", "Jane", "Jack" ]
Let's make it look fancy! Write a function that will make it print like:

0 -> James
1 -> Jill
2 -> Jane
3 -> Jack
Bonus (Only If You Have Time):

Let the user pass in the symbol that will print (ex: "->", "=>", "::", "-----")
Have an extra parameter reversed. If the user passes true, print the elements in reverse order
*/

// Fancy Array

var names = ["Jason", "Helio", "Maul", "Lionel"];
function printArray(nameArr, symNum, reversed){
    var symArr = ['->', '=>', '::', '----'];
    var empArr = [];
    symbol = symArr[symNum]; // set symbol associted with the number input of that names array index value

    for(idx = 0; idx < nameArr.length; idx++){
        if(symNum >= nameArr.length){ // if the number represeting the input number arrays index value
            symbol = symArr[0]; //if the number represtings symArr index, then set symbol to default.
        }
        if(reversed == true){
            for(idx = nameArr.length - 1; idx >= 0; idx--){
                console.log(`${idx + 1} ${symbol} ${names[idx]}`)
            }
            break;
        }
        else {
            for(idx = 0; idx < nameArr.length; idx++){
                console.log(`${idx + 1} ${symbol} ${names[idx]}`)
            }
        }
    }
}

/* pick a symbol and enter it's associated number:
0 = -> | 1 = => | 2 = :: | 3 = ----
*/
printArray(names, 3, false);
