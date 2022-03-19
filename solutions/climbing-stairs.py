# Leetcode 70. Climbing Stairs
#
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy


# Solution using DP
# Complexity:
#   O(N) time | where N represent the number of steps of the staircase
#   O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one
