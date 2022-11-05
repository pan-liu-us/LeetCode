# One Pass

# Time complexity: O(n). Only a single pass is needed.
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1] )
                
        return profit
        