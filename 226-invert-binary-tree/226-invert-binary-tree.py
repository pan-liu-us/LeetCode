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
            
            # swap children
            temp = root.left
            root.left = root.right
            root.right = temp
          
            # invert child trees
            self.invertTree(root.right)
            self.invertTree(root.left)
           
        return root
        