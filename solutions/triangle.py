# Leetcode 120. Triangle
#
# Link: https://leetcode.com/problems/triangle/
# Difficulty: Medium

# Solution using DP
# Complexity:
#   O(N^2) time | where N represent the lenght of the bottom row
#   O(N) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle[-1]) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])

        return dp[0]
