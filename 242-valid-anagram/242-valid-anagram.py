# Approach 2: Frequency Counter List Size 26

# Time complexity: O(n) 
# accessing the counter list is a constant time operation

# Space complexity: O(1)
# the list's size stays constant no matter how large n is.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_list = [0] * 26
        for ch in s:
            counter_list[ord(ch) - ord('a')] += 1
        for ch in t:
            counter_list[ord(ch) - ord('a')] -= 1
            if counter_list[ord(ch) - ord('a')] < 0:
                return False
            
        return True
        