# Leetcode 977. Squares of a Sorted Array
#
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(N) space | where N represent the number of elements in the input array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right, = 0, len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[right]**2)
                right -= 1

        return result[::-1]
