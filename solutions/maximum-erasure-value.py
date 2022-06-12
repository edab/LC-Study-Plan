# Leetcode 1695. Maximum Erasure Value
#
# Link: https://leetcode.com/problems/maximum-erasure-value/
# Difficulty: Medium

# Solution using TwoPointers
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(N) space | where N represent the number of elements in the input array
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        subarray_nums = set()
        subarray_sum = max_subarray_sum = 0
        left = 0

        for num in nums:
            while num in subarray_nums:
                subarray_nums.remove(nums[left])
                subarray_sum -= nums[left]
                left += 1

            subarray_nums.add(num)
            subarray_sum += num
            max_subarray_sum = max(max_subarray_sum, subarray_sum)

        return max_subarray_sum
