# Leetcode 997. Find the Town Judge
#
# Link: https://leetcode.com/problems/find-the-town-judge/
# Difficulty: Easy

# Solution using counting array
# Complexity:
#   O(N) time | where N represent the number of people
#   O(N) space | where N represent the number of people
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

      counts = [0 for _ in range(n)]

      for ai, bi in trust:
        counts[ai - 1] -= 1
        counts[bi - 1] += 1

      for i in range(n):
        if counts[i] == n - 1:
          return i + 1

      return -1
