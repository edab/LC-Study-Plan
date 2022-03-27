# Leetcode 102. Binary Tree Level Order Traversal
#
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using BSP.
# Complexity:
#   O(N) time | where N represent the number of nodes in the tree
#   O(M) space | where M represent the number of nodes in one level
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = list()

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            level = list()
            for i in range(level_size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result
