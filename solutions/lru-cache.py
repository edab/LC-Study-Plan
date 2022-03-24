# Leetcode 146. LRU Cache
#
# Link: https://leetcode.com/problems/lru-cache/
# Difficulty: Medium
# Complexity:
#   O(1) time
#   O(N) space | where N represent the number of elements in the RPN expression

class Node:

    def __init__(self, key = 0, value = 0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0

        self.mru, self.lru = Node(), Node()
        self.mru.next, self.lru.prev = self.lru, self.mru

    def detach_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def insert_node(self, node, at):
        node.next = self.mru.next
        node.prev = self.mru
        node.next.prev = node
        self.mru.next = node

    def update_mru(self, node):

        if node.next or node.prev:
            self.detach_node(node)

        self.insert_node(node, self.mru)

    def check_capacity(self):

        if self.size < self.capacity:
            self.size += 1
            return

        key = self.lru.prev.key

        self.lru.prev = self.cache[key].prev
        self.lru.prev.next = self.lru

        del self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_mru(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
        else:
            self.cache[key] = Node(key, value)
            self.check_capacity()
        self.update_mru(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
