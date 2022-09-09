# Approach 1: HashMap + re module

import collections
import re

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return counts.most_common(1)[0][0]
        
        