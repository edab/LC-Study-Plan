# Leetcode 136. Single Number
#
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy

# Solution using shift operator
# Complexity:
#   O(1) time | where N represent the given input number
#   O(1) space

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1,len(nums)):
            result ^= nums[i]
        return result
