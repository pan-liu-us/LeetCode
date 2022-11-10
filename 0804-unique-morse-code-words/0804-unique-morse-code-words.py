# Approach 1: Hash Set

# Time Complexity: O(N) 
# We iterate through each character of each word in words, 
# N is the sum of the lengths of words in words.

# Space Complexity: O(N)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            code = ''
            for ch in word:
                code += MORSE[ord(ch) - ord('a')]
            seen.add(code)
        return len(seen)
            
            
        