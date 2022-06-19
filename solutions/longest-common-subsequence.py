# Leetcode 1143. Longest Common Subsequence
#
# Link: https://leetcode.com/problems/longest-common-subsequence/
# Difficulty: Medium

# Solution using DP.
# Complexity:
#   O(N*M) time | where N and M represent the length of the two input strings
#   O(N*M) time | where N and M represent the length of the two input strings
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
