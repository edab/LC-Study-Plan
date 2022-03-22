# Leetcode 1254. Number of Closed Islands
#
# Link: https://leetcode.com/problems/number-of-closed-islands/
# Difficulty: Medium

# Solution using two pass DFS, one for removing perimeter islands, one for count
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input image
#   O(M*N) space | where M and N represent the rows and cols of the input image

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        LAND, WATER, VISITED = 0, 1, -1

        ROWS, COLS = len(grid), len(grid[0])
        close_islands = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] in (WATER, VISITED):
                return 0

            grid[r][c] = VISITED

            return (dfs(r-1, c) +
                    dfs(r+1, c) +
                    dfs(r, c+1) +
                    dfs(r, c-1))

        # Remove islands on perimeter
        for r in range(1, ROWS-1):
            if grid[r][0] == LAND:
                dfs(r, 0)
            if grid[r][COLS-1] == LAND:
                dfs(r, COLS-1)
        for c in range(1, COLS-1):
            if grid[0][c] == LAND:
                dfs(0, c)
            if grid[ROWS-1][c] == LAND:
                dfs(ROWS-1, c)

        # Count islands
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if grid[r][c] == LAND:
                    dfs(r, c)
                    close_islands += 1

        return close_islands
