# Approach 2: Iteration

# Start from the root and then at each iteration pop the current node out of the deque. Then do the checks: 1. not None, 2. p.val vs q.val, and if checks are OK, push the child nodes.

# Time complexity: O(N)
# N is a number of nodes in the tree, since one visits each node exactly once.

# Space complexity: O(N)
# In the worst case of perfect fully balanced binary tree, since BFS will have to store at least an entire level of the tree in the queue, and the last level has O(N) nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
              
        queue = deque([(p,q)])
      
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
                
        return True
            
        
        


            
        