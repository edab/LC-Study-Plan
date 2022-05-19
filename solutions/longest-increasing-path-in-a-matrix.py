# Leetcode 329. Longest Increasing Path in a Matrix
#
# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Difficulty: Hard

# Solution using DSF and memoization.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(M*N) space | where M and N represent the rows and cols of the input matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = ((0,-1), (0, 1), (-1, 0), (1, 0))
        dp = {} # (r, c) -> LIP

        def dfs(r, c, previous):

            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= previous):
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(dp.values())
