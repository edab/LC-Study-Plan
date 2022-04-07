# Leetcode 225. Implement Stack using Queues
#
# Link: https://leetcode.com/problems/implement-stack-using-queues/
# Difficulty: Easy
# Complexity:
#   O(N) time for pop() | where N is the number of elements in the stack
#   O(1) time for push(), top() and empty()
#   O(M) space | where M is the number of consecutive open parentheses

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.topValue = None

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.topValue = x

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
          self.topValue = self.queue.popleft()
          self.push(self.topValue)
        return self.queue.popleft()

    def top(self) -> int:
        return self.topValue

    def empty(self) -> bool:
        return len(self.queue) == 0
