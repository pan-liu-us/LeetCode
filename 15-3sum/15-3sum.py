# Approach: Sorting + Two Pointers
# Time Complexity: O(n2)
# Space Complexity: O(logn) to O(n)
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
    
        nums.sort()
        if nums[0] > 0 or nums[length - 1] < 0:
            return []
        
        res = []
        
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, length - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l< r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res                 
                        
        
        
        
        