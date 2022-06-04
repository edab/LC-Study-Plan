# Leetcode 51. N-Queens
#
# Link: https://leetcode.com/problems/n-queens/
# Difficulty: Hard
# Tags: BackTracking

# Solution using backtracking
# Complexity:
#   O(N^2) time | where N represent the number of elements in the input array and K
#   O(N*N) space | where N represent the size of the board
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # bounding functions
        # row is used directly in the cycle
        used_col = set()
        used_pos_diag = set() # (row + col) = constant
        used_neg_diag = set() # (row - col) = constant

        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):

            if row == n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):

                if col in used_col or (row + col) in used_pos_diag or (row - col) in used_neg_diag:
                    continue

                used_col.add(col)
                used_pos_diag.add(row + col)
                used_neg_diag.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                used_col.remove(col)
                used_pos_diag.remove(row + col)
                used_neg_diag.remove(row - col)
                board[row][col] = "."

        backtrack(0)

        return result
