# Approach: Follow the Rules

# Time complexity: O(N) 
# N is the number of characters in the input string

# Space complexity: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)
        
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        
        # discard all whitespaces from the beginning of the string
        while index < n and s[index] == ' ':
            index += 1
         
        # sign is +1 if positive or -1 if negative
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1
            
        # traverse next digits of the string and stop if it's not a digit
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            # check overflow and underflow conditions
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN
            
            # append current digit to the result
            result = 10 * result + digit
            index += 1
            
        return sign * result
         
        