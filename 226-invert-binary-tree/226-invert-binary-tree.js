# Approach 2: Iterative

# T.C. = O(n)
# n is the number of nodes in the tree, each node in the tree is visited / added to the queue only once

# S.C. = O(n)
# size of queue, worst case for a full binary tree, the leaf level has n/2 leaves

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
        
        # store nodes whose left and right child have not been swapped yet
        q = collections.deque([root])
        
        while q:
            cur = q.popleft()   
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root
                
            
            
        
        
        
        