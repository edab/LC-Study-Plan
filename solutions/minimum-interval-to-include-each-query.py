# Leetcode 1851. Minimum Interval to Include Each Query
#
# Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Difficulty: Hard

# Solution using sorting.
# Complexity:
#   O(NlogN + QlogQ) time | where N represent the number of intervals and Q the
#                           number of queries
#   O(M) space | where Q represent the max number of overlapping intervals
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # Sort only intervals, queries should be preserved
        intervals.sort(key = lambda pair : pair[0])
        minHeap = [] # We preserve a tuple (size, right), so we pop the smaller
                     # first, and the leftmost first
        index = 0
        result = {}  # For preserving the original query order

        for query in sorted(queries):

            # Add intervals that starts before
            while index < len(intervals) and intervals[index][0] <= query:
                left, right = intervals[index]
                heapq.heappush(minHeap, (right - left + 1, right))
                index += 1

            # Remove intervals that ends before the current query
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            # Save the min if exist
            result[query] = minHeap[0][0] if minHeap else -1

        return [result[q] for q in queries]
