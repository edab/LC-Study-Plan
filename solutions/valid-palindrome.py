# Leetcode 125. Valid Palindrome
#
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy

# Solution using TwoPointers
# Complexity:
#   O(N) time | where N represent the number of elements in the array
#   O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
