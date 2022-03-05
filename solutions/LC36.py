# Leetcode 36. Valid Sudoku
#
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium
# Complexity:
#   O(9^2) time
#   O(9^2) space

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

      width, height = len(board[0]), len(board)

      rows = collections.defaultdict(set)
      cols = collections.defaultdict(set)
      boxs = collections.defaultdict(set)

      for row in range(height):
        for col in range(width):
          if board[row][col] == '.':
            continue
          if (board[row][col] in rows[row] or
              board[row][col] in cols[col] or
              board[row][col] in boxs[(col // 3, row // 3)]):
            return False

          rows[row].add(board[row][col])
          cols[col].add(board[row][col])
          boxs[(col // 3, row // 3)].add(board[row][col])

      return True
