# Leetcode 1162. As Far from Land as Possible
#
# Link: https://leetcode.com/problems/as-far-from-land-as-possible/
# Difficulty: Medium

# Solution using multi source BFS changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(1) space

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND, VISITED = range(3)
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    q.append((r, c))

        if len(q) == 0 or len(q) == ROWS * COLS:
            return -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == WATER):
                        grid[nr][nc] = VISITED
                        q.append((nr, nc))
            distance += 1

        return distance - 1
