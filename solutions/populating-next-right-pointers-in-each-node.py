# Leetcode 116. Populating Next Right Pointers in Each Node
#
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Difficulty: Medium

# Definition for a Node.
#class Node:
#    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
#                   next: 'Node' = None):
#        self.val = val
#        self.left = left
#        self.right = right
#        self.next = next

# Solution using DFS and modifying the input matrix
# Complexity:
#   O(N) time | where N represent the number of nodes in the input tree
#   O(1) space

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def buildConnectedTree(node: 'Optional[Node]'):
            if not node:
                return
            if node.left:
                node.left.next = node.right
            if node.right and node.next:
                node.right.next = node.next.left
            buildConnectedTree(node.left)
            buildConnectedTree(node.right)

        buildConnectedTree(root)

        return root
