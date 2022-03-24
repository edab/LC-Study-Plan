# Leetcode 310. Minimum Height Trees
#
# Link: https://leetcode.com/problems/minimum-height-trees/
# Difficulty: Medium

# Solution using DFS and modifying the input matrix
# Complexity:
#   O(M*N) time | where M and N represent the rows and cols of the input image
#   O(1) space
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        
