# Leetcode 40. Combination Sum II
#
# Link: https://leetcode.com/problems/combination-sum-ii/
# Difficulty: Medium

# Solution using Backtraking
# Complexity:
#   O(n^2) time | where n represent the number of elements of the input list
#   O(n^2) space | where k represent the number of elements of the input list
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def backtrack(candidate, position, target):

            if target == 0:
                result.append(candidate.copy())

            if target <= 0:
                return

            prev = -1

            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue
                candidate.append(candidates[i])
                backtrack(candidate, i + 1, target - candidates[i])
                candidate.pop()
                prev = candidates[i]

        backtrack([], 0, target)

        return result
