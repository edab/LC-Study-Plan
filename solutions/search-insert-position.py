# Leetcode 35. Search Insert Position
#
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy

# Solution using BinarySearch
# Complexity:
#   O(logN) time | where N represent the number of elements in the input array
#   O(1) space
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            pivot = (left + right) // 2

            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                return pivot

        return left
