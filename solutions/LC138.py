# Leetcode 138. Copy List with Random Pointer
#
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the linked list
#   O(1) space

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        node = head
        if not head:
          return head

        while node:
          new_node = Node(node.val, node.next)
          node.next = new_node
          node = new_node.next

        node = head

        while node:
          if node.random:
            node.next.random = node.random.next
          node = node.next.next

        node = head
        copy_head = head.next
        result = copy_head

        while result.next:
          node.next = node.next.next
          node = node.next
          result.next = result.next.next
          result = result.next

        return copy_head
