# Leetcode 1046. Last Stone Weight
#
# Link: https://leetcode.com/problems/last-stone-weight/
# Difficulty: Easy
# Complexity:
#   O(NlogN) time | where N represent the number of elements in the input list
#   O(N) space | where N represent the number of elements in the input list

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
          first = heapq.heappop(stones)
          second = heapq.heappop(stones)
          if first != second:
            heapq.heappush(stones, first - second)

        stones.append(0)
        return -stones[0]
