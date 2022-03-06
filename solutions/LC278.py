# Leetcode 704. Binary Search
#
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Complexity:
#   O(logN) time | where N represent the given number of program version
#   O(1) space

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 0, n

        while left < right:

            pivot = (left + right) // 2

            if (isBadVersion(pivot)):
                right = pivot
            else:
                left = pivot + 1

        return right
