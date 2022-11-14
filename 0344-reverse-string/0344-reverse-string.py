# Two Pointers

# Time complexity: O(N) to swap N/2 element.
# Space complexity: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1
        