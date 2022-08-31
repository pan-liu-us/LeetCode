# Approach 1: Sort 
# Time Complexity: O(NlogN)
# Space Complexity: O(N)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]

        