# Leetcode 1658. Minimum Operations to Reduce X to Zero
#
# Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Difficulty: Medium

# Solution using DP, prefix_sum
# Complexity:
#   O(N) time | where N represent the number of items in the input list
#   O(N) space | where N represent the number of items in the input list
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        # Reverse thinking, search the longest sequence equal to sum - x

        target = sum(nums) - x
        prefix_sum = 0
        longest = 0
        cache = dict()            # memoization (prefix_sum: index)

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        for i, n in enumerate(nums):

            prefix_sum += n

            if prefix_sum not in cache:
                cache[prefix_sum] = i

            if prefix_sum == target:
                longest = max(longest, i + 1)

            diff = prefix_sum - target
            if diff in cache:
                longest = max(longest, i - cache[diff])

        return -1 if longest == 0 else len(nums) - longest
