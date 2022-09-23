// Approach: Compare with Reverse

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const filtered = s.replace(/[^0-9a-z]/gi, '').toLowerCase(); 
    return (filtered === filtered.split('').reverse().join('')); 
};