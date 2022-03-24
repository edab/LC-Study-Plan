# Leetcode 695. Max Area of Island

# Link: https://leetcode.com/problems/max-area-of-island/
# Difficulty: Medium

# Solution using DFS changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input image
#   O(1) space

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND, VISITED = range(3)
        max_area = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != LAND:
                return 0

            grid[r][c] = VISITED

            return (1 + dfs(r-1, c) +
                        dfs(r+1, c) +
                        dfs(r, c+1) +
                        dfs(r, c-1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    max_area = max(max_area, dfs(r, c))

        return max_area
