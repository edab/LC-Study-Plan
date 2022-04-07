# Leetcode 771. Jewels and Stones
#
# Link: https://leetcode.com/problems/jewels-and-stones/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the stone array
#   O(M) space | where M represent the number of elements in the jewels array

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

      lookup = set(jewels)
      count = 0

      for stone in stones:
        if stone in lookup:
          count += 1

      return count
