# Leetcode 200. Number of Islands
#
# Link: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium

# Solution using BFS and visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(M*N) space | where M and N represent the rows and cols of the input matrix
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))
        count = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    newR, newC = r + dr, c + dc
                    if (newR in range(ROWS) and
                        newC in range(COLS) and
                        (newR, newC) not in visited):
                        visited.add((newR, newC))
                        if grid[newR][newC] == "1":
                            q.append((newR, newC))



        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    count += 1
                    bfs(r, c)

        return count

# Solution using DFS and changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(1) space
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))
        count = 0

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                grid[r][c] = '0'
                for dr, dc in DIRECTIONS:
                    newR, newC = r + dr, c + dc
                    if (newR in range(ROWS) and
                        newC in range(COLS) and
                        grid[newR][newC] == '1'):
                        stack.append((newR, newC))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count
