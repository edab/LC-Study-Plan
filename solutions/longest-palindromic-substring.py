# Leetcode 5. Longest Palindromic Substring
#
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Complexity:
#   O(N^2) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        result = []

        for i in range(len(s)):

          left, right = i, i
          while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(result):
              result = s[left:right+1]
            left -= 1
            right += 1

          left, right = i, i + 1
          while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(result):
              result = s[left:right+1]
            left -= 1
            right += 1

        return result
