# Approach 1: Recursive DFS

# T.C. = O(n)
# n is the number of nodes in the tree, each node is visited once

# S.C. = O(h) => O(n)
# 使用的空间由递归栈的深度决定，它等于当前节点在二叉树中的高度
# 在平均情况下，二叉树的高度与节点个数为对数关系，即 O(logN)。而在最坏情况下，树形成链状，空间复杂度为 O(N)
# h is the height of the tree, because of recursion, O(h) function calls will be placed on the stack in the worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)  
        return root