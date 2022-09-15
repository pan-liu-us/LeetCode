/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let n = Math.max(a.length, b.length);
    a = a.padStart(n, "0"); 
    b = b.padStart(n, "0");
    let carry = 0;
    let res =[];
    
    for (let i = n - 1; i >= 0; i--) {
        if (a[i] === "1") {
            carry++;
        }
        if (b[i] === "1") {
            carry++;
        } 
        if (carry % 2 === 1) {
            res.push("1");
        } else {
            res.push("0");
        }
        carry = Math.floor(carry / 2);
       
    }
     
    if (carry === 1) {
        res.push("1");
    }

    return res.reverse().join("");
};