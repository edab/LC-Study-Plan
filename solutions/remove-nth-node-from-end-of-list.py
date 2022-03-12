# Leetcode 19. Remove Nth Node From End of List
#
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N is the number of elemets in the list
#   O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        nth_node = dummy
        tail = head

        while n > 0 and tail:
          tail = tail.next
          n -= 1

        while tail:
          nth_node = nth_node.next
          tail = tail.next

        nth_node.next = nth_node.next.next

        return dummy.next
