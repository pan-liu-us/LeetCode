# Approach: Stacks

# Time complexity: O(N)
# traverse the given string one character at a time

# Space complexity: O(N)
# push all opening brackets onto the stack and in the worst case, all the brackets are opening brackets

class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]: stack.pop()
                else: return False
            else: stack.append(i)
            
        return len(stack) == 0
        