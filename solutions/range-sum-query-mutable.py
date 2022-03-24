# Leetcode 303. Range Sum Query - Immutable
#
# Link: https://leetcode.com/problems/range-sum-query-immutable/
# Difficulty: Easy

# Solution using DP
# Complexity:
#   O(N) time (init) | where N represent the number of items in the input list
#   O(logN) time (update) | where N represent the number of items in the input list
#   O(1) time (query)
#   O(1) space

class NumArray:

    def __init__(self, nums: List[int]):

        self.N = len(nums)

        # Allocate tree
        self.segment_tree = [0] * (2 * self.N)

        # Insert leaf nodes (element of the original array)
        for i in range(self.N):
            self.segment_tree[self.N + i] = nums[i]

        # Evaluate parent nodes (sub-sums)
        for i in range(self.N - 1, 0, -1) :
            self.segment_tree[i] = self.segment_tree[i << 1] + self.segment_tree[i << 1 | 1];

    def update(self, index: int, val: int) -> None:

        # Set value at position p
        self.segment_tree[index + self.N] = val

        # Move upward and update parents
        i = index + self.N
        while i > 1:
            self.segment_tree[i >> 1] = self.segment_tree[i] + self.segment_tree[i ^ 1]
            i >>= 1

    def sumRange(self, left: int, right: int) -> int:

        result = 0

        # loop to find the sum in the range
        left += self.N
        right += self.N + 1

        while left < right:

            if left & 1:
                result += self.segment_tree[left]
                left += 1

            if right & 1:
                right -= 1
                result += self.segment_tree[right]

            left >>= 1
            right >>= 1

        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
