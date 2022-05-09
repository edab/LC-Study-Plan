# Leetcode 581. Shortest Unsorted Continuous Subarray
#
# Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Difficulty: Medium

# Solution using two pointers.
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(1) space

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        min_from_right, max_from_left = nums[-1], nums[0]
        left, right = -1, -2

        for i in range(1, len(nums)):

            j = len(nums) - i - 1

            min_from_right = min(min_from_right, nums[j])
            max_from_left = max(max_from_left, nums[i])

            if nums[i] < max_from_left:
                right = i

            if nums[j] > min_from_right:
                left = j

        return right - left + 1
