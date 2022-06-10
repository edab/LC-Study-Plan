# Leetcode 130. Surrounded Regions
#
# Link: https://leetcode.com/problems/surrounded-regions/
# Difficulty: Medium

# Solution using DFS
# Complexity:
#   O(N*M) time | where N and M represent the number of rows and columns of the input matrix
#   O(1) space
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))

        def capture(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                capture(nr, nc)

        # Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                # Capture surroudned regions (O -> X)
                if board[r][c] == "O":
                    board[r][c] = "X"
                # Uncapture unsurrounded regions (T -> O)
                elif board[r][c] == "T":
                    board[r][c] = "O"
