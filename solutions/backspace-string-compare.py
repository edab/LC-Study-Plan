# Leetcode 844. Backspace String Compare
#
# Link: https://leetcode.com/problems/backspace-string-compare/
# Difficulty: Easy

# Solution using two pointers.
# Complexity:
#   O(N) time | where N represent the lenght of the longest input string
#   O(1) space

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        first, second = len(s) - 1, len(t) - 1

        def next_index(index, string):
            count = 0
            while index >= 0:
                if string[index] == '#':
                    count += 1
                elif count > 0:
                    count -= 1
                else:
                    break
                index -= 1
            return index


        while first >= 0 or second >= 0:

            new_first = next_index(first, s)
            new_second = next_index(second, t)

            if new_first < 0 and new_second < 0:
                return True
            if new_first < 0 or new_second < 0:
                return False
            if s[new_first] != t[new_second]:
                return False

            first = new_first - 1
            second = new_second - 1

        return True
