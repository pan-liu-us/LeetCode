# Approach 1: Recursion

#  Check if p and q nodes are not None, and their values are equal. If all checks are OK, do the same for the child nodes recursively.

# Time complexity: O(N)
# N is a number of nodes in the tree, since one visits each node exactly once.

# Space complexity: O(N)
# In the worst case of completely unbalanced tree, to keep a recursion stack.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        