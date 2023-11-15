const checkMonotonic = function(array) {
    //write code here to return either true or false 
    let a = parseInt(array[0]);
    let b = parseInt(array[1]);

    if ((array.length == 0) || (array.length == 1)) {
        return true;
    }

    let increasing = false;
    let decreasing = false;

    if (a <= b) {
        increasing = true;
    } else {
        decreasing = true;
    }

    for (let i = 2; i < array.length; i++) {
        if (increasing == true) {
            if (array[i - 1] > array[i]) {
                return false;
            }
        }
        if (decreasing == true) {
            if (array[i - 1] < array[i]) {
                return false;
            }
        }
    }

    return true;
}