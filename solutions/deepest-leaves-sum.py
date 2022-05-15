# Leetcode 1302. Deepest Leaves Sum
#
# Link: https://leetcode.com/problems/deepest-leaves-sum/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using DFS.
# Complexity:
#   O(N) time | where N represent the number of nodes in the input tree
#   O(1)
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        self.max_depth = 0
        self.sum = 0

        def dfs(node, depth):

            if not node:
                return

            if depth > self.max_depth:
                self.max_depth = depth
                self.sum = node.val
            elif self.max_depth == depth:
                self.sum += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return self.sum
