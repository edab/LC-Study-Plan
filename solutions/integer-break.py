# Leetcode 343. Integer Break
#
# Link: https://leetcode.com/problems/integer-break/
# Difficulty: Medium

# Solution using the Fisher-Yates Algorithm.
# Complexity:
#   O(N^2) time | where N represent the given number
#   O(N) time | where N represent the given number
class Solution:
    def integerBreak(self, n: int) -> int:

        dp = {1:1}

        def dfs(num):

            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num

            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)

            return dp[num]

        return dfs(n)
