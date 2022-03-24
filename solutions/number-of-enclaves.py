# Leetcode 1020. Number of Enclaves
#
# Link: https://leetcode.com/problems/number-of-enclaves/
# Difficulty: Medium

# Solution using DFS and changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(1) space
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        SEA, LAND = range(2)
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(r, c):

            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == SEA):
                return

            grid[r][c] = SEA

            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc)

        # Remove island reacheable from borders
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        return sum(sum(row) for row in grid)
                
