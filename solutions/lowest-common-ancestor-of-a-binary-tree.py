# Leetcode 236. Lowest Common Ancestor of a Binary Tree
#
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using tree traversal returning p or q nodes.
# Complexity:
#   O(N) time | where N represent the number of nodes in the tree
#   O(N) space | where N represent the number of nodes in the tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val in (p.val, q.val):
            return root

        if not root.left and not root.right:
            return None

        left = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        right = self.lowestCommonAncestor(root.right, p, q) if root.right else None
        if left and right:
            return root
        return left if left else right
