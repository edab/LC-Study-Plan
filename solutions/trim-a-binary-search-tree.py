# Leetcode 669. Trim a Binary Search Tree
#
# Link: https://leetcode.com/problems/trim-a-binary-search-tree/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using recursion
# Complexity:
#   O(N) time | where N represent the number of elements in the input tree
#   O(1) space| where N represent the number of elements in the input tree
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left, low, high)

        if root.val < low:
            return self.trimBST(root.right, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
