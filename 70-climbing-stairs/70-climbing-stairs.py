# Approach: Dynamic Programming
# The total number of ways to reach ith step = sum of ways of reaching (i-1)th and (i-2)th step
# Example: n = 4, dp = [0,1,2,3,5], dp[n] = 5
    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
        