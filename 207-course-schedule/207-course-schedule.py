# Approach: Topological Sort
# Find a global order for all nodes in a DAG (Directed Acyclic Graph) with regarding to their dependencies.

# Time Complexity: O(∣E∣+∣V∣) 
# where |V| is the number of courses, and |E| is the number of dependencies.

# Space Complexity: O(∣E∣+∣V∣)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        from collections import deque
        
        in_degree_list = [0] * numCourses
        relation_dict = defaultdict(list)
        
        for i in prerequisites:
            in_degree_list[i[0]] += 1
            relation_dict[i[1]].append(i[0])
            
        queue = deque()
        for i in range(len(in_degree_list)):
            if in_degree_list[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            numCourses -= 1
            relation_list = relation_dict[current]
            
            if relation_list:
                for i in relation_list:
                    in_degree_list[i] -= 1
                    if in_degree_list[i] == 0:
                        queue.append(i)
                        
        return numCourses == 0
        
            

            