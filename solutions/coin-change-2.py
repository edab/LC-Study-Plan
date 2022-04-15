# Leetcode 518. Coin Change 2
#
# Link: https://leetcode.com/problems/coin-change-2/
# Difficulty: Medium

# Solution using DFS
# Complexity:
#   O(N*M) time | where N represent the number of coins and M the amount we are
#                 searching for
#   O(N*M) space | where M represent the amount we are searching for
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {} # memoization

        def dfs(coin_index, current_amount):
            # We garantee to not have duplicates with the coin_index, since we
            # are not allowed to use coins with index less than the one
            # selected in our descending path

            if current_amount == amount:
                return 1

            if current_amount > amount or coin_index == len(coins):
                return 0

            if (coin_index, current_amount) not in cache:
                # cache = use the coin + skip the coin
                cache[(coin_index, current_amount)] = (
                    dfs(coin_index, current_amount + coins[coin_index]) +
                    dfs(coin_index + 1, current_amount))

            return cache[(coin_index, current_amount)]

        return dfs(0, 0)
