# Leetcode 704. Binary Search
#
# Link: https://leetcode.com/problems/first-bad-version/
# Difficulty: Easy
# Complexity:
#   O(logN) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index_l, index_r = 0, len(nums) - 1

        while index_l <= index_r:
            index_m = (index_r + index_l) // 2
            if target > nums[index_m]:
                index_l = index_m + 1
            elif target < nums[index_m]:
                index_r = index_m - 1
            else:
                return index_m

        return -1
