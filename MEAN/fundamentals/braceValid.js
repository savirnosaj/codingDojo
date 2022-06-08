/*
Given a string, write a function that will determine whether the braces  - including parentheses (), square brackets [], and curly brackets {} - within the string are valid. That means that any braces within other braces must close before the outer set closes.

HINT: Keep in mind that you may use arrays and objects to keep your information organized!

Example: bracesValid("{{()}}[]") returns true because the inner braces close before the outer braces. Each opening brace has a matching closing brace.

Example:  bracesValid("{(})") returns false because the curly braces close before the parentheses, which starts within the curly braces, had a chance to close.
*/

function braceValid(string) {
    var arr = [];
    var bool = false;
    // iterate through string
    for(var i = 0; i < string.length; i++) {
        // track last value in string
        var check = arr[i];
        var last = arr[arr.length - 1];
        if(string[i] == "{" || string[i] == "[" || string[i] == "(") {
            arr.push(string[i]);
            console.log(arr);
        }
        // add until reach a closing bracket, brace, paranth
        else if(string[i] == ")" || string[i] == "]" || string[i] == "}") {
            arr.push(string[i]);
            if(string[i] == ")" && last == "(") {
                arr.pop(string[i]);
                arr.pop(check);
                console.log(arr);
                check = last;
                console.log(check);
                console.log(string);
            }
            else if(string[i] == "]" && check == "[") {
                console.log(check);
                arr.pop(string[i]);
                console.log(check);
                arr.pop(check);
                console.log(arr);
                console.log(check);
            }
            else if(string[i] == "}" && check == "{") {
                arr.pop(string[i]);
                console.log(check);
                arr.pop(check);
                console.log(arr);
                console.log(check);
            }
            else {
                bool = false;
                console.log("No sequence here");
                break;
            }
        }
        // if program has any other open/close, end program
        else{
            bool = false;
            console.log("Done Here");
            break;
        }
    }
    return bool;
}

console.log(braceValid("{[()]}"));
