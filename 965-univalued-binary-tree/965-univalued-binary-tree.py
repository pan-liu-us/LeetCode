# Approach 2: Recursion

# A tree is univalued if both its children are univalued, plus the root node has the same value as the child nodes

# Time Complexity: O(N) 
# N is the number of nodes in the given tree.

# Space Complexity: O(H)
# H is the height of the given tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        left_correct = not root.left or (root.val == root.left.val and self.isUnivalTree(root.left))
        right_correct = not root.right or (root.val == root.right.val and self.isUnivalTree(root.right))
        return left_correct and  right_correct
        