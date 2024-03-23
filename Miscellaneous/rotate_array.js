const rotateArray = function(array, k) {
    //write code 
    if ((array.length === 0) || k === 0 || k == array.length) {
        return array;
    }

    k = k % array.length;

    let temp = array.slice(-k);

    for (let i = array.length - k - 1; i >= 0; i--) {
        array[i + k] = array[i];
    }

    for (let i = 0; i < temp.length; i++) {
        array[i] = temp[i]
    }


    return array;
}