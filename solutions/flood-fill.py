# Leetcode 733. Flood Fill
#
# Link: https://leetcode.com/problems/flood-fill/
# Difficulty: Easy

# Solution using DFS
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input image
#   O(1) space

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]

        if oldColor == newColor:
            return image

        def dfs(r, c):

            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < rows: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < cols: dfs(r, c+1)

        dfs(sr, sc)
        return image
