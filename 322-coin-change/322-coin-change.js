// Approach: Dynamic programming - Bottom up

// Time complexity : O(S*n). 
// On each step the algorithm finds the next F(i) in n iterations, where 1≤i≤S. Therefore in total the iterations are S∗n.

// Space complexity : O(S). 
// We use extra space for the memoization table.

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

var coinChange = function(coins, amount) {
    let dp = Array(amount + 1).fill(amount + 1);
    dp[0] = 0;
    
    for (c of coins){
      for (var x = c; x < amount + 1; x++) {
          dp[x] = Math.min(dp[x], dp[x-c] + 1)
      }
    }
    
    if (dp[amount] !== amount + 1) {
      return dp[amount]  
    } else {
        return -1
    }
    
};
