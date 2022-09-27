// Approach 2: Counter Array - Size 26

// Time complexity: O(n) 
// accessing the counter array is a constant time operation

// Space complexity: O(1)
// the array's size stays constant no matter how large n is.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    
    const counter = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        counter[s.codePointAt(i) - 'a'.codePointAt(0)]++;
    }
    for (let j = 0; j < t.length; j++) {
        counter[t.codePointAt(j) - 'a'.codePointAt(0)]--;
        if (counter[t.codePointAt(j) - 'a'.codePointAt(0)] < 0) {
            return false;
        }
    }
    
    return true;
};