# Approach 2: Sliding Window
# Time complexity: O(n)
# Space complexity: O(min(m, n))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        mp = {} # store the latest index of non-dup character in s
        
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)
            mp[s[j]] = j
            ans = max(ans, j - i + 1)          
            
        return ans