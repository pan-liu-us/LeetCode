# Approach 1: Built-in Functions

# Use "{:b}" for converting the argument to a binary form
# "{1} is the second argument. {0} is the first".format('yellow', 3)
# Out: '3 is the second argument. yellow is the first'
# So "{0:b}" is convert the first argument to binary format.

# Time complexity: O((N + M)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2) + int(b,2))
        