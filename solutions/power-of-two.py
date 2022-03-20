# Leetcode 231. Power of Two
#
# Link: https://leetcode.com/problems/power-of-two/
# Difficulty: Easy

# Solution using shift operator
# Complexity:
#   O(logN) time | where N represent the given input number
#   O(1) space

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0:
            return False

        while n > 1 and n&1 == 0:
            n >>= 1

        return n == 1
