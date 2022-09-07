# First check for obvious fail case
# Then use the Counter class, if anything remain in Counter return False, if empty, return True
    # For example: ransomNote = "ab", magazine = "acdd"
    # collections.Counter(ransomNote) - collections.Counter(magazine) = Counter({'b': 1})
    # So we return not Counter({'b': 1}), that is False
    # if ransomNote = "a", then we return not Counter(), that is True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        