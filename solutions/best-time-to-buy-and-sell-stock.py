# Leetcode 121. Best Time to Buy and Sell Stock
#
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy

# Solution using SlidingWindow
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        pay, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):

            if prices[pay] < prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[pay])
            else:
                pay = sell

            sell += 1

        return maxProfit
