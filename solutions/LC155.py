# Leetcode 155. Min Stack
#
# Link: https://leetcode.com/problems/min-stack/
# Difficulty: Easy
# Complexity:
#   O(1) time for push(), pop(), top() and getMin()
#   O(N) space | where N represent the number of elements added to the stack

class MinStack:

    def __init__(self):
      self.stack = []
      self.minStack = []

    def push(self, val: int) -> None:
      self.stack.append(val)
      minval = min(val, self.minStack[-1] if self.minStack else val)
      self.minStack.append(minval)

    def pop(self) -> None:
      self.stack.pop()
      self.minStack.pop()

    def top(self) -> int:
      return self.stack[-1]

    def getMin(self) -> int:
      return self.minStack[-1]
