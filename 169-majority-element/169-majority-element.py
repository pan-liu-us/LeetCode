# Approach 2: HashMap 

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts, key=counts.get) # the key whose value is the largest
        
        