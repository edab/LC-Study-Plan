# Leetcode 56. Merge Intervals
#
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium

# Solution using sorting.
# Complexity:
#   O(NlogN) time | where N represent the number of intervals
#   O(1) space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda pair : pair[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:

            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output
