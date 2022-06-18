# Leetcode 968. Binary Tree Cameras
#
# Link: https://leetcode.com/problems/binary-tree-cameras/
# Difficulty: Hard

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using DFS
# Complexity:
#   O(N) time | where N represent the number of nodes in the given tree
#   O(H) space | where H represent the height of the given tree
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        result = 0
        visited = {None}

        def dfs(node, parent = None):

            nonlocal result

            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if ( parent is None
                     and node not in visited
                     or node.left not in visited
                     or node.right not in visited):

                    result += 1
                    visited.update({node, parent, node.left, node.right})

        dfs(root)
        return result
