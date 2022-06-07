# Leetcode 438. Find All Anagrams in a String
#
# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Difficulty: Medium

# Solution using hashmaps and TwoPointers technique
# Complexity:
#   O(N) time | where N represent the number of elements in the input string s
#   O(M) space | where N represent the number of elements in the input string p
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        p_counts = dict()
        s_counts = dict()

        for i in range(len(p)):
            p_counts[p[i]] = 1 + p_counts.get(p[i], 0)
            s_counts[s[i]] = 1 + s_counts.get(s[i], 0)

        result = [0] if p_counts == s_counts else []

        left = 0
        for right in range(len(p), len(s)):
            s_counts[s[right]] = 1 + s_counts.get(s[right], 0)
            s_counts[s[left]] -= 1

            if not s_counts[s[left]]:
                s_counts.pop(s[left])

            left += 1

            if p_counts == s_counts:
                result.append(left)

        return result
