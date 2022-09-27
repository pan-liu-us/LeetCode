# Approach 1: Sorting

# Time complexity: O(nlogn) 
# because sorting costs O(nlogn) time and comparing costs O(n) time

# Space complexity: O(1)
# it depends on the sorting implementation

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) 
        