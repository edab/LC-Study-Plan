# Leetcode 52. N-Queens
#
# Link: https://leetcode.com/problems/n-queens-ii/
# Difficulty: Hard
# Tags: BackTracking

# Solution using backtracking
# Complexity:
#   O(N^N) time | where N represent the size of the board
#   O(1) space
class Solution:
    def totalNQueens(self, n: int) -> int:
        # bounding functions
        # row is used directly in the cycle
        used_col = set()
        used_pos_diag = set() # (row + col) = constant
        used_neg_diag = set() # (row - col) = constant

        result = 0

        def backtrack(row):

            if row == n:
                nonlocal result
                result += 1
                return

            for col in range(n):

                if col in used_col or (row + col) in used_pos_diag or (row - col) in used_neg_diag:
                    continue

                used_col.add(col)
                used_pos_diag.add(row + col)
                used_neg_diag.add(row - col)

                backtrack(row + 1)

                used_col.remove(col)
                used_pos_diag.remove(row + col)
                used_neg_diag.remove(row - col)

        backtrack(0)

        return result
