"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# edge. The original node could be None
# 1. Put the first node in the queue
# 2. Use a dictionary to save the visited node and it's respective clone as key and value => avoid cycles
# 3. Clone the node and put it in the visited dictionary
# 4. Start BFS traversal
    # pop a node cur from the front of the queue
    # iterate through all the neighbors of the cur node
      # clone the nei and put it as visited if not present already
      # add the newly encountered node to the queue
    # add the clone of the nei to the neighbors of the clone node q
# 5. Return the clone of the node from visited 
    
    
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node 
        
        q = deque([node])
        visited = {}
        visited[node] = Node(node.val, [])
        
        #BFS
        while q:
            cur = q.popleft()
            
            for nei in cur.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    q.append(nei)
                visited[cur].neighbors.append(visited[nei])   
                
        return visited[node]
        