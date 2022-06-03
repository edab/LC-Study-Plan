# Leetcode 304. Range Sum Query 2D - Immutable
#
# Link: https://leetcode.com/problems/range-sum-query-2d-immutable/
# Difficulty: Medium

# Solution using DP(prefix_sum)
# Complexity:
#   O(N^2) time (init) | where N represent the number of rows/cols in the input matrix
#   O(1) time (query)
#   O(N^2) space | where N represent the number of rows/cols in the input matrix
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS, COLS = len(matrix), len(matrix[0])

        # Add one additional row on top and col on left to get rid of the edge case
        self.prefixSumMat = [[0] * (COLS + 1) for _ in range((ROWS + 1))]

        for row in range(ROWS):
            prefixSum = 0
            for col in range(COLS):
                prefixSum += matrix[row][col]
                aboveRegionSum = self.prefixSumMat[row][col + 1]
                self.prefixSumMat[row + 1][col + 1] = prefixSum + aboveRegionSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # Take care of the offset introduced to get rid of the edge case
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRightSum = self.prefixSumMat[row2][col2]
        aboveRegionSum = self.prefixSumMat[row1 - 1][col2]
        leftRegionSum = self.prefixSumMat[row2][col1 - 1]
        topLeftCorner = self.prefixSumMat[row1 - 1][col1 - 1]

        return bottomRightSum - aboveRegionSum - leftRegionSum + topLeftCorner

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
