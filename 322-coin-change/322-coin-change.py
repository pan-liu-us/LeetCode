# Approach: Dynamic programming - Bottom up

# Time complexity : O(S*n). 
# On each step the algorithm finds the next F(i) in n iterations, where 1≤i≤S. Therefore in total the iterations are S∗n.

# Space complexity : O(S). 
# We use extra space for the memoization table.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  
        dp[0] = 0
        
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    
    