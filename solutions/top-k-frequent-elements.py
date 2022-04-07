# Leetcode 347. Top K Frequent Elements
#
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Complexity:
#   for bucket sort version
#     O(N) | where N represent the number of elements in the array
#   for the heap version
#     O(KlogN) time | where N represent the number of elements in the array and
#                       K is given
#   O(N) space

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      def using_bucket_sort():

        frequency = [[] for _ in range(len(nums) + 1)]
        counters = {}
        result = []

        for num in nums:
          counters[num] = 1 + counters.get(num, 0)

        for num, count in counters.items():
          frequency[count].append(num)

        for i in range(len(frequency) - 1, 0, -1):
          for value in frequency[i]:
            result.append(value)
            if len(result) >= k:
              return result

      def using_min_heap():

        counters = {}
        counts = []
        result = []

        for num in nums:
          counters[num] = 1 + counters.get(num, 0)
        for num, count in counters.items():
          counts.append((-count, num))

        heapq.heapify(counts)

        for _ in range(k):
          result.append(heapq.heappop(counts)[1])

        return result

      return using_min_heap()
