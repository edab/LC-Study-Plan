# Leetcode 413. Arithmetic Slices
#
# Link: https://leetcode.com/problems/arithmetic-slices/
# Difficulty: Medium


# Solution using DP
# Complexity:
#   O(N) time | where N represent the number of elements in the give list
#   O(1) space
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = result = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                result += dp
            else:
                dp = 0

        return result
