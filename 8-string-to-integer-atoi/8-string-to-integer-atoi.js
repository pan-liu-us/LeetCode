// Approach: Follow the Rules

// Time complexity: O(N) 
// N is the number of characters in the input string

// Space complexity: O(1)

/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let res = 0;
    let sign = 1;
    let index = 0;
    let n = s.length;
    const INT_MAX = Math.pow(2, 31) - 1;
    const INT_MIN = -Math.pow(2, 31);
    
    while(index < n && s[index] === " ") {
        index++;
    }
    
    if(index < n && s[index] === "+") {
        sign = 1;
        index++;
    } else if (index < n && s[index] === "-") {
        sign = -1;
        index++;
    }
    
    while(index < n && !isNaN(s[index]) && s[index] !== " ") {
        let digit = s[index] - 0;
        if (res > Math.floor(INT_MAX / 10) || (res === Math.floor(INT_MAX / 10) && digit > INT_MAX % 10)) {
            return sign === 1 ? INT_MAX : INT_MIN
        }
        
        res = res * 10 + digit;
        index++;
    }
    
    return sign * res;
};