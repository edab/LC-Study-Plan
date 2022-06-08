# Leetcode 572. Subtree of Another Tree
#
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using recursion
# Complexity:
#   O(N * M) time | where N and M represent the number of nodes in the input tree and subRoot tree
#   O(1) space
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.compareTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



    def compareTree(self, source: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not source and not subRoot:
            return True

        if source and subRoot and source.val == subRoot.val:
            return (self.compareTree(source.left, subRoot.left) and
                    self.compareTree(source.right, subRoot.right))

        return False
