# Time Complexity: O(logN)
# n is the length of nums, while loop will run logN time

# Space Complexity: O(1)
# the space required by the algorithm to process data is constant

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1
        
        