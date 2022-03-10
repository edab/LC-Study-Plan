# Leetcode 224. Basic Calculator
#
# Link: https://leetcode.com/problems/basic-calculator/
# Difficulty: Hard
# Complexity:
#   O(N) time | where N is the number of elements in the input array
#   O(M*2) space | where M is the number of open brackets

class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        res = 0
        sign = 1 # 1 means positive, -1 means negative
        operand = 0

        for ch in s:

            if ch.isdigit():

                # Append digit to the operand
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the last op and save the new one
                res += sign * operand
                sign = 1
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Save result and sign to the stack for later
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1

            elif ch == ')':

                # Evaluate all inside bracket
                res += sign * operand
                # Apply the sign found before (
                res *= stack.pop()
                # Sum all evaluated before (
                res += stack.pop()
                operand = 0

        return res + sign * operand
