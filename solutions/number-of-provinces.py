# Leetcode 547. Number of Provinces
#
# Link: https://leetcode.com/problems/number-of-provinces/
# Difficulty: Medium

# Solution using DFS and visited set.
# Complexity:
#   O(N) time | where N represent the number of cities
#   O(N) space | where N represent the number of cities
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        numOfCities = len(isConnected[0])
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for other_city in range(numOfCities):
                if isConnected[city][other_city] and other_city not in visited:
                    dfs(other_city)

        for city in range(numOfCities):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces
