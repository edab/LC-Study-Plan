# Leetcode 374. Guess Number Higher or Lower
#
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/
# Difficulty: Easy

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Solution using Binary search
# Complexity:
#   O(log N) time | where N represent the given number
#   O(1) space
class Solution:
    def guessNumber(self, n: int) -> int:

        left, right = 1, n

        while left < right:

            mid = (right + left + 1) // 2
            if guess(mid) >= 0:
                left = mid
            else:
                right = mid - 1

        return left
