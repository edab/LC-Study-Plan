# Leetcode 22. Generate Parentheses
#
# Link: https://leetcode.com/problems/generate-parentheses/
# Difficulty: Medium

# Solution using Backtraking
# Complexity:
#   O(2^(N+1)) time | where N represent the number of pare
#   O(N) space | where N represent the number of pare
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []

        def backtrack(open_count, closed_count):

            # We found a combination
            if open_count == closed_count == n:
                result.append("".join(stack))
                return

            # We can add an open parenthesis only if
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()

            # We can add a closed parenthesis only if
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()

        backtrack(0, 0)

        return result
