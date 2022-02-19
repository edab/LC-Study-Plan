# Leetcode 160. Intersection of Two Linked Lists
#
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

      first, second = headA, headB

      while first != second:
        first = first.next if first else headB
        second = second.next if second else headA

      return first
        
