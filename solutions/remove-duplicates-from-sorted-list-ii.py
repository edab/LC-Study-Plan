# Leetcode 82. Remove Duplicates from Sorted List II
#
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using two pointers
# Complexity:
#   O(N) time | where N is the number of elemets in the list
#   O(1) space
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        prev = sentinel
        node = head

        while node:

            if node.next and node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                prev.next = node.next
            else:
                prev = prev.next

            node = node.next

        return sentinel.next
