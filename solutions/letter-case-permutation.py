# Leetcode 784. Letter Case Permutation
#
# Link: https://leetcode.com/problems/letter-case-permutation/
# Difficulty: Medium
# Tags: BackTracking, Permutations

# Solution using backtracking
# Complexity:
#   O(N * 2^N) time | where N represent the number of elements in the input string
#   O(1) space
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        res = []

        def backtracking(index, comb):

            if index >= len(s):
                res.append(comb)
                return

            char = s[index]
            if char.isalpha():
                backtracking(index+1, comb+char.upper())
                backtracking(index+1, comb+char.lower())
            else:
                backtracking(index+1, comb+char)

        backtracking(0, "")

        return res
