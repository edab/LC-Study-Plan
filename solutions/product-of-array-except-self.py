# Leetcode 238. Product of Array Except Self
#
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

# Solution using optimized prefix and postfix values
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

# Solution using prefix and postfix values
# Complexity:
#   O(N) time | where N represent the number of elements in the stone array
#   O(N) time | where N represent the number of elements in the stone array

class Solution:

   def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        result = [0] * len(nums)

        # Build prefix array
        for index in range(len(nums)):
            if index == 0:
                prefix[index] = nums[index]
            else:
                prefix[index] = prefix[index-1] * nums[index]

        # Build postfix array
        for index in range(len(nums)-1,-1,-1):
            if index == len(nums)-1:
                postfix[index] = nums[index]
            else:
                postfix[index] = postfix[index+1] * nums[index]

        # Build response
        for index in range(len(nums)):
            a = 1 if index == 0 else prefix[index-1]
            b = 1 if index == len(nums)-1 else postfix[index+1]
            result[index] = a * b

        return result
