# Leetcode 771. Jewels and Stones
#
# Link: https://leetcode.com/problems/jewels-and-stones/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the stone array
#   O(M) space | where M represent the number of elements in the jewels array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

      def mirror(array, start, end):

        while start < end:
          array[start], array[end] = array[end], array[start]
          start, end = start + 1, end - 1

      k = k % len(nums)

      mirror(nums, 0, len(nums)-1)
      mirror(nums, 0, k-1)
      mirror(nums, k, len(nums)-1)
