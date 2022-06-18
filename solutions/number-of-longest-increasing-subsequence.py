# Leetcode 673. Number of Longest Increasing Subsequence
#
# Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# Difficulty: Medium


# Solution using DP
# Complexity:
#   O(N^2) time | where N represent the number of elements in the give list
#   O(N) space | where N represent the number of elements in the give list
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = dict() # key = index, value = [length of LIS, count]
        lenLIS, result = 0, 0


        for i in range(len(nums) - 1, -1, -1):

            maxLen, maxCount = 1, 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCount = length + 1, count
                    elif length + 1 == maxLen:
                        maxCount += count

            if maxLen > lenLIS:
                lenLIS, result = maxLen, maxCount
            elif maxLen == lenLIS:
                result += maxCount

            dp[i] = [maxLen, maxCount]

        return result
