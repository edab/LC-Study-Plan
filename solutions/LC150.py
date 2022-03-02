# Leetcode 150. Evaluate Reverse Polish Notation
#
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the RPN expression
#   O(1) space

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        op = {'+': add, '-': sub, '*': mul, '/': floordiv}

        for token in tokens:
          if token in op:
            a, b = stack.pop(), stack.pop()
            #stack.append(op[token](b,a))
            if token == '+':
              stack.append(a + b)
            elif token == '-':
              stack.append(b - a)
            elif token == '*':
              stack.append(a * b)
            elif token == '/':
              stack.append(int(b / a))
          else:
            stack.append(int(token))

        return stack.pop()
