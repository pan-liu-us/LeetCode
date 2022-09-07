# Approach: Dynamic Programming & Rolling Array => Fibonacci Number
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        first, second = 1, 2

        for i in range(3, n + 1):
            first, second = second, first + second
        return second
        