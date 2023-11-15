const maxArea = function(array) {
    //write code here
    let left = 0;
    let right = array.length - 1;

    let maxArea = 0;

    while (left < right) {
        let area = Math.min(array[left], array[right]) * (right - left);
        maxArea = Math.max(area, maxArea);

        if (array[left] < array[right]) {
            left += 1
        } else {
            right -= 1
        }
    }

    return maxArea

}