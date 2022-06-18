# Leetcode 300. Longest Increasing Subsequence
#
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Difficulty: Medium


# Solution using DP
# Complexity:
#   O(N^2) time | where N represent the number of elements in the give list
#   O(N) space | where N represent the number of elements in the give list
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    DP[i] = max(DP[i], DP[j] + 1)

        return max(DP)
