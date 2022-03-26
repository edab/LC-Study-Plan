# Leetcode 994. Rotting Oranges
#
# Link: https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium

# Solution using multi source BFS changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(M*N) time | where M and N represent the rows and cols of the input matrix

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        time, freshOranges = 0, 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and freshOranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        freshOranges -= 1
            time += 1

        return time if freshOranges == 0 else -1
