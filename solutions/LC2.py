# Leetcode 2. Add Two Numbers
#
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Complexity:
#   O(max(M,N)) time | where M and N represent the number of elements in the
#                      two input lists
#   O(max(M,N)) space | where M and N represent the number of elements in the
#                      two input lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode()
        first, second, current = l1, l2, dummyHead
        carry = 0

        while first or second:
          a = first.val if first else 0
          b = second.val if second else 0
          sum = a + b + carry
          carry = sum // 10
          current.next = ListNode(sum % 10)
          current = current.next
          first = first.next if first else None
          second = second.next if second else None

        if carry > 0:
          current.next = ListNode(carry)

        return dummyHead.next
