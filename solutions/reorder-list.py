# Leetcode 143. Reorder List
#
# Link: https://leetcode.com/problems/reorder-list/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using pointer manipulation
# Complexity:
#   O(N) time | where N represent the number of elements in the linked list
#   O(1) space

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next

        # Reverse second half of the list
        slow.next = None
        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        second_half = prev

        # Merge two half lists
        first, second = head, second_half
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
