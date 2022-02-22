# Leetcode 26. Remove Duplicates from Sorted Array
#
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        first, second = 0, 1

        while second < len(nums):
          if nums[first] != nums[second]:
            if second == first + 1:
              first += 1
              second += 1
            else:
              nums[first+1] = nums[second]
              first += 1
          else:
            second += 1

        return first+1
