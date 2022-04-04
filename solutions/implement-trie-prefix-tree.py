# Leetcode 208. Implement Trie (Prefix Tree)
#
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium

# Solution using a dictionary
# Complexity:
#   O(N) time | where N represent the average length of the keys in the trie
#   O(N*M) space | where N and M represent the average length of the keys in the
#                  trie and the number of words
class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.setdefault(char, {})
        curr['is_word'] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not char in curr:
                return False
            curr = curr[char]
        return curr.get('is_word', False)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not char in curr:
                return False
            curr = curr[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
