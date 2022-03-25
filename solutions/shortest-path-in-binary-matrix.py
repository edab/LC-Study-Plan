# Leetcode 1091. Shortest Path in Binary Matrix
#
# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Difficulty: Medium

# Solution using BFS changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(1) space

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        EMPTY, BLOCKED, VISITED = range(3)
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
        q = deque()

        if grid[0][0] == 0:
            q.append((0,0,1))
            grid[0][0] = VISITED

        while q:
            r, c, distance = q.popleft()
            if ((r,c) == (ROWS - 1, COLS - 1)):
                return distance
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    grid[nr][nc] == EMPTY):
                    q.append((nr,nc,distance+1))
                    grid[nr][nc] = VISITED

        return -1
