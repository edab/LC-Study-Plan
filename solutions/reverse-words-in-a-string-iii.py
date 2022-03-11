# Leetcode 557. Reverse Words in a String III
#
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Medium

# Solution using lists
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string
class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split(' '):
            wordList = list(word)
            l, r = 0, len(wordList) - 1
            while l < r:
                wordList[l], wordList[r] = wordList[r], wordList[l]
                l += 1
                r -= 1
            result.append(''.join(wordList))
        return ' '.join(result)

# Solution using python list comprehension
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])
