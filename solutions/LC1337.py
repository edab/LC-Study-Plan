# Leetcode 1337. The K Weakest Rows in a Matrix
#
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Difficulty: Easy
# Complexity:
#   O(NlogN) time | where N represent the number of elements in the input list
#   O(N) space | where N represent the number of elements in the input list

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

      num_soldiers = []

      def search_border(row):
        index_l, index_r = 0, len(row)
        while index_l < index_r:
          index_m = (index_r + index_l) // 2
          if row[index_m] == 1:
            index_l = index_m + 1
          else:
            index_r = index_m

        return index_l

      for i in range(len(mat)):
        num_soldiers.append((search_border(mat[i]),i))

      heapq.heapify(num_soldiers)

      return [heapq.heappop(num_soldiers)[1] for x in range(k)]
