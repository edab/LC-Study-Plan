# Leetcode 98. Validate Binary Search Tree
#
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the input tree
#   O(N) space | where N represent the number of elements in the input tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:

    def is_valid(node, left_limit, right_limit):
      if not node:
        return True
      if not (left_limit < node.val < right_limit):
        return False
      return (is_valid(node.left, left_limit, node.val) and is_valid(node.right, node.val, right_limit))

    def dfs_bfs_check_iterative(node):
      if not node:
        return True
      stack = []
      previous = None
      while node or stack:
        while node:
          stack.append(node)
          node = node.left
        node = stack.pop()
        if previous and node.val <= previous.val:
          return False
        previous = node
        node = node.right
      return True

    return dfs_bfs_check_iterative(root)
