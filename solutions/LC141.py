# Leetcode 141. Linked List Cycle
#
# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the linked list
#   O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

      slow, fast = head, head

      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
          return True

      return False
