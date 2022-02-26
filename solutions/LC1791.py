# Leetcode 1791. Find Center of Star Graph
#
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Difficulty: Easy
# Complexity:
#   O(1) time
#   O(1) space

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

      def using_sets(edges):
        return set(edges[0]).intersection(set(edges[1])).pop()

      def from_scratch(edges):
        return edges[0][edges[0][1] in edges[1]]

      return from_scratch(edges)
