# Leetcode 215. Kth Largest Element in an Array
#
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Easy
# Complexity:
#   for sort version
#     O(N log N) | where N represent the number of elements in the array
#   for the heap version
#     O(N+KlogN) time | where N represent the number of elements in the array and
#                       K is given
#   for quick select version
#     O(N) amortized | where N represent the number of elements in the array
#                      and worst case is O(N^2) 
#   O(N) space | where N represent the number of elements in the input array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

      def using_sort():
        nums.sort()
        return nums[-k]

      def using_heap():
        negative = [-x for x in nums]
        heapq.heapify(negative)

        for i in range(k):
          result = heapq.heappop(negative)

        return -result

      def using_quick_select(left, right):
        pivot, current = nums[right], left
        for i in range(left, right):
          if nums[i] <= pivot:
            nums[i], nums[current] = nums[current], nums[i]
            current += 1
        nums[current], nums[right] = nums[right], nums[current]

        if current > len(nums) - k:
          return using_quick_select(left, current - 1)
        elif current < len(nums) - k:
          return using_quick_select(current + 1, right)
        else:
          return nums[current]


      return using_sort(0, len(nums) - 1)
