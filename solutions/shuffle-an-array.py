# Leetcode 384. Shuffle an Array
#
# Link: https://leetcode.com/problems/shuffle-an-array/
# Difficulty: Medium

# Solution using the Fisher-Yates Algorithm.
# Complexity:
#   O(N) time | where N represent the number of elements in the array
#   O(N) time | where N represent the number of elements in the array
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        rand_values = [random.random() for _ in range(len(self.array))]
        rand_indices = [i for i in range(len(self.array))]
        rand_indices.sort(key = lambda i: rand_values[i] )
        self.array = [self.array[i] for i in rand_indices]
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
