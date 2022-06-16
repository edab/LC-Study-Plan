# Leetcode 91. Decode Ways
#
# Link: https://leetcode.com/problems/decode-ways/
# Difficulty: Medium


# Solution using dfs
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string
class Solution:
    def numDecodings(self, s: str) -> int:

        dp = { len(s): 1 }  # key(strlen) -> number of ways to decode it

        def dfs(i):

            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0

            result = dfs(i + 1)

            if i + 1 < len(s):
                is_dbldigit_with_1 = s[i] == "1"
                is_dbldigit_with_2 = s[i] == "2" and s[i + 1] in "0123456"
                if is_dbldigit_with_1 or is_dbldigit_with_2:
                    result += dfs(i + 2)

            dp[i] = result

            return result

        return dfs(0)

# Solution using dp
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(1) space
class Solution:
    def numDecodings(self, s: str) -> int:

        dp = { len(s): 1 }  # key(strlen) -> number of ways to decode it

        for i in range(len(s) - 1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s):
                is_dbldigit_with_1 = s[i] == "1"
                is_dbldigit_with_2 = s[i] == "2" and s[i + 1] in "0123456"
                if is_dbldigit_with_1 or is_dbldigit_with_2:
                    dp[i] += dp[i + 2]

        return dp[0]
