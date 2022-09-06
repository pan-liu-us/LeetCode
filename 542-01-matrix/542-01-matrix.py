# BFS
# Time complexity: O(r⋅c)
# Space complexity: O(r⋅c)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: # mat = [[0,0,0],[0,1,0],[1,1,1]]

        m, n = len(mat), len(mat[0])
        dist = [[0] * n for _ in range(m)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0] # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]
        # keep a queue, q to maintain the queue of cells to be examined next
        # start by adding all the cells with 0s to q
        q = collections.deque(zeroes_pos) # deque([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)])
        seen = set(zeroes_pos) # {(0, 1), (1, 2), (0, 0), (0, 2), (1, 0)}

        # BFS
        while q:
            # Pop the cell from queue, as vertax
            i, j = q.popleft()
            # Check its neighbors in 4 directions
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]: 
                # If (ni,nj) already in seen, skip
                if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in seen:
                    continue
                # Else, update dist[ni][nj], add (ni,nj) to q and mark as seen
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
                seen.add((ni, nj))
        
        return dist



        