# Leetcode 189. Rotate Array
#
# Link: https://leetcode.com/problems/rotate-array/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

      lookup = set(jewels)
      count = 0

      for stone in stones:
        if stone in lookup:
          count += 1

      return count
