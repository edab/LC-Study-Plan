# Leetcode 820. Short Encoding of Words
#
# Link: https://leetcode.com/problems/short-encoding-of-words/
# Difficulty: Medium

# Solution using a Trie
# Complexity:
#   O(K*N) time | where K and N represent the average length of the words in the
#                  trie and the number of words
#   O(K*N) space | where K and N represent the average length of the keys in the
#                  trie and the number of words
class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node[char] = node.get(char,dict())
            node = node[char]

    def count(self, root, level):
        if len(root) == 0:
            return level
        count = 0
        for key in root.keys():
            count += self.count(root[key], level + 1)
        return count

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        trie = Trie()

        # Reverse all the words first [time, me] -> index 0, 2
        words = map(lambda x:x[::-1], words)

        for word in words:
            trie.insert(word)

        return trie.count(trie.root, 1)
