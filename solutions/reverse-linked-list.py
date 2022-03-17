# Leetcode 206. Reverse Linked List
#
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using multiple assignements
# Complexity:
#   O(N) time | where N represent the number of nodes in the linked list
#   O(1) space

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next

# Solution using recursion
# Complexity:
#   O(N) time | where N represent the number of nodes in the linked list
#   O(N) time | where N represent the number of nodes in the linked list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
