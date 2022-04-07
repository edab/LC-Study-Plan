# Leetcode 49. Group Anagrams
#
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium

# Solution using counter
# Complexity:
#   O(N*M) time | where N represent the number of words and M the lenght
#   O(N*M) space | where N represent the number of words and M the lenght
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            count_char = [0] * 26

            for char in word:
                count_char[ord(char) - ord('a')] += 1

            result[tuple(count_char)].append(word)

        return result.values()
