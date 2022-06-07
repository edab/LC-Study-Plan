# Leetcode 209. Minimum Size Subarray Sum
#
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Difficulty: Medium

# Solution using TwoPointers technique
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result, temp_sum =  float('inf'), 0
        left = 0
        for right in range(len(nums)):
            temp_sum += nums[right]
            while temp_sum >= target:
                result = min(result, right - left + 1)
                temp_sum -= nums[left]
                left += 1

        return 0 if result == float('inf') else result
