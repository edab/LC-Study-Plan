# Leetcode 103. Binary Tree Zigzag Level Order Traversal
#
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = list()
        q = deque()
        reverse = False

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
                if reverse:
                    result.append(level[::-1])
                else:
                    result.append(level)
                reverse = False if reverse else True

        return result
