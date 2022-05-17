# Leetcode 1192. Critical Connections in a Network
#
# Link: https://leetcode.com/problems/critical-connections-in-a-network/
# Difficulty: Hard

# Solution using the Tarjan algorithm.
# Complexity:
#   O(|V| + |E|) time | where E represent the number of edges, and V the number of vertex
#   O(|V| + |E|) space | where E represent the number of edges, and V the number of vertex
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        result = []
        lowest_reacheable, visited = [0]*n, set()
        adj_list = collections.defaultdict(list)

        def tarjan(u, previous, timer):

            if u in visited:
                return

            visited.add(u)

            curr_idx = lowest_reacheable[u] = timer
            timer += 1
            for v in adj_list[u]:
                if v == previous:
                    continue
                tarjan(v, u, timer)
                lowest_reacheable[u] = min(lowest_reacheable[u], lowest_reacheable[v])
                if lowest_reacheable[v] > curr_idx:
                    result.append([u, v])

        for a, b in connections:
            adj_list[a].append(b)
            adj_list[b].append(a)

        tarjan(0, -1, 0)

        return result
