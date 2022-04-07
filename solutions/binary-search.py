# Leetcode 704. Binary Search
#
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Complexity:
#   O(logN) time | where N represent the given number of program version
#   O(1) space

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (right + left) // 2
            if target > nums[pivot]:
                left = pivot + 1
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                return pivot

        return -1
