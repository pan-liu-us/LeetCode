# Approach 1: One-pass Hash Table => val: index
# Time complexity: O(n)
# Space complexity: O(n)
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in hashmap:
                return [hashmap[diff] + 1, i + 1]
            hashmap[numbers[i]] = i