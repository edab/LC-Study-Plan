# Leetcode 71. Simplify Path
#
# Link: https://leetcode.com/problems/simplify-path/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string

class Solution:
    def simplifyPath(self, path: str) -> str:

      stack = []
      current = ""

      for c in path + "/":

        if c == '/':
          if current == '..':
            if stack: stack.pop()
          elif current != '.' and current != '':
            stack.append(current)
          current = ""
        else:
          current += c


      return "/" + "/".join(stack)
