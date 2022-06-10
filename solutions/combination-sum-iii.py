# Leetcode 216. Combination Sum III
#
# Link: https://leetcode.com/problems/combination-sum-iii/
# Difficulty: Medium

# Solution using DFS
# Complexity:
#   O(k * C(n, k)) time | where k represent the number of elements to combine
#   O(k) space | where k represent the number of elements to combine
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def dfs(i, curr_combination, curr_k, curr_n):

            if curr_k == 0 and curr_n == 0:
                result.append(curr_combination.copy())
            elif curr_k < 0:
                return

            while i < 10 and i * curr_k + curr_k * (curr_k - 1) / 2 <= n:
                curr_combination.append(i)
                dfs(i+1, curr_combination, curr_k - 1, curr_n - i)
                curr_combination.pop()
                i += 1

        dfs(1, [], k, n)

        return result
