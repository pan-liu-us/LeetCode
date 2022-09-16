# Approach: Recursion

# Time Complexity: O(N)
# N is the number of nodes in the tree. We process every node once.

# Space Complexity: O(H)
# H is the height of the tree. Our recursive call stack could be up to H layers deep.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            if not node:
                return 0
            
            nonlocal res
            
            left = dfs(node.left)     
            right = dfs(node.right)

            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0

            res = max(res, left + right)
            return max(left, right) 
        
        dfs(root)
        return res