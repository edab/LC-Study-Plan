# Leetcode 1319. Number of Operations to Make Network Connected
#
# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Difficulty: Medium

# Solution using DFS and visited set.
# Complexity:
#   O(V+E) time | where V and E represent the number of vertex and edges of the input graph
#   O(V) space | where V represent the number of vertex (computers)
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        adj = defaultdict(list)
        visited = set()
        groups = 0
        edges = 0

        def dfs(i):
            visited.add(i)
            for linked in adj[i]:
                if linked not in visited:
                    dfs(linked)

        # Create adjacency list and count edges
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            edges += 1

        # Found number of groups of connected computers
        for i in range(n):
            if i not in visited:
                dfs(i)
                groups += 1

        if edges < n - 1:
            return -1

        redundant = edges - (n - 1) + (groups - 1)

        if redundant >= groups - 1:
            return groups - 1

        return -1
