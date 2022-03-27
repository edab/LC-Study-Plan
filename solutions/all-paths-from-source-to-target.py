# Leetcode 797. All Paths From Source to Target
#
# Link: https://leetcode.com/problems/all-paths-from-source-to-target/
# Difficulty: Medium

# Solution using BFS.
# Complexity:
#   O(V * 2^V) time | where V represent the number of vertex in the input graph
#     - There could be at most 2^(V - 1) - 1 possible paths between source and
#     destination vertex.
#     - It takes O(V) time to complete one path.
#     - TC = O(V * (2^(V - 1) - 1)) ~ O(V * 2^V)
#   O(V * 2^V) space | where V represent the number of vertex in the input graph
#     - The queue can contain O(2^V) paths and each path will take O(V) space.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        q = deque()
        result = []
        destination = len(graph) - 1

        q.append([0])

        while q:

            path = q.popleft()
            current_node = path[-1]

            if current_node == destination:
                result.append(path)

            for next_node in graph[current_node]:
                new_path = list(path[:])
                new_path.append(next_node)
                q.append(new_path)

        return result


# Solution using DFS.
# Complexity:
#   O(V * 2^V) time | where V represent the number of vertex in the input graph
#   O(V) space | where V represent the number of vertex in the input graph
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        destination = len(graph)-1
        result = []

        def dfs(node, path):

            if node == destination:
                result.append(path.copy())
                return

            for next_node in graph[node]:
                path.append(next_node)
                dfs(next_node, path)
                path.pop()

        dfs(0,[0])

        return result
