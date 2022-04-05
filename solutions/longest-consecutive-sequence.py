# Leetcode 128. Longest Consecutive Sequence
#
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium

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
