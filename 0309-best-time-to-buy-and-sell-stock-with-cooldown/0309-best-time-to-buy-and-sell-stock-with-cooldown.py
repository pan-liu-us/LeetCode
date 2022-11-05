# Time complexity: O(n). Only one iteration 
# Space complexity: O(1). 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy => i + 1
        # If Sell => i + 2
        
        dp = {} # caching: key=(i, buying) val=max_profit
        
        def dfs(i, buying): # index i, boolean whether or not buy
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
                
        return dfs(0, True)