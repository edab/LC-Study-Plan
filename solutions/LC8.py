# Leetcode 8. String to Integer (atoi)
#
# Link: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium
# Complexity:
#   O(N^2) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    def myAtoi(self, s: str) -> int:

        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        i = 0
        result = 0
        sign = 1

        # Check whitespaces
        while i < len(s) and s[i] == ' ':
          i += 1

        # Check for +/- symbols
        if i < len(s) and s[i] == '-':
          i += 1
          sign = -1
        elif i < len(s) and s[i] == '+':
          i += 1

        # Check digits
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
          result = result * 10 + int(s[i])
          i += 1

        # Check the MIN/MAX
        result = sign * result
        if result < 0:
          return max(result, MIN_INT)
        else:
          return min(result, MAX_INT)
