# Leetcode 88. Merge Sorted Array
#
# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Complexity:
#   O(N+M) time | where N and M are the length of the two input arrays
#   O(1) space

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        last = m + n - 1

        while m > 0 and n > 0:
          if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
          else:
            nums1[last] = nums2[n-1]
            n -= 1
          last -= 1

        if n > 0:
          nums1[:last+1] = nums2[:n]
