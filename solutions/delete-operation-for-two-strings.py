# Leetcode 583. Delete Operation for Two Strings
#
# Link: https://leetcode.com/problems/delete-operation-for-two-strings/
# Difficulty: Medium

# Solution using DP
# Complexity:
#   O(N*M) time | where N and M represent the length of the two input strings
#   O(N*M) time | where N and M represent the length of the two input strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        w1_len, w2_len = len(word1) + 1, len(word2) + 1

        # Map between words, index=0 mean empty string
        DP = [[0] * w2_len for _ in range(w1_len)]

        # How many delete operation we need for obtaining an empty string?
        for i in range(1, w2_len):
            DP[0][i]=i
        for j in range(1, w1_len):
            DP[j][0]= j

        # For other values
        for i in range(1, w1_len):
            for j in range(1, w2_len):

                if word1[i-1] == word2[j-1]:
                    # Next char is the same, no additional operations
                    DP[i][j] = DP[i-1][j-1]
                else:
                    # Next char not the same, so one delete operation is required
                    DP[i][j] = min(DP[i][j-1] + 1, DP[i-1][j] + 1)

        return DP[i][j]
