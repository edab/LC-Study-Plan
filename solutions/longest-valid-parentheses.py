# Leetcode 32. Longest Valid Parentheses
#
# Link: https://leetcode.com/problems/longest-valid-parentheses/
# Difficulty: Hard
# Complexity:
#   O(N) time | where N is the length of the input String
#   O(N) space | where N is the length of the input String
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        stack.append(-1)
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    seq_len = i - stack[-1]
                    max_len = max(max_len, seq_len)
        return max_len
