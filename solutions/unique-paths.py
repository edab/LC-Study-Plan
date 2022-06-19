# Leetcode 62. Unique Paths
#
# Link: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium

# Solution using DP.
# Complexity:
#   O(N * M) time | where N and M represents the rows and columns of the grid
#   O(N) space | where N represent the columns of the grid
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]
