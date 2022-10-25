# BFS
# T.C. = O(N)
# Where N is the number of pixels in the image. For the worst case, we need to process every pixel.
# S.C. = O(N)
# Since the worst case, O(N) extra space is required by the queue.

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])

        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        q = collections.deque()
        q.append((sr, sc))
        
        while q:
            (r, c) = q.popleft()
            image[r][c] = color

            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):

                if 0 <= i < h and 0 <= j < w and image[i][j] == originalColor:
                    q.append((i, j))

        return image