# Leetcode 283. Move Zeroes
#
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(1) space

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        left = 0

        for right in range(len(nums)):
          if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
