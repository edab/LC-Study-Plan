# Leetcode 743. Network Delay Time
#
# Link: https://leetcode.com/problems/network-delay-time/
# Difficulty: Medium

# Solution using the Djikstra algorithm.
# Complexity:
#   O(|E| * log|V|) time | where E represent the number of edges, and V the number of vertex
#   O(|E|) space | where VErepresent the number of edges
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjacency = collections.defaultdict(list)
        for u, v, w in times:
            adjacency[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        time_to_visit = 0

        while minHeap:

            current_w, current_n = heapq.heappop(minHeap)
            if current_n in visited:
                continue
            visited.add(current_n)
            time_to_visit = max(time_to_visit, current_w)

            for nn, nw in adjacency[current_n]:
                if nn not in visited:
                    heapq.heappush(minHeap, (current_w + nw, nn))

        return time_to_visit if len(visited) == n else -1
