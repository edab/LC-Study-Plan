# Leetcode 435. Non-overlapping Intervals
#
# Link: https://leetcode.com/problems/non-overlapping-intervals/
# Difficulty: Medium

# Solution using sorting.
# Complexity:
#   O(NlogN) time | where N represent the number of intervals
#   O(1) space
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda pair : pair[0])

        result = 0

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start >= prevEnd:

                # Not overlapping if prevEnd < start
                prevEnd = end

            else:

                # Overlapping if prevEnd > start
                # Remove the longest one
                result += 1
                prevEnd = min(prevEnd, end)

        return result
