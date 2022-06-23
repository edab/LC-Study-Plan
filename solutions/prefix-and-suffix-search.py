# Leetcode 745. Prefix and Suffix Search
#
# Link: https://leetcode.com/problems/prefix-and-suffix-search/
# Difficulty: Hard

# Solution using a Trie
# Complexity:
#   O(K*N) time | where K and N represent the average length of the words in the
#                  trie and the number of words
#   O(K*N) space | where K and N represent the average length of the keys in the
#                  trie and the number of words
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_indices = dict() # The very same word can appear many times in the words list

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        for char in word:
            node.children[char] = node.children.get(char,TrieNode())
            node = node.children[char]
            node.word_indices[word] = max(node.word_indices.get(word,0), index)

    def search_prefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]

        return set(node.word_indices.values())


class WordFilter:

    def __init__(self, words: List[str]):

        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        self.cache = dict()

        for i, word in enumerate(words):
            self.prefix_trie.insert(word, i)
            self.suffix_trie.insert(word[::-1], i)

    def f(self, prefix: str, suffix: str) -> int:

        prefix_indices = self.prefix_trie.search_prefix(prefix)
        suffix_indices = self.suffix_trie.search_prefix(suffix[::-1])

        if not prefix_indices or not suffix_indices:
            return -1

        result = prefix_indices.intersection(suffix_indices)

        return max(result)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
