# Leetcode 78. Subsets
#
# Link: https://leetcode.com/problems/subsets/
# Difficulty: Medium
# Tags: BackTracking, Subsets

# Solution using backtracking
# Complexity:
#   O(N*2^N) time | where N represent the number of elements in the input array
#   O(N*2^N) space | where N represent the number of elements in the input array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = list()
        subset = list()

        def backtrack(i):

            # Base case
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Decision 1, include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision 1, do not include nums[i]
            subset.pop()
            backtrack(i + 1)


        backtrack(0)

        return result
