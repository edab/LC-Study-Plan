# Leetcode 1971. Find if Path Exists in Graph
#
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Difficulty: Easy
# Complexity:
#   O(V+E) time | where V represent the number of Vertex and E the number of Edges
#   O(V+E) space | where V represent the number of Vertex and E the number of Edges

class Solution:

  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

    def dfs_iterative(graph, source, destination):

      to_visit = [source]
      seen = set([source])

      while to_visit:
        current = to_visit.pop()
        if current == destination:
          return True
        seen.add(current)

        if current in graph:
          for neighbour in graph[current]:
            if neighbour not in seen:
              to_visit.append(neighbour)

      return False

    def dfs_recursive(graph, node, destination, seen = set()):

      seen.add(node)

      if node == destination:
        return True

      for neighbour in graph[node]:
        if neighbour not in seen:
          if dfs_recursive(graph, neighbour, destination, seen):
            return True

      return False

    def bfs_iterative(graph, source, destination):

      to_visit = deque()
      seen = set()
      to_visit.appendleft(source)

      while to_visit:

        current = to_visit.pop()

        if current == destination:
          return True

        for neighbour in graph[current]:
          if neighbour not in seen:
            seen.add(neighbour)
            to_visit.appendleft(neighbour)

    def bfs_recursive(graph, source, destination):

      def helper(graph, source, destination, to_visit, seen = set()):

        if not to_visit:
          return False

        current = to_visit.pop()
        if current == destination:
          return True

        for neighbour in graph[current]:
          if neighbour not in seen:
            seen.add(current)
            to_visit.appendleft(neighbour)

        return helper(graph, source, destination, to_visit, seen)

      to_visit = deque([source])

      return helper(graph, source, destination, to_visit)


    def create_graph(edges):

      graph = defaultdict(list)

      for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

      return graph

    graph = create_graph(edges)
    return bfs_recursive(graph, source, destination)
