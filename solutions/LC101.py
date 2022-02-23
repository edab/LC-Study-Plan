# Leetcode 101. Symmetric Tree
#
# Link: https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of nodes in the tree
#   O(N) space | where N represent the number of nodes in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

      def isMirror(root1, root2):

        if not root1 and not root2:
          return True

        if root1 and root2:
          if root1.val == root2.val:
            return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))

        return False

      return isMirror(root, root)
