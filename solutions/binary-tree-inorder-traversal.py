# Leetcode 94. Binary Tree Inorder Traversal
#
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def recursive(root):
          if not root:
            return []
          return recursive(root.left) + [root.val] + recursive(root.right)

        def iterative(root):
          stack = []
          result = []
          while root or stack:
            while root:
              stack.append(root)
              root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

          return result

        return iterative(root)
