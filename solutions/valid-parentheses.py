# Leetcode 20. Valid Parentheses
#
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N is the length of the input String
#   O(M) space | where M is the number of consecutive open parentheses

class Solution:
    def isValid(self, s: str) -> bool:

      stack = []
      closeToOpen = {']': '[', ')': '(', '}': '{'}

      for char in s:
        if char in closeToOpen:
          if stack and stack[-1] == closeToOpen[char]:
            stack.pop()
          else:
            return False
        else:
          stack.append(char)

      return not stack
