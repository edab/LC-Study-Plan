# Leetcode 934. Shortest Bridge
#
# Link: https://leetcode.com/problems/shortest-bridge/
# Difficulty: Medium

# Solution using multi source BFS changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        WATER, LAND = range(2)
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))

        q = deque()
        visited = set()

        def dfs(r, c):

            if ((r, c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] != LAND):
                return

            visited.add((r, c))

            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)


        def bfs():

            q, steps = deque(visited), 0

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (nr in range(ROWS) and
                            nc in range(COLS) and
                            (nr, nc) not in visited):
                            if grid[nr][nc] == LAND:
                                return steps
                            q.append((nr, nc))
                            visited.add((nr, nc))
                steps += 1

        def get_first_land():
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == LAND:
                        return (r, c)

        first_r, first_c = get_first_land()
        dfs(first_r, first_c)
        return bfs()
