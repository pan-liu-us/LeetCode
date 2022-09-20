// Approach: Stacks

// Time complexity: O(N)
// traverse the given string one character at a time

// Space complexity: O(N)
// push all opening brackets onto the stack and in the worst case, all the brackets are opening brackets

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if (s.length % 2 !== 0) {
        return false;
    }
    
    let stack = [];
    let mapping = {")": "(", "}": "{", "]": "["}
    
    for (let c of s) {
        if (stack.length && c in mapping) {
            if (stack[stack.length - 1] === mapping[c]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(c);
        } 
    }
    return stack.length === 0;
};