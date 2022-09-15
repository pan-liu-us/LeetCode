/**
 * @param {string[]} tokens
 * @return {number}
 */

// convert a string containing a number into a number use +num
var evalRPN = function(tokens) {
    
    const OPERATORS = ["+", "-", "/", "*"];
    const stack = [];

    for (const token of tokens) {
        if (OPERATORS.includes(token)) {
            const number2 = stack.pop();
            const number1 = stack.pop();
            stack.push(operation(number1, number2, token));
        } else {
            stack.push(Number(token));
        }
    }

    return stack.pop();
};

var operation = function(num1, num2, token) {
    if (token === "+") {
        return num1 + num2; 
    } 
    if (token === "-") {
        return num1 - num2;
    }
    if (token === "*") {
        return num1 * num2;
    }
    if (token === "/") {
        return Math.trunc(num1 / num2);
    } 
}