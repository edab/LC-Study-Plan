# Leetcode 647. Palindromic Substrings
#
# Link: https://leetcode.com/problems/palindromic-substrings/
# Difficulty: Medium

# Solution using TwoPointers
# Complexity:
#   O(N^2) time | where N represent the number of elements in the array
#   O(1) space
class Solution:
    def countSubstrings(self, s: str) -> int:

        result = [0]

        def search_palindromic_substring(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result[0] += 1
                left -= 1
                right += 1

        for i in range(len(s)):

            # Check for odd length polindromic substrings
            search_palindromic_substring(i, i)

            # Check for even length polindromic substrings
            search_palindromic_substring(i, i+1)

        return result[0]
