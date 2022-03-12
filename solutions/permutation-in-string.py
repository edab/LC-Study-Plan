# Leetcode 567. Permutation in String
#
# Link: https://leetcode.com/problems/permutation-in-string/
# Difficulty: Medium

# Solution using two arrays of 26 elements and comparing them
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target, window = [0] * 26, [0] * 26

        B = [ord(x) - ord('a') for x in s2]

        for i in range(len(s1)):
            target[ord(s1[i]) - ord('a')] += 1

        for i in range(len(s2)):

            window[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                window[ ord(s2[i - len(s1)]) - ord('a') ] -= 1

            if window == target:
                return True

        return False

# Solution using two arrays of 26 elements and comparing only the number of matches
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26

# Solution using a hash of the two strings
# Complexity:
#   O(N) time | where N represent the number of elements in the input string
#   O(1) space
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_sum = s2_sum = 0
        for symbol in s1:
            s1_sum += hash(symbol)
        for i in range(len(s1)):
            s2_sum += hash(s2[i])
        if s2_sum == s1_sum:
            return True
        first_index = 0
        for i in range(len(s1), len(s2)):
            s2_sum += hash(s2[i])
            s2_sum -= hash(s2[first_index])
            if s2_sum == s1_sum:
                return True
            first_index += 1
        return False
