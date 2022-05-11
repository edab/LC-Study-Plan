# Leetcode 1641. Count Sorted Vowel Strings
#
# Link: https://leetcode.com/problems/count-sorted-vowel-strings/
# Difficulty: Medium

# Solution using DP
# Complexity:
#   O(N) time | where N represent the given length of the vowel string
#   O(1) space
class Solution:
    def countVowelStrings(self, n: int) -> int:

        def using_dp():
            """
            Using dp

            dp[n][a] == number of valid string of length n ends with a
            dp     a, e, i, o, u
            n = 1: 1  1  1  1  1
            n = 2: 1  2  3  4  5
            n = 3: 1  3  6  10 15
            """

            dp = [1] * 5

            for _ in range(2, n+1):
                for i in reversed(range(4)):
                    dp[i] += dp[i+1]

            return sum(dp)

        def using_combination():
            """
            Pick n digits from 5 vowels, (combination with repeat).

            Combination instead of permutation since sorting is required.

            https://www.mathsisfun.com/combinatorics/combinations-permutations.html

            k = number of element we can choose from (5)
            (n + k - 1)! / (n! * (k - 1)!)
            (n + 4)!     / (n! * 4!) = (n+4)*(n+3)*(n+2)*(n+1) / 24
            """

            return (n+4)*(n+3)*(n+2)*(n+1) // 24

        return using_combination()
