# O(1) space approach

# Time complexity: O(N)
# We use one iteration to construct the array L, and one to update the res array.

# Space complexity: O(1) 
# If the res array does not count as extra space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        R = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * R
            R *= nums[i]
        return res
        