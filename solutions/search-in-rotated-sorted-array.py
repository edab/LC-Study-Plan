# Leetcode 33. Search in Rotated Sorted Array
#
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium

# Solution using binary search
# Complexity:
#   O(logN) time | where N represent the number of elements in the input array
#   O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            # left sorted partition
            if nums[left] <= nums[mid]:

                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # right sorted portion
            else:

                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
