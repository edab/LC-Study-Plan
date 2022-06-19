# Leetcode 201. Bitwise AND of Numbers Range
#
# Link: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Difficulty: Medium

# Solution using Bit Manipulation.
# Complexity:
#   O(1) time
#   O(1) space
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        count = 0

        # Find the leftmost common bits
        while left != right:
            left >>= 1
            right >>= 1
            count += 1

        return left << count
