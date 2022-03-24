# Leetcode 417. Pacific Atlantic Water Flow
#
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium

# Solution using DFS and sets
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(M*N) time | where M and N represent the rows and cols of the input matrix

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))
        reach_pacific = set()
        reach_atlantic = set()

        def dfs(r, c, visited, old_height):

            if ((r, c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                heights[r][c] < old_height):
                return

            visited.add((r, c))

            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, reach_pacific, 0)
            dfs(r, COLS-1, reach_atlantic, 0)

        for c in range(COLS):
            dfs(0, c, reach_pacific, 0)
            dfs(ROWS-1, c, reach_atlantic, 0)

        return reach_pacific.intersection(reach_atlantic)
