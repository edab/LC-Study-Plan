# Leetcode 807. Max Increase to Keep City Skyline
#
# Link: https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# Difficulty: Medium
# Complexity:
#   O(N^2) time | where N represent the number of rows of the input array
#   O(N) space | where N represent the number of rows of the input array
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        max_by_row = [max(row) for row in grid]
        max_by_col = [max(col) for col in zip(*grid)]
        max_total_sum = 0

        for r in range(rows):
            for c in range(cols):
                max_total_sum += min(max_by_row[r], max_by_col[c]) - grid[r][c]

        return max_total_sum
