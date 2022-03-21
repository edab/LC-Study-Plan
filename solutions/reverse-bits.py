# Leetcode 190. Reverse Bits
#
# Link: https://leetcode.com/problems/reverse-bits/
# Difficulty: Easy

# Solution using shift operator
# Complexity:
#   O(1) time | where N represent the given input number
#   O(1) space

class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0

        for i in range(32):

            bit = (n & 1)
            n >>= 1
            result |= (bit << (31-i))

        return result
