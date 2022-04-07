# Leetcode 13. Roman to Integer
#
# Link: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    def romanToInt(self, s: str) -> int:

        romanToIntMap = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V':5, 'I': 1}
        result = 0

        for i in range(len(s)-1):
          if romanToIntMap[s[i]] < romanToIntMap[s[i+1]]:
            result -= romanToIntMap[s[i]]
          else:
            result += romanToIntMap[s[i]]

        return result + romanToIntMap[s[-1]]
