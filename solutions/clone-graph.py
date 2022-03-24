# Leetcode 133. Clone Graph
#
# Link: https://leetcode.com/problems/clone-graph/
# Difficulty: Medium

# Definition for a Node.
# class Node:
#   def __init__(self, val = 0, neighbors = None):
#     self.val = val
#     self.neighbors = neighbors if neighbors is not None else []

# Solution using DFS and HashMap for copying nodes
# Complexity:
#   O(N) time | where N represent the number of nodes in the input graph
#   O(N) space | where N represent the number of nodes in the input graph

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        copyMap = dict()

        def dfs(node):

            if node in copyMap:
                return copyMap[node]

            copy = Node(node.val)
            copyMap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None
