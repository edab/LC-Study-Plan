# Leetcode 424. Longest Repeating Character Replacement
#
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Hard

# Solution using sliding window
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(1) space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        chars_in_window = defaultdict(int)
        max_char_freq = 0
        longest_substring = 0
        l = 0

        for r in range(len(s)):

            chars_in_window[s[r]] += 1
            max_char_freq = max(max_char_freq, chars_in_window[s[r]])

            window_size = (r - l + 1)

            if window_size - max_char_freq > k:
                chars_in_window[s[l]] -= 1
                l += 1
                window_size -= 1

            longest_substring = max(longest_substring, window_size)

        return longest_substring
