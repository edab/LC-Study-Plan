# Leetcode 39. Combination Sum
#
# Link: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium
# Complexity:
#   O(2^T) time | where T represent the target number
#   O(1) space

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(i, current_combination, total):

            if total == target:
                result.append(current_combination.copy())
                return

            if i >= len(candidates) or total > target:
                return

            current_combination.append(candidates[i])
            dfs(i, current_combination, total + candidates[i])

            current_combination.pop()
            dfs(i+1, current_combination, total)

        dfs(0, [], 0)

        return result
