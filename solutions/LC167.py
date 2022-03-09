# Leetcode 167. Two Sum II - Input Array Is Sorted
#
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Easy

# Complexity:
#   O(N) time | where N represent the number of elements in the array
#   O(N) space | where N represent the number of elements in the array
# Tags: HashMap
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = dict()
        for i in range(len(numbers)):
            if numbers[i] in cache:
                return [cache[numbers[i]] + 1, i + 1]
            else:
                cache[target - numbers[i]] = i
        raise ValueError("Input array not contain sum")

# Complexity:
#   O(N) time | where N represent the number of elements in the array
#   O(1) space
# Tags: TwoPointers
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
