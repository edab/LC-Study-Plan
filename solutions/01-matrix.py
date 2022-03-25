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
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    (nr, nc) not in visited):
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    mat[nr][nc] = mat[r][c] + 1

        return mat
