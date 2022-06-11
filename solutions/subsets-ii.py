# Leetcode 90. Subsets II
#
# Link: https://leetcode.com/problems/subsets-ii/
# Difficulty: Medium
# Tags: BackTracking, Subsets

# Solution using backtracking
# Complexity:
#   O(N*2^N) time | where N represent the number of elements in the input array
#   O(N*2^N) space | where N represent the number of elements in the input array
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = list()
        subset = list()

        def backtrack(i):

            # Base case
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Decision 1, all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # Decision 1, all subsets that do not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)

        return result
