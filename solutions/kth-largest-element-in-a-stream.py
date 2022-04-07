# Leetcode 703. Kth Largest Element in a Stream
#
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Difficulty: Easy
# Complexity:
#   O(logN) time for each add() | where N represent the number of elements in
#                                 the input list
#   O(K) space | where K represent the number of elements we need to consider

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
          heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
          heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
