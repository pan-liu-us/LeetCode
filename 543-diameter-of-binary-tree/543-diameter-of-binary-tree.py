# Approach 1: Depth-first Search

# Time complexity: O(N)
# In recursion function LP, we only enter and exit from each node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.

# Space complexity: O(N) 
# Depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(logN).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def LP(node):
            if not node:
                return 0
            nonlocal diameter
            left = LP(node.left)
            right = LP(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1 
        
        LP(root)
        return diameter
    