const checkIsomorphic = function(s, t) {
    //write code here
    let temp = {};

    for (let i = 0; i < s.length; i++) {
        if (!temp[s[i]]) {
            temp[s[i]] = t[i];
        }

        if (temp[s[i]] != t[i]) {
            return false;
        }
    }
    return true;
}