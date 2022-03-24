# Leetcode 542. 01 Matrix
#
# Link: https://leetcode.com/problems/01-matrix/
# Difficulty: Medium

# Solution using DP.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(1) space

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(mat), len(mat[0])

        for r in range(ROWS):
            for c in range(COLS):
                if (mat[r][c] > 0):
                    mat[r][c] = 100001
                    if (r > 0):
                        mat[r][c] = min(mat[r][c], mat[r - 1][c] + 1)
                    if (c > 0):
                        mat[r][c] = min(mat[r][c], mat[r][c - 1] + 1)

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if (mat[r][c] > 0):
                    if (r < ROWS - 1):
                        mat[r][c] = min(mat[r][c], mat[r + 1][c] + 1)
                    if (c < COLS - 1):
                        mat[r][c] = min(mat[r][c], mat[r][c + 1] + 1)

        return mat

# Solution using BFS.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(M*N) space | where M and N represent the rows and cols of the input matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(mat), len(mat[0])

        def bfs():

            q = deque()
            visited = set()

            for r in range(ROWS):
                for c in range(COLS):
                    if mat[r][c] == 0:
                        q.append((r, c))
                        visited.add((r, c))

            while q:
                x, y = q.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX < ROWS and 0 <= newY < COLS and (newX, newY) not in visited:
                        q.append((newX, newY))
                        visited.add((newX, newY))
                        mat[newX][newY] = mat[x][y] + 1

        bfs()

        return mat
