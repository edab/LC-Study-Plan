# Leetcode 49. Group Anagrams
#
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Complexity:
#   O(N*MlogM) time | where N represent the number of words and M the lenght
#   O(N*M) space | where N represent the number of words and M the lenght
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for w in strs:
            key = tuple(sorted(w))
            d[key].append(w)

        return d.values()
