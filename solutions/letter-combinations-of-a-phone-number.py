# Leetcode 17. Letter Combinations of a Phone Number
#
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium
# Complexity:
#   O(N * 4 ^ N) time | where 4 and N represent the number of possible letters
#                       per digit and the number of digits
#   O(1) space | where M and N represent the size of the board

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter_lut = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []

        def backtrack(index, output):

            if len(output) == len(digits):
                result.append(output)
                return

            for char in letter_lut[int(digits[index])]:
                backtrack(index + 1, output + char)

        # We need to reply [] to empty input string
        if digits:
            backtrack(0, "")

        return result
