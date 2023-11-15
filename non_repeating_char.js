function findNonRepeatingCharacter(string) {
    //write code here
    let ht = {};

    for (let i = 0; i < string.length; i++) {
        if (string[i] in ht) {
            ht[string[i]] += 1;
        } else {
            ht[string[i]] = 1;
        }

    }

    for (let i = 0; i < string.length; i++) {
        if (ht[string[i]] == 1) {
            return i;
        }
    }

    return null;
}