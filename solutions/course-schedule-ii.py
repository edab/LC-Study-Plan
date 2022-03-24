# Leetcode 210. Course Schedule II
#
# Link: https://leetcode.com/problems/course-schedule-ii/
# Difficulty: Medium
# Complexity:
#   O(V+E) time | where V represent the number of Vertex and E the number of Edges
#   O(V+E) space | where V represent the number of Vertex and E the number of Edges

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = { course:[] for course in range(numCourses) }
        for course, prerequisite in prerequisites:
          adj_list[course].append(prerequisite)

        print(f"")

        output = []
        visited = set()
        cycle = set()

        def dfs(course):

          if course in cycle:
            return False

          if course in visited:
            return True

          cycle.add(course)

          for prerequisite in adj_list[course]:
            if not dfs(prerequisite):
              return False

          cycle.remove(course)
          visited.add(course)
          output.append(course)

          return True

        for course in range(numCourses):
          if not dfs(course):
            return []

        return output
