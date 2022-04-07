# Leetcode 128. Longest Consecutive Sequence
#
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium

# Solution using Disjoint Set Union Find
# Complexity:
#   O(α(N)) time | where N represent the length of the input list and α is the
#                  Ackermann function
#   O(N) space | where N represent the length of the input list
class DSU:

    def __init__(self, nums):
        self._group = {}
        self._size = {}
        for num in nums:
            self.make_set(num)

    def __contains__(self, value):
        return value in self._group

    def __iter__(self):
        return iter(self._group.keys())

    def make_set(self, value):
        self._group[value] = value
        self._size[value] = 1

    def find(self, value):
        if self._group[value] != value:
            self._group[value] = self.find(self._group[value])
        return self._group[value]

    def union(self, value_a, value_b):
        rank_a, rank_b = self.find(value_a), self.find(value_b)
        if rank_a != rank_b:
            self._group[rank_b] = rank_a
            self._size[rank_a] += self._size[rank_b]

    def longest_group(self):
        return max(self._size.values())

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        disjoint_set = DSU(nums)

        for num in disjoint_set:
            if num - 1 in disjoint_set:
                disjoint_set.union(num, num-1)
            if num + 1 in disjoint_set:
                disjoint_set.union(num, num+1)

        return disjoint_set.longest_group()

# Solution using Hashset
# Complexity:
#   O(M*N) time | where M represent the mean length of a sequence and
#                 and N the length of the input list
#   O(N) space | where N represent the length of the input list
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_size = 0

        for num in nums:

            left = right = num

            while (left - 1) in nums_set:
                left -= 1
                nums_set.remove(left)


            while (right + 1) in nums_set:
                right += 1
                nums_set.remove(right)

            max_size = max(max_size, right - left + 1)

        return max_size

# Solution using HashMap
#   O(N) time  | where N represent the length of the input list
#   O(N) space | where N represent the length of the input list
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        result = 1
        lengths = {key: 0 for key in num}

        for num in nums:

            if lengths[num] == 0:

                lengths[num] = 1
                left, right = lengths.get(num - 1, 0), lengths.get(num + 1, 0)
                length = 1 + left + right
                result, lengths[num - left], lengths[num + right] = max(result, length), length, length

        return result
