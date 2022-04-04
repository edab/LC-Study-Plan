# Leetcode 211. Design Add and Search Words Data Structure
#
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Difficulty: Medium

# Solution using a dictionary
# Complexity:
#   O(N) time | where N represent the average length of the keys in the trie
#   O(N*M) space | where N and M represent the average length of the keys in the
#                  trie and the number of words
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:

        def dfs(start, node):

            for index in range(start, len(word)):
                char = word[index]
                if char == '.':
                    for child in node.children.values():
                        if dfs(index+1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]

            return node.is_word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
