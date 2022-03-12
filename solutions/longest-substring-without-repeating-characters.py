# Leetcode 3. Longest Substring Without Repeating Characters
#
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Easy

# Using a set(), for keep track of presence
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(N) space | where N represent the number of elements in the input array
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()
        left = 0
        result = 0

        for right in range(len(s)):
          while s[right] in chars:
            chars.remove(s[left])
            left += 1
          chars.add(s[right])
          result = max(result, right - left + 1)

        return result

# Using a dict(), saving also the last seen position of char, avoiding
# shortening windows one char at a time.
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(N) space | where N represent the number of elements in the input array
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start, result = -1, 0
        lastSeen = dict()

        for i in range(len(s)):

            if s[i] in lastSeen and lastSeen[s[i]] > start:
                start = lastSeen[s[i]]
            else:
                if i - start > result:
                    result = i - start

            lastSeen[s[i]] = i

        return result
