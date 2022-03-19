# Leetcode 198. House Robber
#
# Link: https://leetcode.com/problems/house-robber/
# Difficulty: Medium

# Solution using DP
# Complexity:
#   O(N) time | where N represent the number of homes
#   O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)
        return rob2
