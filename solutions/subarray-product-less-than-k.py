# Leetcode 713. Subarray Product Less Than K
#
# Link: https://leetcode.com/problems/subarray-product-less-than-k/
# Difficulty: Medium

# Solution using TwoPointers technique
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(1) space
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1: return 0

        prod = 1
        result = left = 0

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            result += right - left + 1

        return result
