# Leetcode 153. Find Minimum in Rotated Sorted Array
#
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium

# Solution using binary search
# Complexity:
#   O(logN) time | where N represent the number of elements in the input array
#   O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:

            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])

            # left sorted partition
            if nums[mid] >= nums[left]:

                left = mid + 1

            # right sorted portion
            else:

                right = mid - 1

        return result
