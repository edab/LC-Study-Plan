# Leetcode 1. Two Sum
#
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

# Solution using HashMap
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(N) space | where N represent the number of elements in the input array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        missing_addendum = {}

        for i in range(len(nums)):
            if nums[i] in missing_addendum:
                return [missing_addendum[nums[i]], i]
            else:
                missing_addendum[target-nums[i]] = i
