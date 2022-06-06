# Leetcode 162. Find Peak Element
#
# Link: https://leetcode.com/problems/find-peak-element/
# Difficulty: Medium

# Solution using binary search
# Complexity:
#   O(logN) time | where N represent the number of elements in the input array
#   O(1) space
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
