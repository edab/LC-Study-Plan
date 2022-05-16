# Leetcode 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#
# Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of nodes in the tree
#   O(N) space | where N represent the number of nodes in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        if original == target:
            return cloned

        if not original:
            return None

        res = self.getTargetCopy(original.left, cloned.left, target)

        if not res:
            res = self.getTargetCopy(original.right, cloned.right, target)

        return res
