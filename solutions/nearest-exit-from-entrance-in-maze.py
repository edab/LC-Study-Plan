# Leetcode 1926. Nearest Exit from Entrance in Maze
#
# Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Difficulty: Medium

# Solution using BFS changing grid values instead of visited set.
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input matrix
#   O(1) space
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        ROWS, COLS = len(maze), len(maze[0])
        EMPTY, WALL, VISITED = '.', '+', 'x'
        DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))

        q = deque()
        q.append(entrance)
        maze[entrance[0]][entrance[1]] = VISITED
        steps = 1

        while q:

            border_len = len(q)

            for _ in range(border_len):
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:

                    nr, nc = r + dr, c + dc

                    if (nr in range(ROWS) and nc in range(COLS)):
                        if maze[nr][nc] == EMPTY:
                            if nr in (0, ROWS-1) or nc in (0, COLS-1):
                                return steps
                            q.append((nr, nc))
                            maze[nr][nc] = VISITED

            steps += 1

        return -1
