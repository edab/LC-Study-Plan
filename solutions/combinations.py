# Leetcode 77. Combinations
#
# Link: https://leetcode.com/problems/combinations/
# Difficulty: Medium
# Tags: BackTracking, Combinations

# Solution using backtracking
# Complexity:
#   O(N^K) time | where N represent the number of elements in the input array and K
#   O(K) space
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtracking(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtracking(i + 1, comb)
                comb.pop()

        backtracking(1, [])

        return res
