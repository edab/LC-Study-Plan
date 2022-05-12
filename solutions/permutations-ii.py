# Leetcode 47. Permutations II
#
# Link: https://leetcode.com/problems/permutations-ii/
# Difficulty: Medium

# Solution using DFS
# Complexity:
#   O(N * 2^N) time | where N represent the number of elements in the input string
#   O(N) space | where N represent the number of elements in the input string
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        count = { n:0 for n in nums }

        for n in nums:
            count[n] += 1

        def dfs():
            if len(nums) == len(permutation):
                result.append(permutation.copy())
                return
            for n in count:
                if count[n] > 0:
                    permutation.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    permutation.pop()

        dfs()

        return result
