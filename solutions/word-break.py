# Leetcode 139. Word Break
#
# Link: https://leetcode.com/problems/word-break/
# Difficulty: Medium

# Solution using dp
# Complexity:
#   O(N*M) time | where N represent the number of elements in the input string and M the size of the dictionary
#   O(N) space | where N represent the number of elements in the input string
class Sol
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
