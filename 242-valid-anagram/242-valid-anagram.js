// Approach 1: Sorting

// Time complexity: O(nlogn) 
// because sorting costs O(nlogn) time and comparing costs O(n) time

// Space complexity: O(1)
// it depends on the sorting implementation

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    return s.length === t.length && [...s].sort().join('') === [...t].sort().join('')
};