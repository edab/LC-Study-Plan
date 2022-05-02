# Leetcode 905. Sort Array By Parity
#
# Link: https://leetcode.com/problems/sort-array-by-parity/
# Difficulty: Easy

# Solution using two pointers.
# Complexity:
#   O(N) time | where N represent the lenght of the longest input list
#   O(1) space

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        even = 0

        for i in range(len(nums)):

            # Find next even number
            if nums[i] % 2 != 0:
                continue

            nums[i], nums[even] = nums[even], nums[i]
            even += 1

        return nums
