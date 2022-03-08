# Leetcode 104. Maximum Depth of Binary Tree
#
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of nodes in the tree
#   O(H) space | where H represent the heigth of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs_recursive(node):

          if not node:
            return 0

          return 1 + max(dfs_recursive(node.left), dfs_recursive(node.right))

        def dfs_iterative(node):

          stack = [(node, 1)]
          result = 0

          while stack and node:
            node, depth = stack.pop()
            result = max(result, depth)

            if node.left:
              stack.append((node.left, depth+1))
            if node.right:
              stack.append((node.right, depth+1))

          return result

        def bfs_iterative(node):
          queue = deque([node])
          depth = 0

          while queue and node:
            for i in range(len(queue)):
              node = queue.popleft()
              if node.left:
                queue.append(node.left)
              if node.right:
                queue.append(node.right)
            depth += 1

          return depth

        return dfs_recursive(root)
