# Leetcode 191. Number of 1 Bits
#
# Link: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy

# Solution using shift operator
# Complexity:
#   O(1) time
#   O(1) space
class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            count +=  n & 1
            n >>= 1

        return count

# Solution using the Brian Kernighan’s Algorithm
# Complexity:
#   O(1) time
#   O(1) space
class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            count += 1
            n &= (n - 1)

        return count
