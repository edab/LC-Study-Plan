# Leetcode 117. Populating Next Right Pointers in Each Node II
#
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
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
#   O(N) space | where N represent the number of nodes in the input tree
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def bfs(node):

            queue = deque([node])

            while queue and node:
                n = len(queue)
                for i in range(len(queue)):
                    node = queue.popleft()
                    if i < n - 1:
                        node.next = queue[0]
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        bfs(root)

        return root
