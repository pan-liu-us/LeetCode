# DFS
# T.C. = O(N)
# Where N is the number of pixels in the image. For the worst case, we need to process every pixel.
# S.C. = O(N)
# Where N is the size of the implicit call stack when calling dfs.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])

        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        
        def dfs(r: int, c: int):
            if r < 0 or c < 0 or r > h or c > w or image[r][c] != originalColor:
                return
            image[r][c] = color
            if r - 1 >= 0: dfs(r - 1, c)
            if r + 1 < h: dfs(r + 1, c)
            if c - 1 >= 0: dfs(r, c - 1)
            if c + 1 < w: dfs(r, c + 1)
        
        dfs(sr, sc)
        return image
        