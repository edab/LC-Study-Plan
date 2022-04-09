# Leetcode 344. Reverse String
#
# Link: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy

# Solution using TwoPointers
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(1) space

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
