# Leetcode 322. Coin Change
#
# Link: https://leetcode.com/problems/coin-change/
# Difficulty: Medium

# Solution using DP
# Complexity:
#   O(N*M) time | where N represent the number of coins and M the amount we are
#                 searching for
#   O(M) space | where M represent the amount we are searching for
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # DP bottom-up, we start solving the base cases
        # What are the minimum number of coins to sum it to n?
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # For all other cases, we try using one of the available coins
        # and the already computed values
        for index in range(1, amount + 1):
            for coin in coins:
                if index - coin >= 0:
                    dp[index] = min(dp[index], 1 + dp[index - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
