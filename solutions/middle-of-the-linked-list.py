# Leetcode 876. Middle of the Linked List
#
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using lists
# Complexity:
#   O(N) time | where N represent the number of nodes in the linked list
#   O(1) space

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node, listLength = head, 0

        while node:
            node = node.next
            listLength += 1

        node, count = head, listLength // 2

        while node and count:
            node = node.next
            count -= 1

        return node
