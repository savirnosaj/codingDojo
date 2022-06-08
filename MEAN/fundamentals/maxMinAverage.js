function maxMinAverage(arr) {
    var max = 0;
    var min = 0;
    var avg = 0;
    
    for(var i = 0; i < arr.length; i++) {
        var mem = arr[i];
        if(arr[i] > max) {
            max = arr[i];
        }
        else if(arr[i] < max) {
            if(min < mem){
                mem = arr[i];
            }
            // can't check for min since min is set to 0 above; don't know how to 
            else {
                min = arr[i];
            }
        }
        avg = avg + arr[i];
    }
    avg /= arr.length;
    return "The minimum is " + min + ", the maximum is " + max + ", and the average is " + avg + ".";
}

console.log(maxMinAverage([1,-2,9,4]));
console.log(maxMinAverage([143,54,21,198,40]));
