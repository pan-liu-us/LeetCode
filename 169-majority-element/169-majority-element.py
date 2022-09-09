# Approach 3: Sorting
# Time complexity: O(nlogn)
# Space complexity: O(1) or O(n)

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        
        