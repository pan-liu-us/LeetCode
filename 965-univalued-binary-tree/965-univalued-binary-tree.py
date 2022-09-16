# Approach 1: Depth-First Search (use set)

# Add all the values into a seen set. After, we can check the length of the set.

# Time Complexity: O(N) 
# N is the number of nodes in the given tree.

# Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        seen = set()
        
        def dfs(node):
            if not node:
                return True
            if node:
                seen.add(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(seen) == 1
        