# Leetcode 39. Combination Sum
#
# Link: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium
# Complexity:
#   O(M * N * 4^k) time | where M and N represent the size of the board, and K
#                         is the length of the given board
#   O(M * N) space | where M and N represent the size of the board

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

    def add(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROWS, COLS = len(board), len(board[0])
        DIRS = ((-1,0), (1,0), (0,-1), (0,1))
        trie = TrieNode()
        result = list()
        visited = set()

        def dfs(parent, r, c):

            char = board[r][c]
            node = parent.children[char]

            if node.is_word:
                node.is_word = False
                result.append(node.word)

            visited.add((r,c))

            for dr, dc in DIRS:

                nr, nc = r + dr, c + dc

                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    board[nr][nc] in node.children and
                    (nr, nc) not in visited):

                    dfs(node, nr, nc)

            visited.remove((r,c))

            if len(node.children) == 0:
                parent.children.pop(char)

        for word in words:
            trie.add(word)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie.children:
                    dfs(trie, r, c)

        return result
