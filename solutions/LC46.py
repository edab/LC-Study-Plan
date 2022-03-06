# Leetcode 46. Permutations
#
# Link: https://leetcode.com/problems/permutations/
# Difficulty: Medium
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(N!) space | where N represent the number of elements in the input array

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):

            num = nums.pop(0)

            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(num)

            result.extend(permutations)

            nums.append(num)

        return result
