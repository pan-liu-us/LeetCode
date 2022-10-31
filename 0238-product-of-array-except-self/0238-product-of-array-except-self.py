# Left and Right List
# Time complexity:O(N)
# N represents the number of elements in the input array. We use three iterations in total.
# To construct the array L, array R, and the answer array using L and R.

# Space complexity:O(N)
# Used up by the two intermediate arrays to keep track of the product of elements to the left and right.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        L = [1] * len(nums)
        R = [1] * len(nums)

        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            R[j] = R[j + 1] * nums[j + 1]

        for num1, num2 in zip(L, R):
            res.append(num1 * num2)
        
        return res
        