# Leetcode 230. Kth Smallest Element in a BST
#
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium

# Solution using dfs inorder
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        n = 0
        stack = []
        node = root

        if node == None:
            return []

        while stack or node:

            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                n += 1
                if n == k:
                    return node.val
                node = node.right
