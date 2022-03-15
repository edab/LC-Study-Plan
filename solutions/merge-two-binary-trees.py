# Leetcode 617. Merge Two Binary Trees
#
# Link: https://leetcode.com/problems/merge-two-binary-trees/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using DFS and modifying the input matrix
# Complexity:
#   O(M+N) time | where M and N represent the node in two input trees
#   O(1) space

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        root = TreeNode(v1 + v2)

        root.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root
