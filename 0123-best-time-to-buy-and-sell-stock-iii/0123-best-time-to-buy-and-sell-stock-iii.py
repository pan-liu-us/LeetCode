# Time complexity: O(n). Only one iteration 
# Space complexity: O(1). 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty = 0
        oneBought = oneSold = twoBought = twoSold = -float('inf')        
        for price in prices:
            prevOneBought, prevOneSold, prevTwoBought = oneBought, oneSold, twoBought
            oneBought = max(empty - price, prevOneBought)
            oneSold = max(prevOneBought + price, prevOneSold)
            twoBought = max(prevOneSold - price, prevTwoBought)
            twoSold = max(prevTwoBought + price, twoSold)
        return max(empty, oneSold, twoSold)
        