# Approach 1: Recursive DFS

# T.C. = O(n)
# n is the number of nodes in the tree, each node is visited once

# S.C. = O(h) => O(n)
# h is the height of the tree, because of recursion, O(h) function calls will be placed on the stack in the worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:
            
            # invert child trees
            inverted_right = self.invertTree(root.right)
            inverted_left = self.invertTree(root.left)
            
            # swap children
            root.left = inverted_right
            root.right = inverted_left
            
        return root
        