# Leetcode 238. Product of Array Except Self
#
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the stone array
#   O(1) space

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
          result[i] = prefix
          prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
          result[i] *= postfix
          postfix *= nums[i]

        return result
