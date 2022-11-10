/**
 * @param {string[]} words
 * @return {number}
 */

// Approach 1: Hash Set
// 1. transform each word into it's Morse Code representation
// 2. put all transformations into a set seen, and return the size of the set

// Time Complexity: O(N) 
// We iterate through each character of each word in words, N is the sum of the lengths of words in words.

// Space Complexity: O(N)

const MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

var uniqueMorseRepresentations = function(words) {
    const seen = new Set();
    for (const word of words) {
        let code = '';
        for (const ch of word) {
            code += (MORSE[ch.charCodeAt() - 'a'.charCodeAt()]);
        }
        seen.add(code);
    }
    return seen.size;
};
