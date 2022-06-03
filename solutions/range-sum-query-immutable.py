# Leetcode 303. Range Sum Query - Immutable
#
# Link: https://leetcode.com/problems/range-sum-query-immutable/
# Difficulty: Easy

# Solution using DP(prefix_sum)
# Complexity:
#   O(N) time (init) | where N represent the number of items in the input list
#   O(1) time (query)
#   O(N) space | where N represent the number of items in the input list

class NumArray:

    def __init__(self, nums: List[int]):

        self.dp = [0 for _ in range(len(nums) + 1)]

        for i in range(1, len(nums)+1):
            self.dp[i] = self.dp[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:

        return self.dp[right+1] - self.dp[left]
