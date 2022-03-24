# Leetcode 1254. Number of Closed Islands
#
# Link: https://leetcode.com/problems/number-of-closed-islands/
# Difficulty: Medium

# Solution using two pass DFS, one for removing perimeter islands, one for count
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input image
#   O(1) space
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        WATER, LAND = range(2)
        ROWS, COLS = len(grid1), len(grid1[0])

        def dfs(r, c):

            is_sub_island = grid1[r][c] == LAND

            grid2[r][c] = WATER

            for dr, dc in (1,0), (-1,0), (0,1), (0,-1):
                nr, nc = r+dr, c+dc
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    grid2[nr][nc] == LAND):
                    is_sub_island &= dfs(nr, nc)

            return is_sub_island

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == LAND:
                    if dfs(r,c):
                        count += 1

        return count

        
