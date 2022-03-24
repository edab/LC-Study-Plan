# Leetcode 207. Course Schedule
#
# Link: https://leetcode.com/problems/course-schedule/
# Difficulty: Medium

# Solution using DFS for detecting cycles
# Complexity:
#   O(N+P) time | where N and P represent the number of nodes (courses) and
#                 prerequisites
#   O(1) space

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list
        coursePrereqMap = { i:[] for i in range(numCourses) }
        for course, prereq in prerequisites:
            coursePrereqMap[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if coursePrereqMap[course] == []:
                return True
            visited.add(course)
            for prereq in coursePrereqMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            coursePrereqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
