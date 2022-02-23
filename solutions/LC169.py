# Leetcode 169. Majority Element
#
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:
  def majorityElement(self, nums: List[int]) -> int:

    def using_sort():
      nums.sort()
      return nums[len(nums) // 2]

    def using_boyer_moore_algorithm():
      count, result = 0, 0
      for num in nums:
        if count == 0:
          result = num
        if num != result:
          count -= 1
        else:
          count += 1
      return result

    def using_counter():
      count = Counter(nums)
      most_common = count.most_common(1)
      return most_common[0][0]

    return using_boyer_moore_algorithm()
