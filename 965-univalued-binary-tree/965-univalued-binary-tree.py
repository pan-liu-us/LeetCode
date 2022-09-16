# Approach 1: Depth-First Search

# Output all the values of the array. After, we can check that they are all equal or not.

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
        vals = []
        
        def dfs(node):
            if not node:
                return True
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(set(vals)) == 1
        