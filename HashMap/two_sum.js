function findIndicesSum(array, targetValue) {
    //write code here
    let num_available = {};

    for (let i = 0; i < array.length; i++) {
        let needed_val = targetValue - array[i];

        if (needed_val in num_available) {
            return [i, num_available[needed_val]];
        } else {
            num_available[array[i]] = i;
        }
    }
    return []
}