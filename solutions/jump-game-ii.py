# Leetcode 45. Jump Game II
#
# Link: https://leetcode.com/problems/jump-game-ii/
# Difficulty: Medium

# Solution using DP.
# Complexity:
#   O(N^2) time | where N represent the length of the input array
#   O(N) space | where N represent the length of the input array
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0

        for i in range(len(nums)):
            n = nums[i]
            for j in range(1, n + 1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i]+1)

        return dp[-1]
