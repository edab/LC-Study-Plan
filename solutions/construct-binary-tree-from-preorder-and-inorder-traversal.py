# Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
#
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using recursion.
# Complexity:
#   O(N) time | where N represent the number of elements in the preorder list
#   O(1) space
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        pivot = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        node.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        return node
