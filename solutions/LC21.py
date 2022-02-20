# Leetcode 21. Merge Two Sorted Lists
#
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Complexity:
#   O(N+M) time | where N and M are the number of nodes in the two linked lists
#   O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

      dummy = ListNode()
      current = dummy

      while list1 and list2:
        if list1.val < list2.val:
          current.next = list1
          list1 = list1.next
        else:
          current.next = list2
          list2 = list2.next
        current = current.next

      if list1:
        current.next = list1
      elif list2:
        current.next = list2

      return dummy.next
